# # algo_runner.py
# from alpha_vantage_client import AlphaVantageClient
# from rsi_ma_crossover import compute_indicators, generate_signals
# from backtester import backtest
# from logger import log_trades
# import pandas as pd
# from config import API_KEY, SYMBOLS

# def run():
#     client = AlphaVantageClient()
#     all_trades, total_pnl, win_ratio = [], 0, 0
#     for sym in SYMBOLS:

#         df = client.fetch_daily(sym).last('6M')
#         df = compute_indicators(df)
#         df = generate_signals(df)
#         trades, pnl, wr = backtest(df)
#         all_trades += trades
#         total_pnl += pnl
#         win_ratio = (win_ratio+wr)/2
#     log_trades(all_trades, total_pnl, win_ratio)

# if __name__ == "__main__":
#     run()


from alpha_vantage_client import AlphaVantageClient
from rsi_ma_crossover import compute_indicators, generate_signals
from backtester import backtest
from logger import log_trades
import pandas as pd
from config import API_KEY, SYMBOLS
from train_model import train

def run():
    train("data.csv")

    client = AlphaVantageClient()
    all_trades, total_pnl, win_ratio = [], 0, 0
    for sym in SYMBOLS:
        df = client.fetch_daily("AAPL") 
        df = compute_indicators(df)
        df = generate_signals(df)
        trades, pnl, wr = backtest(df)
        all_trades += trades
        total_pnl += pnl
        win_ratio = (win_ratio + wr) / 2
    log_trades(all_trades, total_pnl, win_ratio)

if __name__ == "__main__":
    run()
