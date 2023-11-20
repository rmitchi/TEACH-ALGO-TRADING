from .account import Account

class Bank:

	def __init__(self, code: str, name: str):

		self.code = code
		self.name = name

		self.accounts = {}

		self.portal = None

	def __get_account(self, account_id: str) -> Account:
		try:
			return self.accounts[account_id]

		except KeyError:
			return self.portal.get_account(account_id)

	def create_account(self, first_name: str, last_name: str) -> Account:
		
		id = f"{self.code}_{len(self.accounts)+1}"
		account = Account(id=id, first_name=first_name, last_name=last_name)
		self.accounts[account.id] = account
		return account
	
	def transfer(self, from_account_id: str, to_account_id: str, amount: float) -> None:

		from_account = self.__get_account(from_account_id)

		to_account = self.__get_account(to_account_id)

		from_account.withdraw(amount)
		to_account.deposit(amount)