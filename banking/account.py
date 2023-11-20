class Account:

	def __init__(self, id: str, first_name: str, last_name: str):

		self.id = id
		self.first_name = first_name
		self.last_name = last_name

		self.balance = 0.0

	@property
	def name(self) -> str:
		return f"{self.first_name.title()} {self.last_name.title()}"
	
	def deposit(self, amount: float) -> None:
		self.balance += amount

	def withdraw(self, amount: float) -> None:
		
		if self.balance < amount:
			raise Exception("Insufficient money")
		
		self.balance -= amount
