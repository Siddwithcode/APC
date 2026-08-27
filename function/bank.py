balance = 0
transactions = []


def deposit(amount):
    global balance

    balance = balance + amount
    transactions.append("Deposited: " + str(amount))

    print("Amount deposited successfully")


def withdraw(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        transactions.append("Withdrawn: " + str(amount))
        print("Amount withdrawn successfully")
    else:
        print("Insufficient balance")


def balance_enquiry():
    print("Current Balance =", balance)


def transaction_history():
    print("Transaction History:")

    for transaction in transactions:
        print(transaction)


deposit(5000)
withdraw(1000)
deposit(2000)

balance_enquiry()
transaction_history()