"""FIFO token bucket followed by a non-preemptive constant-rate transmitter."""
import argparse
from collections import deque
from dataclasses import dataclass, asdict
import json
import math
from pathlib import Path
from source import ROOT, read_trace, write_trace


@dataclass(frozen=True)
class Config:
    rho: float = 180000  # tokens/s = bytes/s
    b: int = 4096
    bi: int = 16384
    mu: float = 220000  # bytes/s
    bo: int = 4096

    def __post_init__(self):
        if any(not math.isfinite(x) or x <= 0 for x in (self.rho, self.mu)):
            raise ValueError('rho and mu must be finite and positive')
        if any(not isinstance(x, int) or x < 0 for x in (self.b, self.bi, self.bo)):
            raise ValueError('b, bi and bo must be nonnegative integers')


@dataclass
class Result:
    output: list
    drops: list
    releases: list
    occupancy: list
    peak_bi: int
    peak_bo: int


def simulate(packets, config, record=False):
    """Inputs are ordered (id, generation time, bytes), normally from read_trace.

    Start full. Queue capacities count waiting bytes, excluding LBF service.
    At ties: LBF completion, eligible queued TBF releases, then input rows.
    TBF consumes tokens even when its downstream transfer is dropped.
    Oversized packets are dropped before admission. Drain after last arrival.
    """
    c = config
    qi, qo = deque(), deque()
    used_i = used_o = peak_i = peak_o = 0
    tokens, clock, index = float(c.b), 0.0, 0
    busy, completion = None, math.inf
    output, drops, releases, occupancy = [], [], [], []

    def to_lbf(packet, now):
        nonlocal busy, completion, used_o, peak_o
        if record:
            releases.append((packet[0], now, packet[2]))
        if busy is None:
            busy, completion = packet, now + packet[2] / c.mu
        elif used_o + packet[2] <= c.bo:
            qo.append(packet)
            used_o += packet[2]
            peak_o = max(peak_o, used_o)
        else:
            drops.append((packet[0], now, packet[2], 'output_overflow'))

    while index < len(packets) or qi or busy is not None:
        arrival = packets[index][1] if index < len(packets) else math.inf
        ready = clock + max(0.0, qi[0][2] - tokens) / c.rho if qi else math.inf
        now = min(arrival, ready, completion)
        tokens = min(float(c.b), tokens + c.rho * (now - clock))
        clock = now
        if completion <= now:
            output.append((busy[0], now, busy[2]))
            if qo:
                busy = qo.popleft()
                used_o -= busy[2]
                completion = now + busy[2] / c.mu
            else:
                busy, completion = None, math.inf
        while qi and tokens + 1e-7 >= qi[0][2]:
            packet = qi.popleft()
            used_i -= packet[2]
            tokens = max(0.0, tokens - packet[2])
            to_lbf(packet, now)
        while index < len(packets) and packets[index][1] <= now:
            packet = packets[index]
            index += 1
            length = packet[2]
            if length > c.b:
                drops.append((packet[0], now, length, 'larger_than_bucket'))
            elif not qi and tokens + 1e-7 >= length:
                tokens = max(0.0, tokens - length)
                to_lbf(packet, now)
            elif used_i + length <= c.bi:
                qi.append(packet)
                used_i += length
                peak_i = max(peak_i, used_i)
            else:
                drops.append((packet[0], now, length, 'input_overflow'))
        if record:
            occupancy.append((now, used_i, used_o, tokens))
    return Result(output, drops, releases, occupancy, peak_i, peak_o)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=ROOT / 'Input_Traffic_Trace.txt')
    parser.add_argument('--output', type=Path, default=ROOT / 'Output_Traffic_Trace.txt')
    parser.add_argument('--rho', type=float, default=180000)
    parser.add_argument('--b', type=int, default=4096)
    parser.add_argument('--bi', type=int, default=16384)
    parser.add_argument('--mu', type=float, default=220000)
    parser.add_argument('--bo', type=int, default=4096)
    args = parser.parse_args()
    config = Config(args.rho, args.b, args.bi, args.mu, args.bo)
    result = simulate(read_trace(args.input), config, record=True)
    write_trace(args.output, result.output)
    drop_path = args.output.with_name(args.output.stem + '_drops.csv')
    import csv
    with open(drop_path, 'w', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['id', 'time_s', 'bytes', 'reason'])
        writer.writerows(result.drops)
    print(json.dumps(dict(config=asdict(config), delivered=len(result.output),
                          dropped=len(result.drops), peak_bi=result.peak_bi,
                          peak_bo=result.peak_bo), indent=2))


if __name__ == '__main__':
    main()
