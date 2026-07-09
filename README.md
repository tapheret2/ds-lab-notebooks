# ds-lab-notebooks

![status](https://img.shields.io/badge/status-active-brightgreen) ![python](https://img.shields.io/badge/python-3.10%2B-blue) ![license](https://img.shields.io/badge/license-MIT-lightgrey)

Starter **Data Science lab** templates for forecasting, markets, and agent experiments.

## Layout

```
notebooks/
  01_eda_template.ipynb.md   # outline (copy into Jupyter)
  02_forecast_eval.md
  03_polymarket_join.md
scripts/
  make_skeleton.py
```

## Philosophy

- Prefer **scripts + small notebooks**, not 5k-line notebook monoliths  
- Always define **metric** before model  
- Log timestamps; avoid leakage  

Pair with:

- [polymarket-agent](https://github.com/tapheret2/polymarket-agent)
- [brier-lab](https://github.com/tapheret2/brier-lab)
- [keo-ledger](https://github.com/tapheret2/keo-ledger)
- [coingecko-pulse](https://github.com/tapheret2/coingecko-pulse)

## License

MIT
