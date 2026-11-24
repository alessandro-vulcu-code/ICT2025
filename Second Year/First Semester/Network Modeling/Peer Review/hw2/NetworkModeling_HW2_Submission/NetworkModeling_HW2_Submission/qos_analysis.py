"""Homework 2: QoS metrics from the input and final output traces.
Run: python3 qos_analysis.py
Times are seconds, sizes bytes. Jitter = mean absolute difference of
successive delivered packets' one-way shaper delays, ordered by input ID.
"""
import argparse
import math
from statistics import mean
from shaper import read_packets


def percentile(values, p):
    ordered = sorted(values)
    if not ordered:
        return float('nan')
    position = (len(ordered) - 1) * p / 100
    lo = math.floor(position)
    hi = math.ceil(position)
    return ordered[lo] + (ordered[hi] - ordered[lo]) * (position - lo)


def analyze(input_path, output_path):
    source = read_packets(input_path)
    result = read_packets(output_path)
    source_by_id = {pid: (t, length) for pid, t, length in source}
    result_by_id = {pid: (t, length) for pid, t, length in result}
    if len(source_by_id) != len(source) or len(result_by_id) != len(result):
        raise ValueError('Duplicate packet IDs')
    if not set(result_by_id).issubset(source_by_id):
        raise ValueError('Output contains unknown packet IDs')
    for pid, (end, length) in result_by_id.items():
        start, original_length = source_by_id[pid]
        if length != original_length or end < start:
            raise ValueError(f'Invalid output packet {pid}')
    delivered = [pid for pid, _, _ in source if pid in result_by_id]
    delays = [result_by_id[pid][0] - source_by_id[pid][0] for pid in delivered]
    jitter = mean(abs(b - a) for a, b in zip(delays, delays[1:])) if len(delays) > 1 else float('nan')
    duration = max(t for _, t, _ in result) - min(t for _, t, _ in source) if result else float('nan')
    throughput = sum(length for _, _, length in result) / duration if duration > 0 else float('nan')
    print(f'Input packets: {len(source)}')
    print(f'Delivered packets: {len(result)}')
    print(f'Lost packets: {len(source) - len(result)}')
    print(f'Packet loss rate: {100 * (len(source) - len(result)) / len(source):.4f} %')
    print(f'Mean delay: {mean(delays) * 1000:.3f} ms' if delays else 'Mean delay: N/A')
    print(f'P95 delay: {percentile(delays, 95) * 1000:.3f} ms')
    print(f'P99 delay: {percentile(delays, 99) * 1000:.3f} ms')
    print(f'Mean absolute delay variation (jitter): {jitter * 1000:.3f} ms')
    print(f'Output throughput: {throughput * 8 / 1e6:.3f} Mbit/s')
    print(f'Observation interval (first input to last output): {duration:.3f} s')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', default='Input_Traffic_Trace.txt')
    parser.add_argument('--output', default='Output_Traffic_Trace.txt')
    args = parser.parse_args()
    analyze(args.input, args.output)
