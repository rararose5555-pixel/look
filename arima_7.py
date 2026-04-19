import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings('ignore')

# Load data
data = pd.read_csv('airline_passengers.csv')
data['Month'] = pd.to_datetime(data['Month'] + '-01')  # fix date parsing
data.set_index('Month', inplace=True)
ts = data['Passengers'].dropna()

# ADF Test
result = adfuller(ts)
print("ADF Statistic:", result[0])
print("p-value:", result[1])
for key, value in result[4].items():
    print(f"{key}: {value:.4f}")

# Fit ARIMA and Forecast
model_fit = ARIMA(ts, order=(2, 1, 2)).fit()
forecast = model_fit.get_forecast(steps=12)
fc_mean = forecast.predicted_mean
fc_ci = forecast.conf_int()

# 2 Graphs
fig, axes = plt.subplots(2, 1, figsize=(12, 8))

# Graph 1 - smooth line
axes[0].plot(ts, color='black', linewidth=1.5)
axes[0].set_title('Monthly Airline Passengers')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Number of Passengers')

# Graph 2 - actual + forecast
axes[1].plot(ts, color='black', linewidth=1.5, label='Original')
axes[1].plot(fc_mean, color='black', linewidth=1.5, linestyle='--', label='Forecast')
axes[1].fill_between(fc_ci.index, fc_ci.iloc[:, 0], fc_ci.iloc[:, 1], color='lightgray', alpha=0.5)
axes[1].set_title('ARIMA Forecast')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Passengers')
axes[1].legend()

plt.tight_layout()
plt.show()