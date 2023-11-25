from websocket import WebSocketApp
import json

def on_open(ws):
	print("opened")

	_ = {
		"method": "SUBSCRIBE",
		"params":
		["btcusdt@trade"],
		"id": 1
	}
	ws.send(json.dumps(_))


def on_message(ws, data):
	print(data)

wss = WebSocketApp("wss://stream.binance.com:9443/ws", on_open=on_open, on_message=on_message)
wss.run_forever()