import yfinance as yf
import datetime as dt

RSI_PERIOD = 20
OVERSOLD = 40
OVERBOUGHT = 60

def my_strategy(SYMBOL, TIMEFRAME):
	df = yf.download(f"{SYMBOL}.NS", period="7d", interval=TIMEFRAME, progress=False)
	print(df)

	import pandas_ta as pta
	df['rsi'] = pta.rsi(df['Close'], RSI_PERIOD)

	trades = []
	report = []
	positions = {}

	def entry_conditions(dt1, row):
		if dt1.time() > dt.time(15,14):
			return 
		
		if row['rsi'] < OVERSOLD and (row['Close'] > 500):
			return {
				"side": "BUY"
			}
		
	def exit_conditions(dt1, row):

		if dt1.time() > dt.time(15,15):
			return {
				"side": "SELL",
				"reason": "EOD"
			}

		if row['rsi'] > OVERBOUGHT:
			return {
				"side": "SELL",
				"reason": "INDICATOR"
			}

	for _, row in df.iterrows():
		# print(row)

		# Check for entry
		if SYMBOL not in positions:
			entry_data = entry_conditions(_, row)

			if entry_data is None:
				continue
			
			trade = {
				"datetime": _,
				"side": "BUY",
				"price": row["Close"],
			}
			positions[SYMBOL] = trade
			trades.append(trade)
		
		# Check for exit
		else:
			exit_data = exit_conditions(_, row)

			if exit_data is None:
				continue

			trade = {
				"datetime": _,
				"side": "SELL",
				"price": row["Close"],
				"reason": exit_data['reason']
			}
			trades.append(trade)
			report.append({
				"entry_time": positions[SYMBOL]['datetime'],
				"exit_time": _,
				"entry_price": positions[SYMBOL]['price'],
				"exit_price": row["Close"],
				"reason": exit_data["reason"]
			})
			del positions[SYMBOL]

	# print(report)

	import pandas as pd
	report_df = pd.DataFrame(report)
	report_df['pl_abs'] = report_df['exit_price'] - report_df['entry_price']
	report_df['cum'] = report_df['pl_abs'].cumsum()
	report_df['account_balance'] = report_df['cum'] + 1000
	print(report_df)

	print("PL ABS: ", report_df['pl_abs'].sum())
	print("DRAWDOWN: ", report_df['cum'].min())

	report_df.to_csv(f"REPORT-{SYMBOL}.csv")

	# import dhooks

	# hook = dhooks.Webhook("https://discord.com/api/webhooks/1180752033276497961/EyZDwE9t58JmtQvyp2j6pI7qYUgEMRXHslUE3aCYpVwAlAbTVdpUnfJWAJZgBt3yoYre")
	
	# with open(f"REPORT-{SYMBOL}.csv") as f:
	# 	file_name = f"REPORT-{SYMBOL}.csv"
	# 	x = dhooks.File(f, name=file_name)
	# 	hook.send(file=x)
	# 	f.close()

SYMBOLS = ["REFEX"]#["HDFCBANK", "AXISBANK", "ICICIBANK", "SBIN"]
for symbol in SYMBOLS:
	my_strategy(symbol, "1m")