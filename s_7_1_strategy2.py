from s_7_strategy_creation import MyStrategy
import yfinance as yf
import datetime as dt
import pandas_ta as pta

"""
My 1st strategy
BUY RSI < 40
SELL RSI > 60
"""

class Strategy2(MyStrategy):

	def entry_conditions(self, ts, row):
		# print(row)
		if ts.time() > dt.time(15,14):
			return 
		
		if row['RSI'] < 40:
			return {
				"side": "BUY"
			}
	
	def exit_conditions(self, ts, row):
		if ts.time() > dt.time(15,15):
			return {
				"side": "SELL",
				"reason": "EOD"
			}

		if row['RSI'] > 60:
			return {
				"side": "SELL",
				"reason": "INDICATOR"
			}

SYMBOL = "ICICIBANK"
TIMEFRAME = "1m"
PERIOD = "7d"

s1 = Strategy2("RSI depth")

df = yf.download(f"{SYMBOL}.NS", period=PERIOD, interval=TIMEFRAME, progress=False)
df['RSI'] = pta.rsi(df["Close"], 9)

s1.set_data(SYMBOL, df)
s1.simulate()