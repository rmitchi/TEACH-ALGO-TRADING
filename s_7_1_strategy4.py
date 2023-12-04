from s_7_strategy_creation import MyStrategy
import yfinance as yf
import datetime as dt
import pandas_ta as pta

"""
My 3rd strategy
BUY RSI < 40 and ema 9 > ema 26
SELL RSI > 60
"""

class Strategy4(MyStrategy):

	def entry_conditions(self, ts, row):
		# print(row)
		if ts.time() > dt.time(15,14):
			return 
		
		if row["SMALL_EMA"] > row["BIG_EMA"] and ((row["SMALL_EMA"] - row["BIG_EMA"]) > THRESHOLD):
			return {
				"side": "BUY"
			}
	
	def exit_conditions(self, ts, row, position):
		if ts.time() > dt.time(15,15):
			return {
				"side": "SELL",
				"reason": "EOD"
			}

		sl = position['price'] - SL_POINT
		if row['Low'] <= sl:
			return {
				"side": "SELL",
				"reason": "STOPLOSS"
			}
		
		tp = position['price'] + TP_POINT
		if row['High'] >= tp:
			return {
				"side": "SELL",
				"reason": "TAKEPROFIT"
			}

SYMBOL = "ICICIBANK"
TIMEFRAME = "1m"
PERIOD = "1d"
THRESHOLD = 0.85
SL_POINT = 1
TP_POINT = 2

s1 = Strategy4("EMA GAP")

df = yf.download(f"{SYMBOL}.NS", period=PERIOD, interval=TIMEFRAME, progress=False)
df['SMALL_EMA'] = pta.ema(df["Close"], 9)
df['BIG_EMA'] = pta.ema(df["Close"], 50)


s1.set_data(SYMBOL, df)
s1.simulate()