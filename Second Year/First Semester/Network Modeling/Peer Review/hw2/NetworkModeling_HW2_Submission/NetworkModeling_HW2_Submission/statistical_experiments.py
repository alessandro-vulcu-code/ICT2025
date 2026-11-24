"""Homework 2: independent-seed baseline replications and 95% t confidence intervals.
Run in the same folder as source_homework2.py, shaper.py, composite_shaper.py.
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
from qos_analysis import percentile

# Two-sided 95% Student t critical values, degrees of freedom 1..30.
T95 = {1:12.706,2:4.303,3:3.182,4:2.776,5:2.571,6:2.447,7:2.365,8:2.306,9:2.262,10:2.228,11:2.201,12:2.179,13:2.160,14:2.145,15:2.131,16:2.120,17:2.110,18:2.101,19:2.093,20:2.086,21:2.080,22:2.074,23:2.069,24:2.064,25:2.060,26:2.056,27:2.052,28:2.048,29:2.045,30:2.042}

def metrics(source, output):
    by_id = {pid:(time,length) for pid,time,length in source}
    out = {pid:time for pid,time,length in output}
    ids = [pid for pid,_,_ in source if pid in out]
    delays = [out[pid]-by_id[pid][0] for pid in ids]
    jitter = statistics.mean(abs(b-a) for a,b in zip(delays,delays[1:])) if len(delays)>1 else float('nan')
    duration = output[-1][1]-source[0][1] if output else float('nan')
    return {'packets':len(source),'duration_s':source[-1][1]-source[0][1],
            'mean_delay_ms':statistics.mean(delays)*1000 if delays else float('nan'),
            'p95_delay_ms':percentile(delays,95)*1000,
            'p99_delay_ms':percentile(delays,99)*1000,
            'jitter_ms':jitter*1000,
            'loss_percent':100*(len(source)-len(output))/len(source),
            'throughput_mbps':8*sum(length for _,_,length in output)/duration/1e6 if output and duration>0 else float('nan')}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--csv',default='google-meet-incoming.csv')
    p.add_argument('--repetitions',type=int,default=10)
    p.add_argument('--batches',type=int,default=31339)
    p.add_argument('--rho',type=float,default=1000000)
    p.add_argument('--bucket',type=int,default=5000)
    p.add_argument('--input-buffer',type=int,default=100000)
    p.add_argument('--mu',type=float,default=1000000)
    p.add_argument('--output-buffer',type=int,default=100000)
    p.add_argument('--output',default='statistical_results.csv')
    a=p.parse_args()
    if not 2<=a.repetitions<=31: p.error('repetitions must be 2..31')
    rows=[]
    with tempfile.TemporaryDirectory() as folder:
        temp=Path(folder)/'input.txt'
        for i in range(a.repetitions):
            seed=42+i
            generate(a.csv,str(temp),a.batches,seed)
            source=read_packets(str(temp))
            tbf,drop1=token_bucket(source,a.rho,a.bucket,a.input_buffer)
            output,drop2=leaky_bucket(tbf,a.mu,a.output_buffer)
            m=metrics(source,output)
            m={'seed':seed,**m,'tbf_dropped':len(drop1),'lbf_dropped':len(drop2)}
            rows.append(m)
            print(f"Seed {seed}: {m['packets']} packets; mean delay {m['mean_delay_ms']:.3f} ms; loss {m['loss_percent']:.3f}%")
    with open(a.output,'w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)
    print('\nMean and 95% CI across independent runs:')
    for k in ['duration_s','mean_delay_ms','p95_delay_ms','p99_delay_ms','jitter_ms','loss_percent','throughput_mbps']:
        values=[r[k] for r in rows]
        if any(not math.isfinite(x) for x in values):
            print(f'{k}: N/A');continue
        avg=statistics.mean(values)
        half=T95[len(values)-1]*statistics.stdev(values)/math.sqrt(len(values))
        print(f'{k}: {avg:.4f} ± {half:.4f} (95% CI)')
    print(f'\nSaved: {a.output}')

if __name__=='__main__':main()
