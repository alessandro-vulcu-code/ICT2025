#!/usr/bin/env python3
"""Transcribe an English lecture with silence and repetition-loop safeguards."""

from __future__ import annotations

import argparse
import ctypes
import os
import sys
import time
from pathlib import Path

import av
import ctranslate2
from faster_whisper import BatchedInferencePipeline, WhisperModel
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


def configure_cuda_libraries() -> None:
    """Expose CUDA 12 wheels to the dynamic linker, including cuDNN sublibraries.

    A script-local installation takes priority over Python's installed wheels:
    python -m pip install --target .transcribe-cuda nvidia-cublas-cu12 nvidia-cudnn-cu12
    This avoids replacing CUDA 13 packages used by other applications.
    """
    if not sys.platform.startswith("linux"):
        return

    roots = [Path(__file__).resolve().parent / ".transcribe-cuda"]
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


def enable_pyav_compatibility() -> None:
    """Handle removal of metadata_errors from PyAV 19."""
    original_open = av.open

    def compatible_open(*args, **kwargs):
        try:
            return original_open(*args, **kwargs)
        except TypeError as error:
            if "metadata_errors" not in kwargs or "metadata_errors" not in str(error):
                raise

            kwargs.pop("metadata_errors")
            return original_open(*args, **kwargs)

    av.open = compatible_open


def download_model_with_progress(model_name: str) -> str:
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Transcribe an English audio/video lecture using faster-whisper."
    )
    parser.add_argument("input", type=Path, help="Audio or video file to transcribe")
    parser.add_argument(
        "--batch-size",
        type=positive_int,
        default=1,
        help=(
            "Parallel audio chunks (default: 1, sequential decoding with silence "
            "safeguards; larger values are faster but bypass those safeguards)"
        ),
    )
    parser.add_argument(
        "--beam-size",
        type=positive_int,
        default=5,
        help="Beam search width (default: 5; use 1 to prioritize speed over accuracy)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output text file (default: <input>.transcript.txt)",
    )
    parser.add_argument(
        "-m",
        "--model",
        default="medium.en",
        help="Whisper model name or local path (default: medium.en)",
    )
    parser.add_argument(
        "--device",
        choices=("auto", "cpu", "cuda"),
        default="auto",
        help="Inference device (default: auto)",
    )
    parser.add_argument(
        "--compute-type",
        default="auto",
        help="CTranslate2 compute type (default: int8 on CPU, int8_float16 on CUDA)",
    )
    parser.add_argument(
        "--plain",
        action="store_true",
        help="Do not add timestamps to transcript",
    )
    parser.add_argument(
        "--no-vad",
        action="store_true",
        help="Disable voice activity detection",
    )
    args = parser.parse_args()
    if args.no_vad and args.batch_size is not None and args.batch_size > 1:
        parser.error("--no-vad requires --batch-size 1")
    return args


def positive_int(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return number


def format_time(seconds: float) -> str:
    total_seconds = max(0, round(seconds))
    hours, remainder = divmod(total_seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def select_device(requested: str) -> str:
    """Check CUDA dependencies before loading a model or opening its output."""
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


def main() -> int:
    args = parse_args()
    input_path = args.input.expanduser().resolve()

    if not input_path.is_file():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return 1

    if args.device != "cpu":
        configure_cuda_libraries()

    output_path = (
        args.output.expanduser()
        if args.output
        else input_path.with_name(f"{input_path.stem}.transcript.txt")
    )
    output_path = output_path.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        device = select_device(args.device)
    except RuntimeError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    if args.compute_type == "auto":
        compute_type = "int8_float16" if device == "cuda" else "int8"
    else:
        compute_type = args.compute_type

    batch_size = args.batch_size

    try:
        downloaded_model = download_model_with_progress(args.model)
    except Exception as error:
        print(f"Error downloading model: {error}", file=sys.stderr)
        return 1

    print(f"Loading model {args.model!r} on {device} ({compute_type})...")
    model = WhisperModel(downloaded_model, device=device, compute_type=compute_type)

    print(f"Transcribing: {input_path} (batch={batch_size}, beam={args.beam_size})")
    enable_pyav_compatibility()
    transcriber = BatchedInferencePipeline(model=model) if batch_size > 1 else model
    batch_options = {"batch_size": batch_size} if batch_size > 1 else {}
    if batch_size > 1:
        print(
            "Warning: batched decoding bypasses silence hallucination detection "
            "and decoding fallback checks. Use --batch-size 1 if text repeats "
            "or appears during silence.",
            file=sys.stderr,
        )
    else:
        # Silence hallucination detection requires word alignment. The batched
        # pipeline ignores this threshold, so only enable it for sequential use.
        batch_options.update(
            word_timestamps=True,
            hallucination_silence_threshold=2.0,
        )
    started = time.perf_counter()
    segments, info = transcriber.transcribe(
        str(input_path),
        language="en",
        beam_size=args.beam_size,
        vad_filter=not args.no_vad,
        without_timestamps=False,
        # Do not feed invented text back into the next audio window: doing so
        # can sustain repetition loops even after the original bad segment.
        condition_on_previous_text=False,
        **batch_options,
    )

    segment_count = 0
    with output_path.open("w", encoding="utf-8") as output_file:
        for segment in segments:
            text = segment.text.strip()
            if not text:
                continue

            if args.plain:
                line = text
            else:
                line = f"[{format_time(segment.start)}] {text}"

            output_file.write(line + "\n")
            output_file.flush()
            print(line)
            segment_count += 1

    print(
        f"Done: {segment_count} segments, "
        f"detected language={info.language} "
        f"(probability={info.language_probability:.2%})"
    )
    print(f"Transcript saved to: {output_path}")
    elapsed = time.perf_counter() - started
    print(f"Transcription time: {elapsed:.1f}s ({info.duration / max(elapsed, 1e-9):.1f}x real time)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
