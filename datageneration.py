from alpha_vantage.timeseries import TimeSeries
import pandas as pd

# Replace this with your real API key
API_KEY = 'ITWMMM9D9P29WMQ7'

# Initialize Alpha Vantage client
ts = TimeSeries(key=API_KEY, output_format='pandas')

# Get hourly data for a stock or crypto (example: IBM stock)
data, meta_data = ts.get_intraday(symbol='IBM', interval='60min', outputsize='compact')

# Rename and reset index
data.reset_index(inplace=True)
data.rename(columns={
    'date': 'timestamp',
    '1. open': 'open',
    '2. high': 'high',
    '3. low': 'low',
    '4. close': 'close',
    '5. volume': 'volume'
}, inplace=True)

# Optional: sort by time
data.sort_values(by='timestamp', inplace=True)

# Save to CSV
data.to_csv('data.csv', index=False)

print("✅ data.csv file generated!")
