from s_7_strategy_creation import MyStrategy
import yfinance as yf
import datetime as dt
import pandas_ta as pta

"""
My 5rd strategy
MACD 

SL - 1
TP - 2
"""

class Strategy4(MyStrategy):

	def entry_conditions(self, ts, row):
		# print(row)
		if ts.time() > dt.time(15,14):
			return 
		
		if row["MACD"] > row["SIGNAL"]:
			return {
				"side": "BUY"
			}
	
	def exit_conditions(self, ts, row, position):
		if ts.time() > dt.time(15,15):
			return {
				"side": "SELL",
				"reason": "EOD"
			}

		if USE_SL:
			sl = position['price'] - SL_POINT
			if row['Low'] <= sl:
				return {
					"side": "SELL",
					"reason": "STOPLOSS"
				}
		
		if USE_TP:
			tp = position['price'] + TP_POINT
			if row['High'] >= tp:
				return {
					"side": "SELL",
					"reason": "TAKEPROFIT"
				}
		
		if USE_INDICATOR_EXIT:
			if row['MACD'] < row['SIGNAL']:
				return {
					"side": "SELL",
					"reason": "INDICATOR"
				}

SYMBOL = "ADANIENT"
TIMEFRAME = "1m"
PERIOD = "7d"
THRESHOLD = 0.85
USE_SL = False
USE_TP = True
USE_INDICATOR_EXIT = False
SL_POINT = 1
TP_POINT = 4

s1 = Strategy4("MACD V2")

df = yf.download(f"{SYMBOL}.NS", period=PERIOD, interval=TIMEFRAME, progress=False)
macd_df = pta.macd(df["Close"], 12, 26, 9)
# print(macd_df)

df["MACD"] = macd_df["MACD_12_26_9"]
df["SIGNAL"] = macd_df["MACDs_12_26_9"]
# print(df)


s1.set_data(SYMBOL, df)
s1.simulate()