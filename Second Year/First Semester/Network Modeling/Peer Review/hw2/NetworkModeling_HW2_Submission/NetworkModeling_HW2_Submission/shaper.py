"""Homework 2, Part 2: Token Bucket Filter only.

Input:  packet_id,generation_time_seconds,length_bytes (no header)
Output: packet_id,TBF_exit_time_seconds,length_bytes (no header)
This is an INTERMEDIATE trace, not the final composite-shaper output.

Run: python3 shaper.py --rho 1000000 --bucket 5000 --buffer 100000
"""
import argparse
import csv
from collections import deque
from math import inf


def read_packets(path):
    packets = []
    with open(path, newline="") as f:
        for row in csv.reader(f):
            if not row:
                continue
            packet_id, timestamp, length = int(row[0]), float(row[1]), int(row[2])
            if timestamp < 0 or length <= 0:
                raise ValueError("Times must be nonnegative and lengths positive")
            if packets and timestamp < packets[-1][1]:
                raise ValueError("Input must be sorted by timestamp")
            packets.append((packet_id, timestamp, length))
    return packets


def token_bucket(packets, rho, capacity, buffer_capacity):
    """Event-driven FIFO TBF. Buffer counts waiting packets, not forwarded ones."""
    if rho <= 0 or capacity <= 0 or buffer_capacity < 0:
        raise ValueError("rho and bucket must be positive; buffer must be nonnegative")
    queue = deque()
    queued_bytes = 0
    tokens = float(capacity)  # initially full
    now = 0.0
    i = 0
    departures = []
    dropped = []
    while i < len(packets) or queue:
        next_arrival = packets[i][1] if i < len(packets) else inf
        if queue:
            needed = queue[0][2] - tokens
            next_departure = now if needed <= 1e-9 else now + needed / rho
        else:
            next_departure = inf
        next_time = min(next_arrival, next_departure)
        tokens = min(float(capacity), tokens + rho * (next_time - now))
        now = next_time

        # A queued head packet gets priority over arrivals at the same time.
        if queue and tokens + 1e-7 >= queue[0][2]:
            packet_id, generation, length = queue.popleft()
            queued_bytes -= length
            tokens = max(0.0, tokens - length)
            departures.append((packet_id, now, length))
            continue

        # Process one arrival; it cannot bypass a queued packet.
        if i < len(packets) and packets[i][1] <= now + 1e-12:
            packet_id, generation, length = packets[i]
            i += 1
            if length > capacity or queued_bytes + length > buffer_capacity:
                # An immediately forwardable packet needs no buffer space.
                if not queue and length <= capacity and tokens + 1e-7 >= length:
                    tokens = max(0.0, tokens - length)
                    departures.append((packet_id, now, length))
                else:
                    dropped.append(packet_id)
            elif not queue and tokens + 1e-7 >= length:
                tokens = max(0.0, tokens - length)
                departures.append((packet_id, now, length))
            else:
                queue.append((packet_id, generation, length))
                queued_bytes += length
    return departures, dropped


def write_trace(path, packets):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        for packet_id, timestamp, length in packets:
            writer.writerow((packet_id, f"{timestamp:.9f}", length))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="Input_Traffic_Trace.txt")
    parser.add_argument("--output", default="TBF_Trace.txt")
    parser.add_argument("--rho", type=float, default=1000000.0, help="tokens/s")
    parser.add_argument("--bucket", type=int, default=5000, help="tokens")
    parser.add_argument("--buffer", type=int, default=100000, help="bytes")
    args = parser.parse_args()
    packets = read_packets(args.input)
    departures, dropped = token_bucket(packets, args.rho, args.bucket, args.buffer)
    write_trace(args.output, departures)
    print(f"Input packets: {len(packets)}")
    print(f"Forwarded by TBF: {len(departures)}")
    print(f"Dropped by TBF: {len(dropped)}")
    print(f"Saved intermediate trace: {args.output}")


if __name__ == "__main__":
    main()
