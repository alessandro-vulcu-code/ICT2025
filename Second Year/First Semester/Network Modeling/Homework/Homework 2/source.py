"""Empirical Zoom batch-renewal source fitted to Homework 1's training CSV."""
from pathlib import Path
import argparse
import math
import numpy as np

ROOT = Path(__file__).resolve().parent
TRAINING = ROOT / 'data/zoom_training_180s.csv'


def fit_cycles(path=TRAINING, threshold=0.001):
    data = np.loadtxt(path, delimiter=',', skiprows=1, ndmin=2)
    times, lengths = data[:, 0], data[:, 1]
    if (len(times) < 3 or not np.isfinite(data).all() or
            np.any(np.diff(times) < 0) or np.any(lengths <= 0) or
            np.any(lengths != lengths.astype(int))):
        raise ValueError('Training data must contain ordered times and positive integer lengths')
    starts = np.r_[0, np.flatnonzero(np.diff(times) > threshold) + 1]
    cycles = []
    # Exactly the boundary exclusion and complete joint tuples used in Homework 1.
    for i in range(1, len(starts) - 1):
        lo, hi = starts[i:i + 2]
        cycles.append((times[hi] - times[lo], times[lo:hi] - times[lo],
                       lengths[lo:hi].astype(int)))
    if not cycles:
        raise ValueError('No complete training cycles')
    return cycles


def generate(cycles, duration=600.0, seed=2026, simultaneous=True):
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError('Duration must be finite and positive')
    rng = np.random.default_rng(seed)
    packets, epoch = [], 0.0
    while epoch < duration:
        interval, offsets, lengths = cycles[rng.integers(len(cycles))]
        for offset, length in zip(offsets, lengths):
            timestamp = epoch if simultaneous else epoch + float(offset)
            if timestamp < duration:
                packets.append((len(packets) + 1, timestamp, int(length)))
        epoch += float(interval)
    return packets


def write_trace(path, packets):
    with open(path, 'w', newline='') as stream:
        for pid, timestamp, length in packets:
            stream.write(f'{pid}\t{timestamp:.12f}\t{length}\n')


def read_trace(path):
    packets, seen, previous = [], set(), -1.0
    with open(path) as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            try:
                pid_text, time_text, length_text = line.split()
                pid, timestamp, length = int(pid_text), float(time_text), int(length_text)
                if (pid in seen or pid < 0 or not math.isfinite(timestamp) or
                        timestamp < 0 or timestamp < previous or length <= 0):
                    raise ValueError('invalid fields')
            except ValueError as exc:
                raise ValueError(f'{path}:{line_number}: invalid trace row') from exc
            packets.append((pid, timestamp, length))
            seen.add(pid)
            previous = timestamp
    return packets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--training', type=Path, default=TRAINING)
    parser.add_argument('--duration', type=float, default=1800)
    parser.add_argument('--seed', type=int, default=2026)
    parser.add_argument('--preserve-offsets', action='store_true',
                        help='Use Homework 1 packet offsets instead of simultaneous batches')
    parser.add_argument('--output', type=Path, default=ROOT / 'Input_Traffic_Trace.txt')
    args = parser.parse_args()
    packets = generate(fit_cycles(args.training), args.duration, args.seed, not args.preserve_offsets)
    write_trace(args.output, packets)
    print(f'{len(packets)} packets written to {args.output}')


if __name__ == '__main__':
    main()
