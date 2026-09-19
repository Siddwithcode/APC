class BankAccount:
    def __init__(self, acc_no, balance): self.acc_no, self.balance = acc_no, balance
class SavingsAccount(BankAccount):
    def __init__(self, acc_no, balance, interest_rate):
        super().__init__(acc_no, balance)
        self.interest_rate = interest_rate
class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, acc_no, balance, int_rate, bonus):
        super().__init__(acc_no, balance, int_rate)
        self.bonus = bonus
    def calc_interest(self):
        return (self.balance * self.interest_rate / 100) + self.bonus
p = PremiumSavingsAccount(123, 1000, 5, 50)
print(f"Interest: {p.calc_interest()}")
