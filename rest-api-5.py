from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

orders = []

class PlaceOrder(BaseModel):

	ticker : str
	side : str
	quantity : int
	order_type : str

@app.post("/")
async def place_order(data: PlaceOrder):
	order = {
		"id": len(orders) + 1,
		"status": "PENDING",
		"ticker": data.ticker,
		"side": data.side,
		"quantity": data.quantity,
		"order_type": data.order_type,
	}
	orders.append(order)
	return {"data": "success"}

@app.get("/")
async def get_orders():
	return orders

@app.delete("/")
async def remove_order(id: int):
	return orders

uvicorn.run(app, port=7999)