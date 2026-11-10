"""Hand-computed queue cases and end-to-end conservation/envelope checks."""
import math
import tempfile
import unittest
from pathlib import Path
from source import fit_cycles, generate, read_trace, write_trace
from shaper import Config, simulate


class ShaperTests(unittest.TestCase):
    def test_token_wait_and_serialization(self):
        result = simulate([(1, 0, 100), (2, 0, 100), (3, 0, 100)],
                          Config(100, 100, 200, 200, 0), True)
        self.assertEqual(result.output, [(1, .5, 100), (2, 1.5, 100), (3, 2.5, 100)])
        self.assertFalse(result.drops)

    def test_both_overflows(self):
        trace = [(i, 0, 100) for i in range(1, 6)]
        result = simulate(trace, Config(100, 200, 100, 10, 0))
        self.assertEqual([r[0] for r in result.output], [1])
        self.assertEqual([r[3] for r in result.drops].count('input_overflow'), 2)
        self.assertEqual([r[3] for r in result.drops].count('output_overflow'), 2)

    def test_service_excluded_and_completion_first(self):
        result = simulate([(1, 0, 100), (2, 0, 100), (3, 0, 100), (4, 1, 100)],
                          Config(1000, 1000, 0, 100, 100))
        self.assertEqual(result.output, [(1, 1, 100), (2, 2, 100), (4, 3, 100)])
        self.assertEqual(result.drops[0][0], 3)

    def test_oversize_and_fifo(self):
        result = simulate([(1, 0, 101), (2, 0, 100), (3, 0, 90), (4, .1, 10)],
                          Config(100, 100, 100, 1000, 100), True)
        self.assertEqual(result.drops[0][3], 'larger_than_bucket')
        self.assertEqual([r[0] for r in result.output], [2, 3, 4])
        self.assertAlmostEqual(result.releases[1][1], .9)
        self.assertAlmostEqual(result.releases[2][1], 1)

    def test_empty_and_bad_parameters(self):
        self.assertEqual(simulate([], Config()).output, [])
        for args in [dict(rho=0), dict(mu=math.inf), dict(b=-1), dict(bo=1.5)]:
            with self.assertRaises(ValueError):
                Config(**args)

    def test_trace_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'trace.txt'
            for text in ['1 -0.1 10', '1 nan 10', '1 0 0', '1 0 10\n1 1 10',
                         '1 1 10\n2 0 10']:
                path.write_text(text)
                with self.assertRaises(ValueError):
                    read_trace(path)

    def test_source_reuses_homework1_exactly(self):
        cycles = fit_cycles()
        self.assertEqual(len(cycles), 7233)
        trace = generate(cycles, 120, 2026, simultaneous=False)
        self.assertEqual(len(trace), 13102)
        self.assertEqual(sum(p[2] for p in trace), 12975909)
        simultaneous = generate(cycles, 1, 2026, True)
        self.assertTrue(any(a[1] == b[1] for a, b in zip(simultaneous, simultaneous[1:])))

    def test_random_trace_invariants(self):
        trace = generate(fit_cycles(), 10, 77)
        c = Config(90000, 4096, 4096, 120000, 4096)
        result = simulate(trace, c, True)
        source = {p[0]: p for p in trace}
        ids = [p[0] for p in result.output] + [p[0] for p in result.drops]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), set(source))
        self.assertLessEqual(result.peak_bi, c.bi)
        self.assertLessEqual(result.peak_bo, c.bo)
        for i, packet in enumerate(result.output):
            self.assertGreaterEqual(packet[1] - source[packet[0]][1] + 1e-9, packet[2]/c.mu)
            if i:
                self.assertGreaterEqual(packet[1]-result.output[i-1][1]+1e-9, packet[2]/c.mu)
        # Every release interval must obey the packetized TBF envelope.
        releases = result.releases
        for i in range(len(releases)):
            total = 0
            for j in range(i, min(i+100, len(releases))):
                total += releases[j][2]
                self.assertLessEqual(total, c.b+c.rho*(releases[j][1]-releases[i][1])+1e-5)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'trace.txt'
            write_trace(path, result.output)
            self.assertEqual([p[0] for p in read_trace(path)], [p[0] for p in result.output])


if __name__ == '__main__':
    unittest.main()
