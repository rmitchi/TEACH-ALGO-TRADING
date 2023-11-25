api_key = "ad948ba71cdd3e407d4b7bf370d2efb237b774b4705c7fdf9e54c723cb46f0eb"
api_secret = "472bf2e903f2f22adc807fc2ba50abc79f1d407ba89b076accfa7ee45fe214b7"


from binance import Client # pip install python-binance

import time

orders = []


client = Client(api_key=api_key, api_secret=api_secret, testnet=True)

data = client.futures_account_balance()
print(data)

while True:
	params = {
		"symbol": "BTCUSDT",
		"side": "BUY",
		"type": "MARKET",
		"quantity": 1
	}
	data = client.futures_create_order(**params)
	orders.append("quantity")
	print(data)

	time.sleep(2)


	if len(orders) == 3:
		params = {
		"symbol": "BTCUSDT",
		"side": "SELL",
		"type": "MARKET",
		"quantity": len(orders)
		}
		data = client.futures_create_order(**params)
		print(data)
		orders = []