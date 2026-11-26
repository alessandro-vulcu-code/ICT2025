# Network Modeling - AY 2026/2027 Homework 2 - Traffic Shaping

This package contains the Source module, the Shaper module, one input trace with its
output trace, and the report.

## Files

- `source.py`: Source module. Generates the synthetic packet flow of the HW1 model.
- `shaper.py`: Shaper module. Runs a trace through the Token Bucket Filter and the Leaky Bucket Filter.
- `params.json`: the HW1 model parameters that are fitted once from the Teams capture, read by `source.py`.
- `Input_Traffic_Trace.txt`: input trace, 3600 s, seed 1.
- `Output_Traffic_Trace.txt`: the output of the shaper for that input trace.

## Requirements

Python 3.8 or newer with `numpy`, `pandas` and `scipy`. There is nothing to compile.

```
pip install numpy pandas scipy
```

## Running

Both programs are run from the folder that contains the files above.

**1. Source**

```
python source.py --duration 3600 --seed 1
```

`--duration` is the simulated time in seconds and `--seed` selects the random stream. The model parameters are read from `params.json`.

**2. Shaper**

```
python shaper.py --r 45800 --b 120000 --Bi 10000 --mu 1830000 --Bo 120000
```

| Option | Meaning | Unit |
|---|---|---|
| `--r` | token generation rate (called rho in the report) | tokens/s (1 token = 1 byte) |
| `--b` | token bucket capacity | tokens |
| `--Bi` | TBF input buffer | bytes |
| `--mu` | LBF maximum forwarding rate | bytes/s |
| `--Bo` | LBF output buffer | bytes |

The values above are the configuration chosen in the report. The program prints the number of packets in, out and dropped (split by cause) and the loss ratio.
