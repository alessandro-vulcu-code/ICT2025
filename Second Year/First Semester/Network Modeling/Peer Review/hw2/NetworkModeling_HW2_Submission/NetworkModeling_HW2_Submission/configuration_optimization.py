"""Compare composite TBF/LBF configurations using paired synthetic traffic runs.
Run: python3 configuration_optimization.py
Optional: --repetitions 10 --batches 31339
Outputs: optimization_runs.csv, optimization_summary.csv
Does not overwrite the original Input/Output traffic traces.
"""
import argparse
import csv
import math
import statistics
import tempfile
from pathlib import Path
from source_homework2 import generate
from shaper import read_packets, token_bucket
from composite_shaper import leaky_bucket
from statistical_experiments import metrics, T95

CONFIGS = {
    'Baseline': {'rho': 1_000_000, 'bucket': 5000, 'Bi': 100_000, 'mu': 1_000_000, 'Bo': 100_000},
    'Balanced': {'rho': 500_000, 'bucket': 1500, 'Bi': 20_000, 'mu': 500_000, 'Bo': 5000},
    'Aggressive': {'rho': 400_000, 'bucket': 1500, 'Bi': 5000, 'mu': 400_000, 'Bo': 1500},
}
LIMITS = {'mean_delay_ms': 20, 'p95_delay_ms': 50, 'jitter_ms': 10, 'loss_percent': 1}
FIELDS = ['mean_delay_ms','p95_delay_ms','p99_delay_ms','jitter_ms','loss_percent','throughput_mbps']

def ci(values):
    if len(values) < 2 or not all(math.isfinite(v) for v in values):
        return float('nan'), float('nan')
    return statistics.mean(values), T95[len(values)-1] * statistics.stdev(values) / math.sqrt(len(values))

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--csv', default='google-meet-incoming.csv')
    p.add_argument('--repetitions', type=int, default=10)
    p.add_argument('--batches', type=int, default=31339)
    p.add_argument('--seed', type=int, default=42)
    args = p.parse_args()
    if not 2 <= args.repetitions <= 31: p.error('--repetitions must be between 2 and 31')
    if args.batches < 1: p.error('--batches must be positive')
    runs = []
    with tempfile.TemporaryDirectory() as folder:
        path = str(Path(folder) / 'temporary_trace.txt')
        for index in range(args.repetitions):
            seed = args.seed + index
            generate(args.csv, path, args.batches, seed)
            source = read_packets(path)
            max_packet = max(length for _, _, length in source)
            print(f'\nSeed {seed}: {len(source)} packets, max packet {max_packet} bytes')
            for name, config in CONFIGS.items():
                if config['bucket'] < max_packet:
                    raise ValueError(f'{name}: bucket smaller than max packet ({max_packet})')
                tbf, dropped_tbf = token_bucket(source, config['rho'], config['bucket'], config['Bi'])
                output, dropped_lbf = leaky_bucket(tbf, config['mu'], config['Bo'])
                if len(output) + len(dropped_tbf) + len(dropped_lbf) != len(source):
                    raise AssertionError('Packet accounting failed')
                m = metrics(source, output)
                row = {'configuration': name, 'seed': seed, **config, **m,
                       'tbf_dropped': len(dropped_tbf), 'lbf_dropped': len(dropped_lbf)}
                runs.append(row)
                print(f"  {name:10s} mean={m['mean_delay_ms']:8.3f} ms  "
                      f"P95={m['p95_delay_ms']:8.3f} ms  "
                      f"jitter={m['jitter_ms']:7.3f} ms  loss={m['loss_percent']:7.3f}%")

    with open('optimization_runs.csv','w',newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(runs[0]))
        writer.writeheader(); writer.writerows(runs)

    summaries = []
    print('\n=== Averages and 95% CI across independent seeds ===')
    for name, config in CONFIGS.items():
        subset = [r for r in runs if r['configuration'] == name]
        summary = {'configuration': name, **config}
        for field in FIELDS:
            avg, half = ci([r[field] for r in subset])
            summary[field] = avg
            summary[field + '_ci95_halfwidth'] = half
        # Conservative screening: upper endpoint of each estimated CI must meet its threshold.
        # This is a screening heuristic, not a formal joint 95% guarantee.
        meets = all(math.isfinite(summary[k]) and
                    summary[k] + summary[k+'_ci95_halfwidth'] <= bound
                    for k, bound in LIMITS.items())
        summary['passes_ci_upper_screen'] = meets
        summary['total_buffer_bytes'] = config['Bi'] + config['Bo']
        summaries.append(summary)
        print(f'\n{name}:')
        for field in FIELDS:
            print(f"  {field}: {summary[field]:.4f} +/- {summary[field+'_ci95_halfwidth']:.4f}")
        print(f"  CI-upper QoS screen: {'PASS' if meets else 'FAIL'}")
        print(f"  Allocated buffers (Bi+Bo): {summary['total_buffer_bytes']} bytes")

    with open('optimization_summary.csv','w',newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(summaries[0]))
        writer.writeheader(); writer.writerows(summaries)
    print('\nSaved: optimization_runs.csv and optimization_summary.csv')
    print('Note: These are only three candidate configurations; no global optimum is claimed.')

if __name__ == '__main__':
    main()
