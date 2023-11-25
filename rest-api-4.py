from fastapi import FastAPI
import uvicorn

app = FastAPI()

users = [
	{
		"username": "abc",
		"password":"12345678"
	},
	{
		"username": "xyz",
		"password":"hello"
	},
]

@app.get("/login")
async def login(username: str,password: str) :
	for user in users:
		if user["username"] == username:
			if user["password"] == password:
				return {'data': "successful"}
			else: 
				return {'data': "wrong inputs"}
		else: 
				return {'data': "wrong inputs"}
	return {'data': "wrong inputs"}



uvicorn.run(app, port=7999)