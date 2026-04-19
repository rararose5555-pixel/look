import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import warnings
import os

warnings.filterwarnings('ignore')

print(os.getcwd())

data = pd.read_csv('data.csv')
data['Temp'] = pd.to_numeric(data['Temp'], errors='coerce')
ts = data['Temp'].dropna()

result = adfuller(ts)
print("\nADF Statistic :", result[0])
print("p-value        :", result[1])
print("Critical Values:")
for key, value in result[4].items():
    print(f"   {key}: {value:.4f}")

if result[1] <= 0.05:
    print("\n✅ Series is STATIONARY (reject H0)")
else:
    print("\n⚠️  Series is NON-STATIONARY (fail to reject H0) — differencing applied")

ts_diff = ts.diff().dropna()

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Time Series Analysis — Daily Minimum Temperatures', fontsize=14, fontweight='bold')

axes[0, 0].plot(ts.values, color='steelblue')
axes[0, 0].set_title('Daily Minimum Temperatures in Melbourne')
axes[0, 0].set_xlabel('Observations')
axes[0, 0].set_ylabel('Temperature')

axes[0, 1].plot(ts_diff.values, color='darkorange')
axes[0, 1].set_title('Differenced Time Series')
axes[0, 1].set_xlabel('Observations')
axes[0, 1].set_ylabel('Differenced Temp')
axes[0, 1].axhline(0, color='black', linewidth=0.8, linestyle='--')

max_lags = len(ts_diff) // 2 - 1

plot_acf(ts_diff, ax=axes[1, 0], lags=max_lags, title='Autocorrelation Function (ACF)')

plot_pacf(ts_diff, ax=axes[1, 1], lags=max_lags, title='Partial Autocorrelation Function (PACF)')

plt.tight_layout()
plt.show()