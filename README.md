# Mini Algo-Trading System

##  Objective
Design a Python-based mini algo-trading prototype that:

- Connects to a stock data API (Alpha Vantage)
- Implements a sample trading strategy (RSI + Moving Average crossover)
- Stores & analyzes trades automatically in Google Sheets
- Generates portfolio analytics and buy/sell signals using rule-based logic and ML

---
## Features Implemented

## 1. Data Ingestion
Fetches daily stock data for RELIANCE.NS, TCS.NS, and INFY.NS using Alpha Vantage API

## 2. Trading Strategy Logic
Buy signal: RSI < 30 AND 20-DMA crosses above 50-DMA

Sell signal: 20-DMA crosses below 50-DMA

Backtesting for last 6 months

Logs trades, calculates P&L and win ratio

## 3. Machine Learning (Bonus)
Features: RSI, MACD, MA20, MA50, Signal Line, Volume

Model: Decision Tree Classifier

Target: Predict next-day price movement

Outputs model accuracy

## 4. Google Sheets Integration
Logs each trade to Google Sheets

Maintains:

Trade Log (Sheet1)

Summary Tab with Total P&L and Win Ratio

## 5. Automation
One-click run() function:

Fetches data

Computes indicators

Runs strategy

Logs trades & stats

Trains ML model
