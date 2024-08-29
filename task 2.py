class BankAccount:
def __init__(self, account_number):
self.__account_number = account_number
self.__balance = 0
def deposit(self, amount):
self.__balance += amount
def withdraw(self, amount):
if self.__balance >= amount:
self.__balance -= amount
else:
print("Insufficient funds")
def get_balance(self):
return self.__balance
account = BankAccount("12345")
account.deposit(1000)
account.withdraw(500)
print("Balance:", account.get_balance())
