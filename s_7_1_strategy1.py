from s_7_strategy_creation import MyStrategy
import yfinance as yf
import datetime as dt
import pandas_ta as pta

"""
My 1st strategy
BUY EMA9 > EMA 26
SELL EMA26 < EMA9
"""

class Strategy1(MyStrategy):

	def entry_conditions(self, ts, row):
		# print(row)
		if ts.time() > dt.time(15,14):
			return 
		
		if row['EMA_9'] > row['EMA_26']:
			# print(row)
			return {
				"side": "BUY"
			}
	
	def exit_conditions(self, ts, row):
		if ts.time() > dt.time(15,15):
			return {
				"side": "SELL",
				"reason": "EOD"
			}

		if row['EMA_9'] < row['EMA_26']:
			return {
				"side": "SELL",
				"reason": "INDICATOR"
			}

SYMBOL = "ICICIBANK"
TIMEFRAME = "1m"
PERIOD = "7d"

s1 = Strategy1("EMA cross")

df = yf.download(f"{SYMBOL}.NS", period=PERIOD, interval=TIMEFRAME, progress=False)
df['EMA_9'] = pta.ema(df["Close"], 9)
df['EMA_26'] = pta.ema(df["Close"], 26)

s1.set_data(SYMBOL, df)
s1.simulate()