class ATM:
    def __init__(self):
        self.balance = 0.0

    def check_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount:.2f} successfully.")
        else:
            print("Insufficient funds or invalid amount.")

    def display_account_details(self):
        print(f"--- Account Details ---\nBalance: ${self.balance:.2f}")

if __name__ == "__main__":
    atm = ATM()
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Details\n5. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            atm.deposit(float(input("Enter deposit amount: ")))
        elif choice == '3':
            atm.withdraw(float(input("Enter withdrawal amount: ")))
        elif choice == '4':
            atm.display_account_details()
        elif choice == '5':
            break
        else:
            print("Invalid choice, try again.")
