import yfinance as yf


df = yf.download("AXISBANK.NS", period="1d", interval="1m", progress=False)
print(df)

import pandas_ta as pta

ema = pta.rsi(df['Close'], 20)
print(ema)