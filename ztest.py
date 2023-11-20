from banking import Portal, Bank


portal = Portal()

bank1 = Bank(code="USCP", name="Cyprus National Bank")
portal.add_bank(bank1)

bank2 = Bank(code="JPS", name="Shinigami Bank of Japan")
portal.add_bank(bank2)

bank3 = Bank(code="INK", name="Kotak bank")
portal.add_bank(bank3)

a1 = bank1.create_account("Alex", "Saverin")
a2 = bank2.create_account("Aiden", "Pearce")
a3 = bank3.create_account("Janet", "Vanhautten")
a4 = bank1.create_account("Shirley", "Saverin")
a5 = bank2.create_account("Emma", "Watson")
a6 = bank3.create_account("Jason", "Vanhautten")

a1.deposit(10000)
a2.deposit(15000)
a3.deposit(20000)
a4.deposit(10000)
a5.deposit(1000)
a6.deposit(4000)

bank1.transfer(a1.id, a2.id, 3000)

print(a1.balance, a2.balance)