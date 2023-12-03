# import datetime
# import yfinance as yf	# pip install yfinance

# print(datetime.datetime.now())
# df = yf.download("SBIN.NS", period="7d", interval="1m", prepost=False, progress=False)
# print(df)
# df.to_csv("SBIN.csv")
# print(datetime.datetime.now())


# ! ======================================

import yfinance as yf
import pandas as pd

df = pd.read_csv("EQUITY_L.csv")
# print(df)
tickers = list(df['SYMBOL'])
# print(tickers)

# tickers = ['HDFCBANK', 'ICICIBANK', 'INDUSINDBANK', 'KOTAKBANK', 'BOB', 'BOI', 'SBIN', 'AXISBANK']

for ticker in tickers:
	print("Downloading ticker", ticker)

	df = yf.download(f"{ticker}.NS", period="7d", interval="1m", prepost=False, progress=False)
	print(df)

	df.to_csv(f"data/{ticker}.csv")