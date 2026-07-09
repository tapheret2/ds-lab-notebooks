# Polymarket join sketch

```text
scan_*.json  (forecasts)
     +
resolved markets (outcome YES/NO)
     →
eval table: brier_model vs brier_market
```

Use `pm-agent daily-scan` then `pm-agent eval` from polymarket-agent.
