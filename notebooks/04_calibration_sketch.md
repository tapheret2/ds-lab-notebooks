# 04 — Calibration sketch

## Goal
Plot reliability diagram inputs (bin midpoints vs empirical frequency).

## Steps
1. Collect `(p_hat, y)` pairs
2. Bin by predicted probability
3. Compute mean `p_hat` and mean `y` per bin
4. Plot diagonal reference

## Notes
- Prefer Brier decomposition when n is large
- Pair with `brier-lab` metrics
