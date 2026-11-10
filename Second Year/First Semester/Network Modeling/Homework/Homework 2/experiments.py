"""Reproducible parameter search, independent confirmation, and report figures."""
import argparse
from collections import Counter
from dataclasses import asdict
import csv
import itertools
import json
import os
from pathlib import Path
import shutil
os.environ.setdefault('MPLCONFIGDIR', '/tmp/tokenbucket-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t as student_t
from source import ROOT, fit_cycles, generate, write_trace, read_trace
from shaper import Config, simulate

OUT = ROOT / 'analysis'
TARGETS = dict(loss_pct=1.0, mean_ms=30.0, p95_ms=50.0, p99_ms=100.0,
               jitter95_ms=30.0)


def metrics(trace, result, duration):
    original = {p[0]: p for p in trace}
    delays = np.array([p[1]-original[p[0]][1] for p in result.output])
    input_bytes = sum(p[2] for p in trace)
    output_bytes = sum(p[2] for p in result.output)
    fixed_bytes = sum(p[2] for p in result.output if p[1] < duration)
    return dict(packets=len(trace), loss_pct=100*len(result.drops)/len(trace),
                byte_delivery_pct=100*output_bytes/input_bytes,
                offered_kbps=8*input_bytes/duration/1000,
                throughput_kbps=8*fixed_bytes/duration/1000,
                mean_ms=float(np.mean(delays)*1000) if len(delays) else float('inf'),
                p95_ms=float(np.quantile(delays, .95)*1000) if len(delays) else float('inf'),
                p99_ms=float(np.quantile(delays, .99)*1000) if len(delays) else float('inf'),
                jitter95_ms=float(np.quantile(np.abs(np.diff(delays)), .95)*1000)
                if len(delays) > 1 else float('inf'),
                drain_s=max(0, result.output[-1][1]-duration) if result.output else 0,
                peak_bi=result.peak_bi, peak_bo=result.peak_bo,
                drop_reasons=dict(Counter(p[3] for p in result.drops)))


def feasible(m):
    return all(m[k] <= bound for k, bound in TARGETS.items()) and m['byte_delivery_pct'] >= 99


def cost(c):
    # Equal weight for each rate reservation and total storage, with stated scales.
    return c.rho/100000 + c.mu/100000 + (c.b+c.bi+c.bo)/16384


def save_csv(path, rows):
    with open(path, 'w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--search-duration', type=float, default=300)
    parser.add_argument('--duration', type=float, default=1800)
    parser.add_argument('--replications', type=int, default=10)
    args = parser.parse_args()
    if args.replications < 2:
        parser.error('At least two replications required')
    OUT.mkdir(exist_ok=True)
    cycles = fit_cycles()
    search_trace = generate(cycles, args.search_duration, 2026)
    rows = []
    grid = itertools.product([110000, 140000, 180000, 220000], [1341, 4096, 8192, 16384],
                             [4096, 16384], [120000, 220000, 300000], [4096, 16384])
    for values in grid:
        c = Config(*values)
        m = metrics(search_trace, simulate(search_trace, c), args.search_duration)
        rows.append(dict(**asdict(c), cost=cost(c), feasible=feasible(m),
                         **{k:v for k,v in m.items() if k != 'drop_reasons'}))
    save_csv(OUT / 'parameter_search.csv', rows)
    candidates = sorted((r for r in rows if r['feasible']), key=lambda r:r['cost'])
    if not candidates:
        raise RuntimeError('No feasible search configuration; inspect parameter_search.csv')
    selected = Config(**{k:candidates[0][k] for k in asdict(Config())})
    print(f'Search: {len(rows)} configurations; {len(candidates)} feasible; selected {selected}', flush=True)
    # Independent seeds never used to select the candidate.
    confirmations = []
    representative = None
    for seed in range(3026, 3026+args.replications):
        trace = generate(cycles, args.duration, seed)
        result = simulate(trace, selected, record=seed == 3026)
        m = metrics(trace, result, args.duration)
        confirmations.append(dict(seed=seed, **m))
        if seed == 3026:
            representative = trace, result
            write_trace(ROOT / 'Input_Traffic_Trace.txt', trace)
            write_trace(ROOT / 'Output_Traffic_Trace.txt', result.output)
            # Assignment uses both naming conventions; aliases contain identical data.
            shutil.copyfile(ROOT / 'Input_Traffic_Trace.txt', ROOT / 'Input_Trace_File.txt')
            shutil.copyfile(ROOT / 'Output_Traffic_Trace.txt', ROOT / 'Output_Trace_File.txt')
            save_csv(OUT / 'drops.csv', [dict(id=p[0], time_s=p[1], bytes=p[2], reason=p[3])
                                      for p in result.drops] or
                     [dict(id='', time_s='', bytes='', reason='')])
        print(f'Confirmation {seed}: loss {m["loss_pct"]:.3f}%, p95 {m["p95_ms"]:.2f} ms', flush=True)
    ci = {}
    for key in list(TARGETS) + ['byte_delivery_pct', 'offered_kbps', 'throughput_kbps']:
        values = np.array([r[key] for r in confirmations])
        half = float(student_t.ppf(.975, len(values)-1)*values.std(ddof=1)/np.sqrt(len(values)))
        ci[key] = dict(mean=float(values.mean()), half95=half,
                       minimum=float(values.min()), maximum=float(values.max()))
    trace, result = representative
    checks = {}
    for name, packets, duration in [
            ('homework1_offsets', generate(cycles, args.duration, 3026, False), args.duration),
            ('held_out_capture', [(i+1,float(t),int(l)) for i,(t,l) in enumerate(
                np.loadtxt(ROOT/'data/zoom_validation_120s.csv',
                           delimiter=',', skiprows=1))], 120)]:
        checks[name] = metrics(packets, simulate(packets, selected), duration)
    controls = {}
    for name, config in [('underprovisioned', Config(90000, 1341, 4096, 100000, 4096)),
                         ('large_buffers', Config(110000, 8192, 65536, 120000, 65536))]:
        controls[name] = dict(config=asdict(config), metrics=metrics(trace, simulate(trace,config),args.duration))
    summary = dict(search_duration_s=args.search_duration, duration_s=args.duration,
                   replications=args.replications, search_seed=2026,
                   configuration_count=len(rows), feasible_count=len(candidates),
                   selected=asdict(selected), selected_cost=cost(selected), targets=TARGETS,
                   ci95=ci, replications_results=confirmations, robustness=checks, controls=controls,
                   all_confirmation_runs_pass=all(feasible(m) for m in confirmations))
    (OUT/'results.json').write_text(json.dumps(summary, indent=2)+'\n')
    (ROOT/'selected_config.json').write_text(json.dumps(asdict(selected), indent=2)+'\n')
    save_csv(OUT/'replications.csv', [{k:v for k,v in r.items() if k != 'drop_reasons'} for r in confirmations])
    save_csv(OUT/'buffer_trace.csv', [dict(time_s=r[0], input_B=r[1], output_B=r[2], tokens=r[3])
                                   for r in result.occupancy])
    plot(rows, selected, trace, result, args.duration)
    if not summary['all_confirmation_runs_pass']:
        raise RuntimeError('Selected candidate failed independent confirmation; review search')


def plot(rows, selected, trace, result, duration):
    plt.rcParams.update({'font.size':8, 'axes.spines.top':False, 'axes.spines.right':False,
                         'pdf.fonttype':42})
    fig, axes = plt.subplots(1, 3, figsize=(7.1, 2.0), layout='constrained')
    for ok, color, label in [(False, '#bdbdbd', 'Fails QoS'), (True, '#287b9a', 'Meets QoS')]:
        r = [r for r in rows if r['feasible'] == ok]
        axes[0].scatter([r['cost'] for r in r], [r['p95_ms'] for r in r], s=10, c=color, label=label)
    chosen = next(r for r in rows if all(r[k] == v for k,v in asdict(selected).items()))
    axes[0].scatter([cost(selected)], [chosen['p95_ms']], marker='*', s=80, color='#cb542d')
    axes[0].axhline(50, lw=.7, ls='--', color='black')
    axes[0].set(xlabel='Normalized resource cost', ylabel='95th delay percentile (ms)', title='(a) 300 s parameter search')
    axes[0].legend(fontsize=6, frameon=False)
    original = {p[0]:p[1] for p in trace}
    delays = np.sort([(p[1]-original[p[0]])*1000 for p in result.output])
    axes[1].plot(delays, np.arange(1,len(delays)+1)/len(delays), color='#287b9a')
    axes[1].set(xlabel='Packet delay (ms)', ylabel='CDF', title='(b) Selected: seed 3026', xlim=(0, max(100,np.quantile(delays,.999))))
    edges = np.arange(0,10.0001,.1)
    for packets,label,color in [(trace,'Input','#999999'),(result.output,'Output','#287b9a')]:
        ts = np.array([p[1] for p in packets]); ls=np.array([p[2] for p in packets])
        rate = np.histogram(ts,bins=edges,weights=ls)[0]*8/.1/1000
        axes[2].stairs(rate,edges,label=label,color=color,lw=.8)
    axes[2].set(xlabel='Time (s)',ylabel='Rate (kbit/s)',title='(c) First 10 s, 100 ms bins')
    axes[2].legend(fontsize=6,frameon=False)
    for ax in axes:
        ax.grid(alpha=.2)
    fig.savefig(OUT/'results.pdf')
    fig.savefig(OUT/'results.png',dpi=180)
    plt.close(fig)


if __name__ == '__main__':
    main()
