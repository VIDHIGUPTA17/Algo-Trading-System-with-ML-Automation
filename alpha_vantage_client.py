import os
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from config import API_KEY, SYMBOLS
# from .config import API_KEY, SYMBOLS
SYMBOLS = ['RELIANCE.NS','TCS.NS','INFY.NS']


class AlphaVantageClient:
    def __init__(self):
        self.ts = TimeSeries(key=API_KEY, output_format='pandas')
    def fetch_daily(self, symbol):
        data, _ = self.ts.get_daily(symbol=symbol, outputsize='full')
        data.index = pd.to_datetime(data.index)
        return data[['4. close']].rename(columns={'4. close': 'close'})
    def fetch_intraday(self, symbol, interval='15min'):
        df, _ = self.ts.get_intraday(symbol=symbol, interval=interval, outputsize='full')
        df.index = pd.to_datetime(df.index)
        return df[['4. close']].rename(columns={'4. close': 'close'})
