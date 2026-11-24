"""Two-stage, QoS-constrained parameter search for Network Modeling HW2.
Run: python3 parameter_search.py
Optional: --repetitions 10 --batches 31339 --seed 42
Outputs: search_screen.csv, search_validation.csv, search_summary.csv.
Existing Input/Output traces are not modified.
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

LIMITS = {'mean_delay_ms': 20, 'p95_delay_ms': 50,
          'jitter_ms': 10, 'loss_percent': 1}
METRICS = ['mean_delay_ms','p95_delay_ms','p99_delay_ms',
           'jitter_ms','loss_percent','throughput_mbps']

# Focused search around the previously observed viable region.
# Rates are bytes/s; token rate is tokens/s with 1 token = 1 byte.
CANDIDATES = [
    {'rho': rho, 'bucket': 1500, 'Bi': bi, 'mu': mu, 'Bo': bo}
    for rho, mu in [(500000,500000),(600000,600000),(750000,750000),
                    (600000,750000),(750000,600000)]
    for bi, bo in [(20000,5000),(40000,5000),(60000,5000),
                   (20000,10000),(40000,10000),(60000,10000)]
]
BASELINE = {'rho':1000000,'bucket':5000,'Bi':100000,'mu':1000000,'Bo':100000}

def run(source, config):
    if config['bucket'] < max(length for _,_,length in source):
        raise ValueError('Token bucket smaller than maximum packet')
    tbf, drop1 = token_bucket(source, config['rho'], config['bucket'], config['Bi'])
    output, drop2 = leaky_bucket(tbf, config['mu'], config['Bo'])
    assert len(source) == len(output) + len(drop1) + len(drop2), 'Packet accounting mismatch'
    return {**metrics(source, output), 'tbf_dropped':len(drop1), 'lbf_dropped':len(drop2)}

def passing(row):
    return all(math.isfinite(row[k]) and row[k] <= v for k,v in LIMITS.items())

def write_csv(path, rows):
    if not rows: return
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--csv', default='google-meet-incoming.csv')
    parser.add_argument('--batches', type=int, default=31339)
    parser.add_argument('--repetitions', type=int, default=10)
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()
    if not 2 <= args.repetitions <= 31: parser.error('repetitions must be 2..31')
    if args.batches < 1: parser.error('batches must be positive')

    with tempfile.TemporaryDirectory() as folder:
        trace = str(Path(folder)/'source.txt')
        generate(args.csv, trace, args.batches, args.seed)
        source = read_packets(trace)
        print(f'Screening {len(CANDIDATES)} candidates on seed {args.seed}, {len(source)} packets...')
        screening = []
        for i, c in enumerate(CANDIDATES, 1):
            result = run(source, c)
            screening.append({'candidate':f'C{i:02d}', **c, **result,
                              'passes_single_seed':passing(result),
                              'buffer_bytes':c['Bi']+c['Bo']})
            if i % 5 == 0: print(f'  Screened {i}/{len(CANDIDATES)}')
        write_csv('search_screen.csv', screening)
        viable = [r for r in screening if r['passes_single_seed']]
        viable.sort(key=lambda r:(r['buffer_bytes'], r['rho']+r['mu'],
                                  r['loss_percent'], r['mean_delay_ms']))
        print(f'Single-seed pass: {len(viable)}/{len(screening)}')
        # Validate up to 3 economical candidates, plus baseline as reference.
        selected = [{'candidate':'Baseline', **BASELINE}]
        selected += [{k:r[k] for k in ['candidate','rho','bucket','Bi','mu','Bo']}
                     for r in viable[:3]]
        if len(selected) == 1:
            print('No candidate passed screening; baseline only. Broaden search ranges.')
        print('Validating:', ', '.join(r['candidate'] for r in selected))
        runs = []
        for j in range(args.repetitions):
            seed = args.seed + j
            if j:  # seed 0 already generated
                generate(args.csv, trace, args.batches, seed)
                source = read_packets(trace)
            for c in selected:
                m = run(source, c)
                runs.append({'candidate':c['candidate'],'seed':seed,
                             **{k:c[k] for k in ['rho','bucket','Bi','mu','Bo']}, **m})
            print(f'  Validated seed {seed} ({j+1}/{args.repetitions})')
    write_csv('search_validation.csv', runs)
    summaries = []
    for c in selected:
        sub = [r for r in runs if r['candidate']==c['candidate']]
        summary = {k:c[k] for k in ['candidate','rho','bucket','Bi','mu','Bo']}
        for k in METRICS:
            vals = [r[k] for r in sub]
            summary[k] = statistics.mean(vals)
            summary[k+'_ci95_halfwidth'] = (T95[len(vals)-1] * statistics.stdev(vals)
                                            / math.sqrt(len(vals)))
        summary['passes_ci_upper_screen'] = all(
            summary[k]+summary[k+'_ci95_halfwidth'] <= limit
            for k,limit in LIMITS.items())
        summary['buffer_bytes'] = c['Bi']+c['Bo']
        summaries.append(summary)
    write_csv('search_summary.csv', summaries)
    print('\n=== Validated results (mean across seeds) ===')
    for r in summaries:
        print(f"{r['candidate']:9s} rho={r['rho']:7d} mu={r['mu']:7d} "
              f"Bi={r['Bi']:6d} Bo={r['Bo']:5d} "
              f"delay={r['mean_delay_ms']:7.3f}ms "
              f"P95={r['p95_delay_ms']:7.3f}ms "
              f"loss={r['loss_percent']:6.3f}% "
              f"CI-upper={'PASS' if r['passes_ci_upper_screen'] else 'FAIL'}")
    print('\nSaved: search_screen.csv, search_validation.csv, search_summary.csv')
    print('This is a limited candidate search, NOT a global optimum.')
    print('Longer independent simulations and boundary tests are still needed.')

if __name__ == '__main__': main()
