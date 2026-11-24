"""Homework 2: one-at-a-time sensitivity experiments on the existing input trace.
Run: python3 sensitivity_analysis.py
Outputs: sensitivity_results.csv and sensitivity_delay_loss.png.
Does not overwrite Input_Traffic_Trace.txt or Output_Traffic_Trace.txt.
"""
import csv
import math
from statistics import mean
import matplotlib.pyplot as plt
from shaper import read_packets, token_bucket
from composite_shaper import leaky_bucket

BASE = {'rho': 1_000_000, 'bucket': 5000, 'Bi': 100_000, 'mu': 1_000_000, 'Bo': 100_000}
SWEEPS = {
    'rho': [200_000, 300_000, 350_000, 500_000, 1_000_000],
    'bucket': [1500, 2500, 5000, 10000, 20000],
    'Bi': [0, 1500, 5000, 20000, 100000],
    'mu': [200_000, 300_000, 350_000, 500_000, 1_000_000],
    'Bo': [0, 1500, 5000, 20000, 100000],
}

def percentile(values, p):
    if not values:
        return float('nan')
    values = sorted(values)
    pos = (len(values)-1)*p/100
    lo = math.floor(pos)
    hi = math.ceil(pos)
    return values[lo] + (values[hi]-values[lo])*(pos-lo)

def run(source, params):
    tbf, lost_tbf = token_bucket(source, params['rho'], params['bucket'], params['Bi'])
    output, lost_lbf = leaky_bucket(tbf, params['mu'], params['Bo'])
    source_times = {pid: t for pid, t, length in source}
    delays = [(t-source_times[pid])*1000 for pid, t, length in output]
    loss = 100*(len(lost_tbf)+len(lost_lbf))/len(source)
    duration = output[-1][1]-source[0][1] if output else float('nan')
    throughput = 8*sum(length for _, _, length in output)/duration/1e6 if duration > 0 else float('nan')
    return dict(delivered=len(output), tbf_dropped=len(lost_tbf), lbf_dropped=len(lost_lbf),
                loss_percent=loss, mean_delay_ms=mean(delays) if delays else float('nan'),
                p95_delay_ms=percentile(delays, 95), throughput_mbps=throughput)

def main():
    source = read_packets('Input_Traffic_Trace.txt')
    maximum_packet = max(length for _, _, length in source)
    print(f'Input packets: {len(source)}; maximum packet size: {maximum_packet} bytes')
    rows=[]
    for param, values in SWEEPS.items():
        print(f'\nChanging {param} (all other parameters fixed):')
        for value in values:
            config=BASE.copy()
            config[param]=value
            if config['bucket'] < maximum_packet:
                print(f'  {value}: skipped (bucket smaller than maximum packet)')
                continue
            result=run(source, config)
            row={'parameter':param,'value':value,**result}
            rows.append(row)
            print(f"  {value:>9}: delay={result['mean_delay_ms']:>9.3f} ms, loss={result['loss_percent']:>7.3f}%, throughput={result['throughput_mbps']:.3f} Mbit/s")
    with open('sensitivity_results.csv','w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    fig, axes=plt.subplots(2, 5, figsize=(17, 7))
    for col, param in enumerate(SWEEPS):
        subset=[r for r in rows if r['parameter']==param]
        xs=[r['value'] for r in subset]
        for row_index, (field, label) in enumerate([('mean_delay_ms','Mean delay (ms)'),('loss_percent','Loss (%)')]):
            ax=axes[row_index,col]
            ax.plot(xs,[r[field] for r in subset],marker='o')
            ax.set_title(f'{param}: {label}')
            ax.set_xlabel(param)
            ax.grid(alpha=.25)
            ax.ticklabel_format(axis='x',style='sci',scilimits=(0,0))
    fig.tight_layout()
    fig.savefig('sensitivity_delay_loss.png',dpi=170)
    plt.close(fig)
    print('\nSaved: sensitivity_results.csv and sensitivity_delay_loss.png')
    print('Note: This is a single-trace exploratory sweep, not yet a replicated optimization study.')

if __name__=='__main__':
    main()
