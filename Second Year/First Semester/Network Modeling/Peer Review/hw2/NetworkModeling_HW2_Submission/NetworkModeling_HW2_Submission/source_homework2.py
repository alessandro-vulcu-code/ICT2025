"""Homework 2 source module: synthetic Google Meet packet trace.

Run: python3 source_homework2.py --csv google-meet-incoming.csv
Optional: --batches 31339 --seed 42 --output Input_Traffic_Trace.txt
Output columns (no header): packet_id, generation_time_seconds, length_bytes.
"""
import argparse
import csv
import random
from collections import Counter

Q_SINGLETON = 0.5701841156386611
P_GEOMETRIC = 0.30284635100499124
BATCH_GAP_THRESHOLD = 0.0001
MEAN_INTER_BATCH_GAP = 0.007132435030952838


def generate(csv_path, output_path, batches, seed):
    rng = random.Random(seed)
    lengths = []
    with open(csv_path, newline="") as source:
        for row in csv.DictReader(source):
            lengths.append(int(row["Length"]))
    if not lengths:
        raise ValueError("Input CSV has no packet lengths")
    counts = Counter(lengths)
    sizes, weights = zip(*sorted(counts.items()))
    current_time = 0.0
    packet_id = 0
    with open(output_path, "w", newline="") as target:
        writer = csv.writer(target)
        for batch_idx in range(batches):
            batch_size = 1
            if rng.random() >= Q_SINGLETON:
                batch_size = 2
                while rng.random() > P_GEOMETRIC:
                    batch_size += 1
            packet_lengths = rng.choices(sizes, weights=weights, k=batch_size)
            for length in packet_lengths:
                packet_id += 1
                writer.writerow((packet_id, f"{current_time:.9f}", length))
            if batch_idx < batches - 1:
                current_time += BATCH_GAP_THRESHOLD + rng.expovariate(
                    1 / (MEAN_INTER_BATCH_GAP - BATCH_GAP_THRESHOLD)
                )
    return packet_id, current_time


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", default="google-meet-incoming.csv")
    parser.add_argument("--output", default="Input_Traffic_Trace.txt")
    parser.add_argument("--batches", type=int, default=31339)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    if args.batches < 1:
        parser.error("--batches must be positive")
    n, duration = generate(args.csv, args.output, args.batches, args.seed)
    print(f"Generated {n} packets in {args.batches} batches")
    print(f"Last packet generation time: {duration:.3f} s")
    print(f"Saved: {args.output}")
