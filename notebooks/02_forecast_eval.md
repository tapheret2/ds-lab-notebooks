# Forecast evaluation checklist

1. Collect forecasts with `as_of` timestamp  
2. Wait for outcomes  
3. Score: Brier, log-loss (`brier-lab`)  
4. Calibration plot (reliability bins)  
5. Compare to **market mid** or naive baseline  

Never score with prices after resolution mixed into training features.
