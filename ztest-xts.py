import requests

class XTSAPI:

	def place_order(self, ticker, side, quantity, order_type, price):
		
		data = {
			"exchangeSegment": "NSECM",
			"exchangeInstrumentID": ticker,
			"productType": "NRML",
			"orderType": order_type,
			"orderSide": side,
			"timeInForce": "DAY",
			"disclosedQuantity": 0,
			"orderQuantity": quantity,
			"limitPrice": price,
			"stopPrice": 0,
			"orderUniqueIdentifier": "123abc"

		} 
		headers = {"token": "some token"}
		requests.post("jkfasdf", json=data, headers=headers)
		

	def cancel_order(self, order_id):
		requests.delete("/fdsahjk", params={"appOrderID": order_id})



api = XTSAPI()

api.place_order("ADANIENT", "BUY", 1, "LIMIT", 1000)

api.cancel_order(1234)