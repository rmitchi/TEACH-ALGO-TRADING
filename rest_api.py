from fastapi import FastAPI
import uvicorn

app = FastAPI()

cars = [
	{
		"id": 1,
		"name": "BMW",
		"color": "BLACK",
		"price": 100
	},
	{
		"id": 2,
		"name": "BMW",
		"color": "WHITE",
		"price": 200
	},
	{
		"id": 3,
		"name": "FERRARI",
		"color": "RED",
		"price": 300
	},
]

@app.get("/")
async def hello():
	return {"data": "This is hello"}

@app.get("/search-cars")
async def hello2():
	return {"data": cars}

@app.get("/buy")
async def hello3(car_id: int):

	for car in cars:
		if car['id'] == car_id:
			cars.remove(car)
			break
	return {"data": "congo"}

uvicorn.run(app, port=7999)