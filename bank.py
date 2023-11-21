class Credit:

	def give_credit(self, account_id: str, amount: float):
		...

	def valid(self, account_id: str):
		...

class Transfer:
	...

class Utility:
	...

class Loan:
	
	...

class Bank(Credit, Loan, Transfer, Utility):

	def __init__(self):

		self.accounts = {}

	def add_account(self, account):
		self.accounts[account.account_id] = account

	def send_message(self, message):
		print(message)

	def transfer(self, from_account_id: str, to_account_id: str, amount: float) -> int:
		"""
		This function transfers amount from one account to another account
		"""

		if from_account_id not in self.accounts:
			return 1
		
		if to_account_id not in self.accounts:
			return 2
		
		from_account = self.accounts[from_account_id]
		to_account = self.accounts[to_account_id]

		if from_account.balance < amount:
			self.send_message(f"Insufficient funds in account {from_account_id}, can not transfer funds")
			return 3
		
		from_account.balance -= amount
		self.send_message(f"{amount} has been debited from {from_account_id}, new balance is {from_account.balance}")

		to_account.balance += amount
		self.send_message(f"{amount} has been credited to {to_account_id}, new balance is {to_account.balance}")

		return 0

	def deposit(self, account_id, amount):

		if account_id not in self.accounts:
			raise Exception("Account not found")
		
		account = self.accounts[account_id]

		account.balance += amount

	def withdraw(self, account_id, amount):

		if account_id not in self.accounts:
			raise Exception("Account not found")
		
		account = self.accounts[account_id]

		if account.balance < amount:
			raise Exception("Insufficient amount")

		account.balance -= amount

	def loan(self, account_id: str, amount: float, interest: float) -> float:
		"""
		This function calculates load amount\n
		"""

		return amount + ((amount * interest / 100) * 12)

class Account:

	def __init__(self, account_id: str, name: str, balance: float) -> None:
		self.account_id = account_id
		self.name = name
		self.balance = balance



BANK = Bank()

account1 = Account(1, "Alex Saverin", 10000)
account2 = Account(2, "Aiden Pearce", 15000)
account3 = Account(3, "Janet Vanhoutten", 20000)

BANK.add_account(account1)
BANK.add_account(account2)
BANK.add_account(account3)

BANK.give_credit()

code1 = BANK.transfer(1, 2, 5000)
code2 = BANK.transfer(1, 2, 5000)
code3 = BANK.transfer(1, 2, 5000)
print(code1, code2, code3)
print(account1.balance)
print(account2.balance)

print(BANK.loan(1, 1000, 1))