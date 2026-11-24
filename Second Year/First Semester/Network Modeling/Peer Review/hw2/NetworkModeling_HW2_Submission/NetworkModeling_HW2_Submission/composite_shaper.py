"""Homework 2: TBF followed by FIFO, non-preemptive LBF.
Run: python3 composite_shaper.py --rho 1000000 --bucket 5000 --input-buffer 100000 --mu 1000000 --output-buffer 100000
Times in seconds; lengths and buffers in bytes. Output timestamps are transmission completion times.
"""
import argparse
from collections import deque
from shaper import read_packets, token_bucket, write_trace


def leaky_bucket(packets, mu, buffer_capacity):
    """FIFO work-conserving transmitter. Output buffer counts waiting packets only.

    At a transmission completion, a waiting packet starts before new arrivals
    with the same timestamp. A packet currently transmitting does not occupy
    the waiting buffer.
    """
    if mu <= 0 or buffer_capacity < 0:
        raise ValueError('mu must be positive and output buffer nonnegative')
    queue = deque()
    waiting_bytes = 0
    finish = float('inf')
    active = None
    output = []
    dropped = []
    i = 0
    while i < len(packets) or active is not None or queue:
        arrival = packets[i][1] if i < len(packets) else float('inf')
        if active is not None and finish <= arrival:
            packet_id, _, length = active
            output.append((packet_id, finish, length))
            active = None
            if queue:
                active = queue.popleft()
                waiting_bytes -= active[2]
                finish += active[2] / mu
            else:
                finish = float('inf')
        else:
            packet = packets[i]
            i += 1
            if active is None:
                active = packet
                finish = arrival + packet[2] / mu
            elif waiting_bytes + packet[2] <= buffer_capacity:
                queue.append(packet)
                waiting_bytes += packet[2]
            else:
                dropped.append(packet[0])
    return output, dropped


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', default='Input_Traffic_Trace.txt')
    parser.add_argument('--output', default='Output_Traffic_Trace.txt')
    parser.add_argument('--rho', type=float, default=1000000.0)
    parser.add_argument('--bucket', type=int, default=5000)
    parser.add_argument('--input-buffer', type=int, default=100000)
    parser.add_argument('--mu', type=float, default=1000000.0)
    parser.add_argument('--output-buffer', type=int, default=100000)
    args = parser.parse_args()
    source = read_packets(args.input)
    tbf_output, tbf_dropped = token_bucket(source, args.rho, args.bucket, args.input_buffer)
    lbf_output, lbf_dropped = leaky_bucket(tbf_output, args.mu, args.output_buffer)
    write_trace(args.output, lbf_output)
    print(f'Input packets: {len(source)}')
    print(f'TBF forwarded: {len(tbf_output)}; TBF dropped: {len(tbf_dropped)}')
    print(f'LBF forwarded: {len(lbf_output)}; LBF dropped: {len(lbf_dropped)}')
    print(f'Total dropped: {len(tbf_dropped) + len(lbf_dropped)}')
    print(f'Saved final trace: {args.output}')


if __name__ == '__main__':
    main()
