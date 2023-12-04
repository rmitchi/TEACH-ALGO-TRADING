import pandas as pd

class MyStrategy:

	def __init__(self, name) -> None:
		self.name = name
		self.positions = {}
		self.trades = []
		self.report = []

	def entry_conditions(self, ts, row):
		...
	
	def exit_conditions(self, ts, row, position = None):
		...

	def set_data(self, symbol, df):
		self.symbol = symbol
		self.df = df

	def generate_report(self):
		report_df = pd.DataFrame(self.report)
		report_df['pl_abs'] = report_df['exit_price'] - report_df['entry_price']
		report_df['cum'] = report_df['pl_abs'].cumsum()
		report_df['account_balance'] = report_df['cum'] + 1000
		print(report_df)

		print("PL ABS: ", report_df['pl_abs'].sum())
		print("DRAWDOWN: ", report_df['cum'].min())

		report_df.to_csv(f"REPORT-{self.name}-{self.symbol}.csv")

	def simulate(self):
		symbol = self.symbol
		df = self.df

		for ts, row in df.iterrows():
			print(ts)
			if symbol not in self.positions:
				
				entry_data = self.entry_conditions(ts, row)

				if entry_data is None:
					continue
				
				trade = {
					"datetime": ts,
					"side": "BUY",
					"price": row["Close"],
				}
				self.positions[symbol] = trade
				self.trades.append(trade)

			else:
				exit_data = self.exit_conditions(ts, row, self.positions[symbol])

				if exit_data is None:
					continue

				trade = {
					"datetime": ts,
					"side": "SELL",
					"price": row["Close"],
					"reason": exit_data['reason']
				}
				self.trades.append(trade)
				
				self.report.append({
					"entry_time": self.positions[symbol]['datetime'],
					"exit_time": ts,
					"entry_price": self.positions[symbol]['price'],
					"exit_price": row["Close"],
					"reason": exit_data["reason"]
				})
				del self.positions[symbol]


		# Completed simulation
		self.generate_report()

