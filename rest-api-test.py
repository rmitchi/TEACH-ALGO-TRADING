import requests

url = "http://localhost:7999/search-cars"
response = requests.get(url)
print(response)
print(response.json())

print("Available cars")
for car in response.json()['data']:
	print("Name of car", car['name'])
	print("Color", car['color'])
	print("Price Rs:", car['price'])

url = "http://localhost:7999/buy"
params = {"car_id": 2}
response = requests.get(url=url, params=params)
print(response)
print(response.json())
