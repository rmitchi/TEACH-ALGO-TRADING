class Shop:

	cars = []

	def add_car(self, car):
		self.cars.append(car)

	def search(self, name: str = None, color: str = None, min_price: float = None, max_price: float = None) -> list:
		
		result = []

		for car in self.cars:

			if (name is not None) and (car.name != name):
				continue

			if (color is not None) and (car.color != color):
				continue

			if (min_price is not None) and (car.price <= min_price):
				continue

			if (max_price is not None) and (car.price >= max_price):
				continue

			result.append({"name": car.name, "color": car.color, "price": car.price})

		return result
	
	def sell(self):
		...

class Car:

	def __init__(self, name: str, color: str, price: float):

		self.name = name
		self.color = color
		self.price = price

shop = Shop()

c1 = Car("BMW", "White", 100)
shop.add_car(c1)

c2 = Car("BMW", "Black", 200)
shop.add_car(c2)

c3 = Car("Nano", "White", 10)
shop.add_car(c3)


available_cars = shop.search(name="BMW", min_price=110)
print(available_cars)