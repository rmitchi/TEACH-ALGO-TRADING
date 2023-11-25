from fastapi import FastAPI
import uvicorn

app = FastAPI()

accounts = [
	{
		"id": "AC1",
		"name": "Dummy user 1",
		"no_of_followers": 0,
		"no_of_following": 0,
	},
	{
		"id": "AC2",
		"name": "Dummy user 2",
		"no_of_followers": 0,
		"no_of_following": 0,
	},
	{
		"id": "AC3",
		"name": "Dummy user 3",
		"no_of_followers": 0,
		"no_of_following": 0,
	},
	{
		"id": "AC4",
		"name": "Dummy user 4",
		"no_of_followers": 0,
		"no_of_following": 0,
	},
	{
		"id": "AC5",
		"name": "Dummy user 5",
		"no_of_followers": 0,
		"no_of_following": 0,
	},
]

@app.get("/")
async def get_follow(id: str):
	for account in accounts:
		if account['id'] == id:
			return {"no_of_followers": account['no_of_followers'],"no_of_following": account['no_of_following']}
		
	return {"error": "Account not found"}


@app.get("/follow")
async def follow(user_id: str, follow_id: str):
	for account in accounts:
		if account['id'] == user_id:
			account['no_of_following'] = account['no_of_following'] + 1
		if account['id'] == follow_id:
			account['no_of_followers'] = account['no_of_followers'] + 1
		
@app.get("/unfollow")
async def withdraw(user_id: str, follow_id: str):
	for account in accounts:
		if account['id'] == user_id:
			account['no_of_following'] = account['no_of_following'] - 1
		if account['id'] == follow_id:
			account['no_of_followers'] = account['no_of_followers'] - 1

uvicorn.run(app, port=7999)