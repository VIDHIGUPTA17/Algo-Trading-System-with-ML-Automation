# def backtest(df, initial_cash=100000):
#     cash, position = initial_cash, 0
#     trades = []
#     for date, row in df.iterrows():
#         if row.signal == 1 and cash>0:
#             qty = cash // row.close
#             cash -= qty * row.close
#             position += qty
#             trades.append((date,'BUY',qty,row.close))
#         elif row.signal == -1 and position>0:
#             cash += position * row.close
#             trades.append((date,'SELL',position,row.close))
#             position = 0
#     pnl = cash + position*df['close'].iloc[-1] - initial_cash
#     win_ratio = sum(1 for t in trades if t[1]=='SELL' and t[3]>next(t2[3] for t2 in trades if t2[0]<t[0] and t2[1]=='BUY')) / max(1, sum(1 for t in trades if t[1]=='SELL'))
#     return trades, pnl, win_ratio


def backtest(df, initial_cash=100000):
    cash, position = initial_cash, 0
    trades = []

    for date, row in df.iterrows():
        if row.signal == 1 and cash > 0:
            qty = cash // row.close
            cash -= qty * row.close
            position += qty
            trades.append((date, 'BUY', qty, row.close))
        elif row.signal == -1 and position > 0:
            cash += position * row.close
            trades.append((date, 'SELL', position, row.close))
            position = 0

    pnl = cash + position * df['close'].iloc[-1] - initial_cash

    win_count = 0
    sell_count = 0

    for t in trades:
        if t[1] == 'SELL':
            sell_count += 1
            try:
                prev_buy_price = next(
                    t2[3] for t2 in reversed(trades)
                    if t2[0] < t[0] and t2[1] == 'BUY'
                )
                if t[3] > prev_buy_price:
                    win_count += 1
            except StopIteration:
                pass

    win_ratio = win_count / max(1, sell_count)

    return trades, pnl, win_ratio
