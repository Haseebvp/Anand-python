class Bankaccount:
	def __init__(self):
		self.balance=0
	def deposit(self,amount):
		self.balance+=amount
		return self.balance
	def withdraw(self,amount):
		self.balance-=amount
		return self.balance
a=Bankaccount()
b=Bankaccount()
print a.deposit(100)
print b.deposit(500)
print b.withdraw(400)
print a.withdraw(100)

