from s_7_strategy_creation import MyStrategy
import yfinance as yf
import datetime as dt
import pandas_ta as pta

"""
My 3rd strategy
BUY RSI < 40 and ema 9 > ema 26
SELL RSI > 60
"""

class Strategy2(MyStrategy):

	def entry_conditions(self, ts, row):
		# print(row)
		if ts.time() > dt.time(15,14):
			return 
		
		if row['RSI'] < 40 and row['EMA_9'] > row['EMA_26'] :
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

s1 = Strategy2("RSI & EMA")

df = yf.download(f"{SYMBOL}.NS", period=PERIOD, interval=TIMEFRAME, progress=False)
df['RSI'] = pta.rsi(df["Close"], 9)
df['EMA_9'] = pta.ema(df["Close"], 9)
df['EMA_26'] = pta.ema(df["Close"], 26)


s1.set_data(SYMBOL, df)
s1.simulate()