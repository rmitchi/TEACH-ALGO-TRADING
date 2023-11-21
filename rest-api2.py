from fastapi import FastAPI
import uvicorn

app = FastAPI()

accounts = [
	{
		"id": "AC1",
		"name": "Dummy user 1",
		"balance": 1000
	},
	{
		"id": "AC2",
		"name": "Dummy user 2",
		"balance": 5000
	},
]


@app.get("/")
async def Welcome():
	return {"data": "Welcome SBI"}

@app.get("/balance")
async def get_balance(id: str):
	for account in accounts:
		if account['id'] == id:
			return {"balance": account['balance']}
		
	return {"error": "Account not found"}


@app.get("/deposit")
async def deposit(id: str, amount: float):
	for account in accounts:
		if account['id'] == id:
			account["balance"] = amount + account["balance"]
			return {'data':"success"}
		

		
@app.get("/withdraw")
async def withdraw(id: str, amount: float):
	for account in accounts:
		if account['id'] == id:
			if account["balance"] <= amount:
				return {"error": "Funds are not enough"}
			account["balance"] = account["balance"] - amount
			return {'data':"success"}


uvicorn.run(app, port=7999)