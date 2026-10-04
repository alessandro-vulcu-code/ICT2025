#!/usr/bin/env python3
"""Transcribe an English university lecture with faster-whisper."""

from __future__ import annotations

import argparse
import ctypes
import sys
from pathlib import Path

import av
import ctranslate2
from faster_whisper import WhisperModel
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
        help="CTranslate2 compute type (default: int8 on CPU, float16 on CUDA)",
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
    return parser.parse_args()


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
            "driver. See https://github.com/SYSTRAN/faster-whisper#gpu"
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
        compute_type = "float16" if device == "cuda" else "int8"
    else:
        compute_type = args.compute_type

    try:
        downloaded_model = download_model_with_progress(args.model)
    except Exception as error:
        print(f"Error downloading model: {error}", file=sys.stderr)
        return 1

    print(f"Loading model {args.model!r} on {device} ({compute_type})...")
    model = WhisperModel(downloaded_model, device=device, compute_type=compute_type)

    print(f"Transcribing: {input_path}")
    enable_pyav_compatibility()
    segments, info = model.transcribe(
        str(input_path),
        language="en",
        beam_size=5,
        vad_filter=not args.no_vad,
        condition_on_previous_text=True,
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
