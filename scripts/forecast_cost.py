import pandas as pd

df = pd.read_csv('data/final_dataset.csv')

# Assume current daily cost trend continues
average_daily_cost = df['daily_cost_usd'].mean()

forecast_30_days = average_daily_cost * 30
forecast_90_days = average_daily_cost * 90

forecast = {
    'average_daily_cost_usd': round(average_daily_cost, 4),
    'forecast_30_days_usd': round(forecast_30_days, 4),
    'forecast_90_days_usd': round(forecast_90_days, 4)
}

forecast_df = pd.DataFrame([forecast])
forecast_df.to_csv('data/cost_forecast.csv', index=False)

print("Cost forecast generated:")
print(forecast_df)
