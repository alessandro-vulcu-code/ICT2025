# Network Modeling — Homework 2

## Traffic Source and Composite Traffic Shaper

This project generates synthetic Google Meet UDP traffic and simulates a Token Bucket Filter (TBF) followed by a Leaky Bucket Filter (LBF). The simulation uses logical time.

## Requirements

- Python 3
- `google-meet-incoming.csv` (packet-length data from Homework 1)
- `matplotlib` for the sensitivity analysis figure

Run all commands from the project directory.

## 1. Generate Input Traffic

```bash
python3 source_homework2.py --csv google-meet-incoming.csv --batches 31339 --seed 42 --output Input_Traffic_Trace.txt
```

The trace contains `packet_id,timestamp_seconds,length_bytes`, without a header. Packets in the same batch share a timestamp.

## 2. Run the Composite Shaper

```bash
python3 composite_shaper.py --input Input_Traffic_Trace.txt --output Output_Traffic_Trace.txt --rho 1000000 --bucket 5000 --input-buffer 100000 --mu 1000000 --output-buffer 100000
```

The five configurable parameters are:

| Parameter | Description |
|---|---|
| `--rho` | TBF token rate (tokens/s) |
| `--bucket` | Token bucket capacity (tokens) |
| `--input-buffer` | TBF buffer size (bytes) |
| `--mu` | LBF transmission rate (bytes/s) |
| `--output-buffer` | LBF buffer size (bytes) |

Both filters use FIFO ordering. One token is required per byte. The output timestamps represent packet transmission completion times. Dropped packets are excluded.

The supplied input/output traces use the baseline parameters shown above. C13 and C08 were evaluated separately.

## 3. Run Tests and QoS Analysis

```bash
python3 boundary_tests.py
python3 qos_analysis.py --input Input_Traffic_Trace.txt --output Output_Traffic_Trace.txt
```

## 4. Reproduce Experiments

```bash
python3 statistical_experiments.py
python3 sensitivity_analysis.py
python3 configuration_optimization.py
python3 parameter_search.py
python3 long_duration_validation.py
```

The `results/` folder contains saved experimental CSV files and the sensitivity analysis figure. Running the scripts may create new output files in the main project directory.

## Submission Files

The submission contains the Python source code, `google-meet-incoming.csv`, matching input/output trace files, saved experimental results, this README, and the PDF report.