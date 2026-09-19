class BankAccount:
    def calculate_interest(self): pass
class SavingsAccount(BankAccount):
    def calculate_interest(self): print("Savings: 4%")
class CurrentAccount(BankAccount):
    def calculate_interest(self): print("Current: 0%")
class FixedDepositAccount(BankAccount):
    def calculate_interest(self): print("FD: 7%")
for b in [SavingsAccount(), CurrentAccount(), FixedDepositAccount()]: b.calculate_interest()
