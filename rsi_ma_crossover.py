# strategies/rsi_ma_crossover.py
import pandas as pd
import numpy as np

def compute_indicators(df):
    delta = df['close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - 100/(1+rs)
    df['MA20'] = df['close'].rolling(20).mean()
    df['MA50'] = df['close'].rolling(50).mean()
    return df.dropna()

def generate_signals(df):
    df['signal'] = 0
    buy_cond = (df['RSI'] < 30) & (df['MA20'].shift(1) < df['MA50'].shift(1)) & (df['MA20'] > df['MA50'])
    sell_cond = (df['MA20'].shift(1) > df['MA50'].shift(1)) & (df['MA20'] < df['MA50'])
    df.loc[buy_cond, 'signal'] = 1
    df.loc[sell_cond, 'signal'] = -1
    return df

# strategies/backtester.py
def backtest(df, initial_cash=100000):
    cash, position = initial_cash, 0
    trades = []
    for date, row in df.iterrows():
        if row.signal == 1 and cash>0:
            qty = cash // row.close
            cash -= qty * row.close
            position += qty
            trades.append((date,'BUY',qty,row.close))
        elif row.signal == -1 and position>0:
            cash += position * row.close
            trades.append((date,'SELL',position,row.close))
            position = 0
    pnl = cash + position*df['close'].iloc[-1] - initial_cash
    win_ratio = sum(1 for t in trades if t[1]=='SELL' and t[3]>next(t2[3] for t2 in trades if t2[0]<t[0] and t2[1]=='BUY')) / max(1, sum(1 for t in trades if t[1]=='SELL'))
    return trades, pnl, win_ratio
