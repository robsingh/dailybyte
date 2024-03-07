"""
Write a context manager to roll back a transaction on the given Account class.

There are two special (aka dunder) methods you need to define to create a context manager.

The purpose of the context manager is to roll back any transaction that will make the balance go below 0 (debt != cool). 

"""
class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    

class TransactionRollback:
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
        self.initial_balance = account.balance

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.account.balance < 0:
            self.account.balance = self.initial_balance
            print("Transaction rolled back!!")

        
account = Account(100)
print("Initial Balance: ", account.balance)

with TransactionRollback(account, 150): #amount considered for withdrawal
    account.withdraw(150) #amount attempted for withdrawal

print("Final Balance: ", account.balance)