class Bank:

	def __init__(self):

		self.accounts = {}

	def add_account(self, account):
		self.accounts[account.account_id] = account

	def transfer(self, from_account_id, to_account_id, amount):

		if from_account_id not in self.accounts:
			raise Exception("Account not found")
		
		if to_account_id not in self.accounts:
			raise Exception("Account not found")
		
		from_account = self.accounts[from_account_id]
		to_account = self.accounts[to_account_id]

		if from_account.balance < amount:
			raise Exception("Insufficient amount")
		
		from_account.balance -= amount
		to_account.balance += amount

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


class Account:

	def __init__(self, account_id, name, balance) -> None:
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

BANK.transfer(1, 2, 5000)
BANK.transfer(1, 2, 5000)

print(account1.balance)
print(account2.balance)