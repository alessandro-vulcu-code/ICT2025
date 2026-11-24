"""Boundary and invariant tests for Homework 2. Run: python3 boundary_tests.py"""
import unittest
from collections import Counter
from tempfile import TemporaryDirectory
from pathlib import Path
import csv

from shaper import token_bucket, read_packets, write_trace
from composite_shaper import leaky_bucket
from source_homework2 import generate


class BoundaryTests(unittest.TestCase):
    def test_tbf_token_wait_and_fifo(self):
        packets = [(1, 0., 1500), (2, 0., 1500), (3, .5, 1000)]
        out, lost = token_bucket(packets, 1000, 2000, 3000)
        self.assertEqual([x[0] for x in out], [1, 2, 3])
        self.assertEqual([round(x[1], 8) for x in out], [0., 1., 2.])
        self.assertEqual(lost, [])

    def test_tbf_same_timestamp_fifo(self):
        packets = [(1, 0., 1000), (2, 0., 1000), (3, 0., 1000)]
        out, lost = token_bucket(packets, 1000, 1000, 2000)
        self.assertEqual([x[0] for x in out], [1, 2, 3])
        self.assertEqual([round(x[1], 8) for x in out], [0., 1., 2.])
        self.assertFalse(lost)

    def test_tbf_full_buffer_drops_and_accounts_bytes(self):
        packets = [(1, 0., 1000), (2, 0., 1000), (3, 0., 1000)]
        out, lost = token_bucket(packets, 1000, 1000, 1000)
        self.assertEqual([x[0] for x in out], [1, 2])
        self.assertEqual(lost, [3])

    def test_tbf_no_buffer_allows_immediate_packet(self):
        out, lost = token_bucket([(1, 0., 1000), (2, 0., 1000)], 1000, 1000, 0)
        self.assertEqual([x[0] for x in out], [1])
        self.assertEqual(lost, [2])

    def test_tbf_oversize_packet_is_dropped(self):
        out, lost = token_bucket([(1, 0., 1200), (2, 0., 500)], 1000, 1000, 10000)
        self.assertEqual(lost, [1])
        self.assertEqual([x[0] for x in out], [2])

    def test_tbf_exact_bucket_capacity(self):
        out, lost = token_bucket([(1, 0., 1262)], 500, 1262, 0)
        self.assertEqual(out, [(1, 0., 1262)])
        self.assertFalse(lost)

    def test_tbf_refill_during_idle_period(self):
        out, lost = token_bucket([(1, 0., 1000), (2, 5., 1000)], 1000, 1000, 0)
        self.assertEqual([x[1] for x in out], [0., 5.])
        self.assertFalse(lost)

    def test_lbf_nonpreemptive_and_fifo(self):
        out, lost = leaky_bucket([(1, 0., 1000), (2, 0., 1000), (3, .5, 1000)], 1000, 1000)
        self.assertEqual([x[0] for x in out], [1, 2])
        self.assertEqual([x[1] for x in out], [1., 2.])
        self.assertEqual(lost, [3])

    def test_lbf_zero_waiting_buffer(self):
        out, lost = leaky_bucket([(1, 0., 1000), (2, 0., 1000), (3, 1., 1000)], 1000, 0)
        self.assertEqual([x[0] for x in out], [1, 3])
        self.assertEqual([x[1] for x in out], [1., 2.])
        self.assertEqual(lost, [2])

    def test_lbf_completion_before_same_time_arrival(self):
        out, lost = leaky_bucket([(1, 0., 1000), (2, 0., 1000), (3, 1., 1000)], 1000, 1000)
        self.assertEqual([x[0] for x in out], [1, 2, 3])
        self.assertEqual([x[1] for x in out], [1., 2., 3.])
        self.assertFalse(lost)

    def test_lbf_length_over_mu_completion(self):
        out, lost = leaky_bucket([(1, 2., 500)], 2000, 0)
        self.assertEqual(out, [(1, 2.25, 500)])
        self.assertFalse(lost)

    def test_composite_conservation_and_timing(self):
        packets = [(1, 0., 1000), (2, 0., 1000), (3, 0., 1000), (4, 1., 1000)]
        mid, lost_tbf = token_bucket(packets, 1000, 1000, 1000)
        out, lost_lbf = leaky_bucket(mid, 1000, 1000)
        in_ids = {p[0] for p in packets}
        delivered = {p[0] for p in out}
        dropped = set(lost_tbf) | set(lost_lbf)
        self.assertFalse(delivered & dropped)
        self.assertEqual(in_ids, delivered | dropped)
        self.assertEqual(len(out) + len(lost_tbf) + len(lost_lbf), len(packets))
        generated = {pid: t for pid, t, _ in packets}
        self.assertTrue(all(t >= generated[pid] for pid, t, _ in out))
        self.assertEqual([x[1] for x in out], sorted(x[1] for x in out))

    def test_invalid_parameters(self):
        for args in [(0, 1000, 1000), (1000, 0, 1000), (1000, 1000, -1)]:
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    token_bucket([], *args)
        for args in [(0, 1000), (1000, -1)]:
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    leaky_bucket([], *args)

    def test_trace_roundtrip_and_order_validation(self):
        with TemporaryDirectory() as td:
            path = Path(td) / 'trace.txt'
            original = [(1, 0., 1262), (2, .125, 500)]
            write_trace(path, original)
            self.assertEqual(read_packets(path), original)
            path.write_text('1,1.0,100\n2,0.0,100\n')
            with self.assertRaises(ValueError):
                read_packets(path)

    def test_source_batch_timestamps_and_unique_ids(self):
        with TemporaryDirectory() as td:
            csvpath = Path(td) / 'sizes.csv'
            with csvpath.open('w', newline='') as f:
                w = csv.writer(f)
                w.writerow(['Length'])
                w.writerows([[500], [1000], [1262]])
            trace = Path(td) / 'generated.txt'
            n, duration = generate(csvpath, trace, 100, 42)
            packets = read_packets(trace)
            self.assertEqual(len(packets), n)
            self.assertEqual([p[0] for p in packets], list(range(1, n + 1)))
            timestamps = [p[1] for p in packets]
            self.assertEqual(len(set(timestamps)), 100)
            self.assertGreaterEqual(duration, 0.)
            self.assertTrue(all(p[2] in (500, 1000, 1262) for p in packets))


if __name__ == '__main__':
    unittest.main(verbosity=2)
