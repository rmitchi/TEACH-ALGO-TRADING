class Portal:

	banks = {}

	def get_account(self, account_id: str):
		bank_code = account_id.split('_')[0]
		return self.banks[bank_code].accounts.get(account_id)

	def add_bank(self, bank):

		bank.portal = self
		self.banks[bank.code] = bank

	