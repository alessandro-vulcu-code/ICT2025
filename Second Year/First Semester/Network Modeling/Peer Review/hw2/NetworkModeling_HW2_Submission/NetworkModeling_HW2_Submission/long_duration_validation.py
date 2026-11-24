"""HW2 long-duration independent-seed validation.
Run: python3 long_duration_validation.py
Optional: --batches 125000 --repetitions 5 --seed 100
Outputs long_validation_runs.csv and long_validation_summary.csv.
Does not overwrite Input_Traffic_Trace.txt or Output_Traffic_Trace.txt.
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
    'Baseline': dict(rho=1000000, bucket=5000, Bi=100000, mu=1000000, Bo=100000),
    'C13': dict(rho=750000, bucket=1500, Bi=20000, mu=750000, Bo=5000),
    'C08': dict(rho=600000, bucket=1500, Bi=40000, mu=600000, Bo=5000),
}
LIMITS = {'mean_delay_ms':20, 'p95_delay_ms':50, 'jitter_ms':10, 'loss_percent':1}
KPI = ['duration_s', 'mean_delay_ms', 'p95_delay_ms', 'p99_delay_ms', 'jitter_ms', 'loss_percent', 'throughput_mbps']

def write_csv(name, rows):
    with open(name, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--csv', default='google-meet-incoming.csv')
    p.add_argument('--batches', type=int, default=125000)
    p.add_argument('--repetitions', type=int, default=5)
    p.add_argument('--seed', type=int, default=100)
    a=p.parse_args()
    if a.batches < 1: p.error('batches must be positive')
    if not 2 <= a.repetitions <= 31: p.error('repetitions must be between 2 and 31')
    runs=[]
    with tempfile.TemporaryDirectory() as folder:
        path=str(Path(folder)/'input.csv')
        for j in range(a.repetitions):
            seed=a.seed+j
            generate(a.csv,path,a.batches,seed)
            source=read_packets(path)
            duration=source[-1][1]-source[0][1]
            print(f'Seed {seed}: {len(source)} packets, {duration/60:.2f} min generated traffic', flush=True)
            for name, c in CONFIGS.items():
                if max(length for _,_,length in source)>c['bucket']:
                    raise ValueError(f'{name}: bucket smaller than maximum packet')
                tbf,drop1=token_bucket(source,c['rho'],c['bucket'],c['Bi'])
                output,drop2=leaky_bucket(tbf,c['mu'],c['Bo'])
                assert len(source)==len(output)+len(drop1)+len(drop2)
                m=metrics(source,output)
                runs.append(dict(config=name,seed=seed,**c,**m,tbf_dropped=len(drop1),lbf_dropped=len(drop2)))
                print(f"  {name:8s} delay={m['mean_delay_ms']:7.3f}ms P95={m['p95_delay_ms']:7.3f}ms loss={m['loss_percent']:6.3f}%",flush=True)
    write_csv('long_validation_runs.csv',runs)
    summaries=[]
    print('\n=== Long-run means and 95% confidence intervals ===')
    for name,c in CONFIGS.items():
        subset=[r for r in runs if r['config']==name]
        row=dict(config=name,**c,buffer_bytes=c['Bi']+c['Bo'])
        for key in KPI:
            vals=[r[key] for r in subset]
            if all(math.isfinite(v) for v in vals):
                avg=statistics.mean(vals)
                half=T95[len(vals)-1]*statistics.stdev(vals)/math.sqrt(len(vals))
            else:
                avg=half=float('nan')
            row[key+'_mean']=avg
            row[key+'_ci_halfwidth']=half
        row['ci_upper_pass']=all(math.isfinite(row[k+'_mean']+row[k+'_ci_halfwidth']) and row[k+'_mean']+row[k+'_ci_halfwidth'] <= limit for k,limit in LIMITS.items())
        summaries.append(row)
        print(f"{name:8s} delay={row['mean_delay_ms_mean']:.3f} ± {row['mean_delay_ms_ci_halfwidth']:.3f}ms, "
              f"loss={row['loss_percent_mean']:.3f} ± {row['loss_percent_ci_halfwidth']:.3f}%, "
              f"CI-upper QoS={'PASS' if row['ci_upper_pass'] else 'FAIL'}")
    write_csv('long_validation_summary.csv',summaries)
    print('\nSaved: long_validation_runs.csv and long_validation_summary.csv')
    print('Note: Confidence intervals summarize run-to-run uncertainty; they are not guarantees for every future call.')

if __name__=='__main__': main()
