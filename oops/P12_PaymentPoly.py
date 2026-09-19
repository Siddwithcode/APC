class Payment:
    def make_payment(self): pass
class UPIPayment(Payment):
    def make_payment(self): print("Paid via UPI")
class CardPayment(Payment):
    def make_payment(self): print("Paid via Card")
class WalletPayment(Payment):
    def make_payment(self): print("Paid via Wallet")
def process(payment): payment.make_payment()
process(UPIPayment())
