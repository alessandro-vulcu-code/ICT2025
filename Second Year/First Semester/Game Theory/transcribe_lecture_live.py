#!/usr/bin/env python3
"""Transcribe Linux system playback through PulseAudio or pipewire-pulse.

Requires faster-whisper, huggingface-hub, tqdm, numpy, ffmpeg and pactl. Audio is buffered on disk so slow inference does not block capture.
"""

from __future__ import annotations

import argparse
import ctypes
import os
from datetime import datetime
import math
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import time


SAMPLE_RATE = 16000
BYTES_PER_SECOND = SAMPLE_RATE * 2


def configure_cuda_libraries() -> None:
    """Expose CUDA 12 wheels to the dynamic linker, including cuDNN sublibraries.

    A script-local installation takes priority over Python's installed wheels:
    python -m pip install --target .transcribe-cuda nvidia-cublas-cu12 nvidia-cudnn-cu12
    This avoids replacing CUDA 13 packages used by other applications.
    """
    if not sys.platform.startswith("linux"):
        return

    script_directory = Path(__file__).resolve().parent
    roots = [script_directory / ".transcribe-cuda", script_directory.parent / ".transcribe-cuda"]
    roots.extend(Path(entry) for entry in sys.path if entry)
    directories = []
    for package, library in (
        ("cuda_nvrtc", "libnvrtc.so.12"),
        ("cublas", "libcublas.so.12"),
        ("cudnn", "libcudnn.so.9"),
    ):
        for root in roots:
            directory = root / "nvidia" / package / "lib"
            if (directory / library).is_file():
                directories.append(str(directory))
                break

    existing = os.environ.get("LD_LIBRARY_PATH", "").split(os.pathsep)
    if directories and existing[:len(directories)] != directories:
        environment = os.environ.copy()
        environment["LD_LIBRARY_PATH"] = os.pathsep.join(
            directories + [entry for entry in existing if entry and entry not in directories]
        )
        # LD_LIBRARY_PATH must be set before the interpreter starts for dlopen.
        os.execvpe(sys.executable, [sys.executable, *sys.argv], environment)


def download_model_with_progress(model_name: str) -> str:
    from faster_whisper.utils import _MODELS
    from huggingface_hub import snapshot_download
    from tqdm.auto import tqdm

    class ModelDownloadProgress(tqdm):
        """Hugging Face progress bar showing percentage, speed, and ETA."""

        def __init__(self, *args, **kwargs):
            kwargs["bar_format"] = (
                "{desc}: {percentage:3.0f}%|{bar}| "
                "{n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]"
            )
            super().__init__(*args, **kwargs)

    model_path = Path(model_name).expanduser()
    if model_path.exists():
        return str(model_path.resolve())

    repo_id = _MODELS.get(model_name, model_name if "/" in model_name else None)
    if repo_id is None:
        valid_models = ", ".join(sorted(_MODELS))
        raise ValueError(
            f"Unknown model {model_name!r}. Available models: {valid_models}"
        )

    print(f"Checking/downloading model: {repo_id}")
    return snapshot_download(
        repo_id,
        allow_patterns=[
            "config.json",
            "preprocessor_config.json",
            "model.bin",
            "tokenizer.json",
            "vocabulary.*",
        ],
        tqdm_class=ModelDownloadProgress,
    )


def format_time(seconds: float) -> str:
    total_seconds = max(0, round(seconds))
    hours, remainder = divmod(total_seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def select_device(requested: str) -> str:
    """Check CUDA dependencies before loading a model or opening its output."""
    import ctranslate2

    if requested == "cpu":
        return "cpu"

    try:
        if ctranslate2.get_cuda_device_count() == 0:
            raise RuntimeError("No CUDA device is available to CTranslate2")
        if sys.platform.startswith("linux"):
            # CTranslate2 loads these lazily, during segment generation.
            for library in ("libcublas.so.12", "libcudnn.so.9"):
                ctypes.CDLL(library)
    except (OSError, RuntimeError) as error:
        message = (
            f"CUDA unavailable: {error}. GPU inference needs cuBLAS for CUDA 12 "
            "and cuDNN 9 for CUDA 12 on LD_LIBRARY_PATH, plus a working NVIDIA "
            "driver. Install isolated CUDA 12 libraries beside this script with: "
            "python -m pip install --target .transcribe-cuda "
            "nvidia-cublas-cu12 nvidia-cudnn-cu12. "
            "See https://github.com/SYSTRAN/faster-whisper#gpu"
        )
        if requested == "cuda":
            raise RuntimeError(message + " Alternatively, use --device cpu.") from error
        print(f"Warning: {message}\nFalling back to CPU.", file=sys.stderr)
        return "cpu"

    return "cuda"


def positive_seconds(value: str) -> float:
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("must be a finite number greater than zero")
    return number


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list-sources", action="store_true", help="List audio sources and exit")
    parser.add_argument("--source", help="PulseAudio source (default: monitor of default output)")
    parser.add_argument("-o", "--output", type=Path, help="New transcript file; existing files are protected")
    parser.add_argument("-m", "--model", default="base.en", help="Model name or path (default: base.en)")
    parser.add_argument("--language", default="en", help="Language code or auto (default: en)")
    parser.add_argument("--device", choices=("auto", "cpu", "cuda"), default="auto")
    parser.add_argument("--compute-type", default="auto")
    parser.add_argument("--chunk-seconds", type=positive_seconds, default=8,
                        help="Audio per inference, minimum 1 second (default: 8)")
    parser.add_argument("--duration", type=positive_seconds, help="Stop capture after this many seconds")
    parser.add_argument("--beam-size", type=int, default=1, help="Beam search width (default: 1)")
    parser.add_argument("--plain", action="store_true", help="Omit timestamps")
    parser.add_argument("--no-vad", action="store_true", help="Disable voice activity detection")
    args = parser.parse_args()
    if args.chunk_seconds < 1:
        parser.error("--chunk-seconds must be at least 1")
    if args.beam_size < 1:
        parser.error("--beam-size must be at least 1")
    return args


def pactl(*arguments: str) -> str:
    if not shutil.which("pactl"):
        raise RuntimeError("pactl is missing. Install your distribution's PulseAudio utilities.")
    result = subprocess.run(["pactl", *arguments], capture_output=True, text=True, timeout=10)
    if result.returncode:
        raise RuntimeError(f"Cannot query audio server: {result.stderr.strip()}")
    return result.stdout.strip()


def resolve_source(requested: str | None) -> str:
    source = requested or f"{pactl('get-default-sink')}.monitor"
    names = [line.split("\t")[1] for line in pactl("list", "short", "sources").splitlines()
             if "\t" in line]
    if source not in names:
        raise RuntimeError(f"Audio source {source!r} not found. Use --list-sources and --source NAME.")
    return source


def stop_capture(process: subprocess.Popen) -> None:
    if process.poll() is None:
        process.send_signal(signal.SIGINT)


def transcribe_live(args, model, output, source: str, format_time) -> None:
    import numpy as np

    # Independent reader/writer descriptors avoid sharing a file position.
    # Mono 16-bit PCM uses roughly 115 MB per captured hour.
    with tempfile.TemporaryDirectory(prefix="lecture-live-") as directory:
        audio_path = Path(directory) / "capture.pcm"
        with audio_path.open("wb") as audio_writer, audio_path.open("rb") as audio_reader, \
                tempfile.TemporaryFile() as errors:
            command = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin",
                       "-f", "pulse", "-i", source, "-ac", "1", "-ar", str(SAMPLE_RATE)]
            if args.duration:
                command += ["-t", str(args.duration)]
            command += ["-f", "s16le", "-acodec", "pcm_s16le", "pipe:1"]
            process = subprocess.Popen(command, stdout=audio_writer, stderr=errors,
                                       start_new_session=True)
            stopping = False

            def request_stop(signum, frame):
                nonlocal stopping
                if stopping:
                    raise KeyboardInterrupt
                stopping = True
                print("\nStopping capture; transcribing remaining audio. Ctrl+C again to exit.",
                      flush=True)
                stop_capture(process)

            old_handler = signal.signal(signal.SIGINT, request_stop)
            old_term = signal.signal(signal.SIGTERM, request_stop)
            chunk_bytes = round(args.chunk_seconds * SAMPLE_RATE) * 2
            pending = bytearray()
            samples_processed = 0
            last_warning = 0.0
            stop_started = None
            try:
                print(f"Listening: {source}\nCapture active. Start/resume your video. Ctrl+C to stop.",
                      flush=True)
                while True:
                    if stopping:
                        if stop_started is None:
                            stop_started = time.monotonic()
                        elif process.poll() is None and time.monotonic() - stop_started > 5:
                            process.kill()
                    pending.extend(audio_reader.read(chunk_bytes - len(pending)))
                    ended = process.poll() is not None
                    if ended and len(pending) < chunk_bytes:
                        # Read once more after exit: the writer may have finished
                        # between the previous read and poll.
                        pending.extend(audio_reader.read(chunk_bytes - len(pending)))
                    if len(pending) < chunk_bytes and not ended:
                        time.sleep(0.05)
                        continue
                    if not pending:
                        break
                    if len(pending) % 2:
                        raise RuntimeError("Capture ended with an incomplete PCM sample")
                    audio = np.frombuffer(pending, dtype="<i2").astype(np.float32) / 32768.0
                    pending = bytearray()
                    offset = samples_processed / SAMPLE_RATE
                    samples_processed += len(audio)
                    segments, _ = model.transcribe(
                        audio, language=None if args.language == "auto" else args.language,
                        beam_size=args.beam_size, vad_filter=not args.no_vad,
                        condition_on_previous_text=False, without_timestamps=False,
                    )
                    for segment in segments:
                        text = segment.text.strip()
                        if text:
                            line = text if args.plain else f"[{format_time(offset + segment.start)}] {text}"
                            output.write(line + "\n")
                            output.flush()
                            print(line, flush=True)
                    backlog = (audio_path.stat().st_size / 2 - samples_processed) / SAMPLE_RATE
                    if backlog > 2 * args.chunk_seconds and time.monotonic() - last_warning > 30:
                        print(f"Warning: transcription is {backlog:.0f}s behind capture. "
                              "Try a smaller model or CUDA.", file=sys.stderr)
                        last_warning = time.monotonic()
                return_code = process.wait()
                if return_code and not stopping:
                    errors.seek(0)
                    detail = errors.read().decode(errors="replace").strip()
                    raise RuntimeError(f"Audio capture failed ({return_code}): {detail}")
            finally:
                signal.signal(signal.SIGINT, old_handler)
                signal.signal(signal.SIGTERM, old_term)
                stop_capture(process)
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait()


def main() -> int:
    args = parse_args()
    try:
        if not sys.platform.startswith("linux"):
            raise RuntimeError("This version requires Linux with PulseAudio or pipewire-pulse.")
        if args.list_sources:
            print(pactl("list", "short", "sources"))
            return 0
        if not shutil.which("ffmpeg"):
            raise RuntimeError("ffmpeg is missing. Install it using your distribution's package manager.")
        source = resolve_source(args.source)
        output_path = (args.output or Path(datetime.now().strftime("live_%Y%m%d_%H%M%S.transcript.txt")))
        output_path = output_path.expanduser().resolve()
        if output_path.exists():
            raise RuntimeError(f"Output already exists: {output_path}. Choose another --output.")

        from faster_whisper import WhisperModel

        if args.device != "cpu":
            configure_cuda_libraries()
        device = select_device(args.device)
        compute_type = args.compute_type
        if compute_type == "auto":
            compute_type = "int8_float16" if device == "cuda" else "int8"
        model_path = download_model_with_progress(args.model)
        print(f"Loading {args.model!r} on {device} ({compute_type})...", flush=True)
        model = WhisperModel(model_path, device=device, compute_type=compute_type)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("x", encoding="utf-8") as output:
            print(f"Transcript: {output_path}", flush=True)
            transcribe_live(args, model, output, source, format_time)
        print(f"Transcript saved to: {output_path}")
        return 0
    except KeyboardInterrupt:
        print("\nStopped. Transcript written so far is saved; pending audio was discarded.", file=sys.stderr)
        return 130
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
