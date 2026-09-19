from abc import ABC, abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def deposit(self): pass
    @abstractmethod
    def withdraw(self): pass
class SavingsAccount(BankAccount):
    def deposit(self): print("Savings deposit")
    def withdraw(self): print("Savings withdraw")
s = SavingsAccount()
s.deposit()
