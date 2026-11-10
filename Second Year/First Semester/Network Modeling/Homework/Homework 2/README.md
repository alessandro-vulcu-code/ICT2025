# Homework 2: Zoom source and composite traffic shaper

Completed implementation of `Homework-TokenBucket-v3.pdf`, based on Homework 1's
empirical batch-renewal Zoom video model. The original Homework 1 files are unchanged.

## Deliverables

- `source.py`: source module with reproducible independent cycle sampling.
- `shaper.py`: simulated-time TBF followed by FIFO, non-preemptive LBF.
- `Input_Traffic_Trace.txt` and `Output_Traffic_Trace.txt`: corresponding 1,800 s
  experiment, seed 3026, selected configuration below.
- `Input_Trace_File.txt` and `Output_Trace_File.txt`: identical copies using the
  filenames specified in the assignment's deliverables section.
- `output/pdf/report.pdf`: three-page report; editable source in `report.tex`.
- `analysis/`: search results, independent replications, KPI summaries, plots,
  buffer/token history and drop log.

## Environment and commands

Python 3.10 or newer; no compilation needed for either application. Install
dependencies with `python -m pip install -r requirements.txt`. NumPy is required
by the source; SciPy and Matplotlib support the experiments. PDF compilation
requires `pdflatex` (TeX Live with standard packages).

Run these commands **from this directory**. The interpreter used here was
`/home/alessandrovulcu/.conda/envs/sklearn-env/bin/python`; substitute it for
`python` if needed on this machine.

Generate the submitted input and process it with the selected shaper:

```bash
python source.py --duration 1800 --seed 3026 --output Input_Traffic_Trace.txt
python shaper.py --input Input_Traffic_Trace.txt --output Output_Traffic_Trace.txt \
  --rho 180000 --b 4096 --bi 16384 --mu 220000 --bo 4096
```

All five shaper parameters are configurable through the flags above. Rates are
**bytes/s**, not bits/s; bucket and buffer capacities are integers in bytes
(one token per byte). Defaults match this selected configuration. Each module
also supports `--help`. For a different training file, use `source.py --training`.

Reproduce the full search, submission traces, statistics, figures and report:

```bash
python -m unittest -v test_shaper.py
python experiments.py
python build_report.py
```

The experiments regenerate both pairs of trace filenames. Individual module runs
write only their requested trace paths; the shaper also writes an adjacent
`*_drops.csv` file. Rebuild the report after regenerating experiments.
`experiments.py --search-duration 300 --duration 1800 --replications 10` spells out
the defaults; shorter runs are exploratory and do not reproduce reported statistics.
`build_report.py` uses the final, documented grid and configuration in its narrative;
revise that narrative if changing the grid or selection rule.

## Source reuse and batch convention

`data/zoom_training_180s.csv` and `data/zoom_validation_120s.csv` are byte-for-byte
copies of Homework 1's exported CSVs. Training covers the selected camera-on
interval `[270,450)` s relative to the first filtered packet; held-out validation
covers `[450,570)` s. CSV times are relative to each sample's start. Lengths are
captured Ethernet frame lengths (`frame.len`), not media payload bytes.

Exactly as in Homework 1, adjacent packets separated by at most 1 ms form a
cluster. Both boundary clusters are excluded. Each of 7,233 complete cycles
stores its duration to the next cluster start and its joint list of packet
offsets and lengths. Whole cycles are sampled independently and uniformly with
NumPy's seeded generator, preserving within-cycle dependence. Mean model rate
is 865.95 kbit/s; maximum packet length is 1,341 B.

Homework 2 requires identical timestamps for packets generated in the same batch.
The default therefore emits the sampled cycle's packet list at its start epoch.
`source.py --preserve-offsets` restores Homework 1's original short packet offsets;
the experiments include that variant as a robustness check. This changes packet
inter-arrival times within batches, while preserving fitted batch epochs, counts
and lengths. The tests verify exact reproduction of Homework 1's 120 s synthetic
trace packet count and byte total with offsets enabled.

The source starts at epoch zero and stops generating at `duration` (exclusive).
Every packet gets a unique, consecutive ID. The source simulates a sustained
camera-on flow; it does not add the manually controlled camera phases from capture.

## Trace format and queue semantics

Each trace has no header and contains three whitespace-separated columns:

```text
packet_id    timestamp_seconds    packet_length_bytes
```

Each actual row contains numeric values. Input timestamps are generation times;
output timestamps are completion times. Same-batch input timestamps match; IDs
and lengths persist. Lost IDs are absent from output. Trace reader rejects
duplicate/negative IDs, invalid sizes, nonfinite/negative times, and decreasing
timestamps. It accepts blank lines and `#` comments.

- The token bucket starts full. Continuous tokens accumulate lazily at event
  times and are capped at `b`. Each departure consumes its packet's full length.
- Packets longer than `b` are dropped as `larger_than_bucket`; they never block
  the FIFO. Other packets unable to leave immediately wait in the input queue.
- `bi` and `bo` bound **waiting bytes**. The LBF's packet in service is excluded.
  Idle service accepts immediately even when `bo=0`. Full queues tail-drop the
  new packet with reason `input_overflow` or `output_overflow`.
- An accepted TBF departure consumes tokens even if the LBF drops it. There is
  no backpressure or token refund.
- Ties process LBF completion first, queued token-eligible packets next, then
  new input rows in file order. Existing FIFO packets cannot be bypassed.
- Packet transmission takes `length/mu` simulated seconds. No real-time sleeps,
  threads, payloads, or elapsed execution time affect the simulation.
- Both queues drain after source shutdown. A numerical token tolerance of
  `1e-7` bytes prevents floating-point deadlocks at exact eligibility times.

`analysis/buffer_trace.csv` records waiting bytes and tokens after each event;
`analysis/drops.csv` identifies each discarded packet and its stage. The shaper's
Python API can optionally retain TBF departures for token-envelope validation.

## Experimental method and results

The proposed shaping-only budgets are loss at most 1%, byte delivery at least
99%, mean delay at most 30 ms, p95 delay at most 50 ms, p99 delay at most 100 ms,
and p95 absolute successive delivered-packet delay variation at most 30 ms.
These are chosen experimental targets, not Zoom specifications.

Search uses one common 300 s trace, seed 2026, across 192 configurations. Of
these, 28 pass every budget. Feasible settings minimize the explicitly chosen
resource score:

```text
cost = rho/100000 + mu/100000 + (b + bi + bo)/16384
```

This treats rate reservations and burst/storage allowances as normalized design
resources. It is a stated preference, not a monetary or globally optimal cost.
The selected setting is saved in `selected_config.json`: rho=180000, b=4096,
bi=16384, mu=220000, bo=4096, cost=5.50.

Ten independent 1,800 s runs (seeds 3026–3035) confirm all budgets without using
those seeds for selection. Mean loss is about 0.169%, mean delay 16.71 ms and
mean p95 delay 44.89 ms. Full results and Student-t 95% confidence intervals
across run-level metrics are in `analysis/results.json`. A quantile interval
describes the mean run quantile, not an individual packet or pooled quantile.

Throughput counts bytes completed within `[0,T)` over fixed duration `T`.
Delay and delivery/loss fractions include the drain. Delay describes survivors;
loss is reported separately to expose survivor bias. Jitter is p95 of absolute
successive delivered-packet delay differences, not the RTP jitter estimator.

The reported statistical precision concerns simulation randomness conditional on
this fitted model. It excludes training uncertainty and does not establish Zoom
QoS generally. As Homework 1 reported, independent cycle sampling loses slow
traffic correlation and overstates some short-window variability. The held-out
120 s capture and original-offset checks are additional descriptive checks.
The shaper does not model encoder adaptation, propagation, decoding or playout.

## Validation

Eight unit tests cover hand-calculated token/serialization times, FIFO behavior,
input/output overflows, exclusion of in-service bytes, event ties, oversized
packets, configuration and trace validation, source reproduction, packet
conservation, bounded queues, nonoverlapping service and TBF release envelopes.
The final PDF is three pages and was rendered for visual inspection.
