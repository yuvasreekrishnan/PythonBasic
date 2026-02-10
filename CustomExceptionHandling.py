class InsufficientBalance(Exception):
    balance = None
    amount = None
    message = None

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Your balance is {balance} and you are trying to withdraw {amount}"
        super().__init__(self.message)


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalance(balance, amount)
    else:
        print("withdrawal successful")
try:   
    balance = 1000
    amount = int(input("enter the amount to withdraw :"))
    new_balance = balance - amount
    withdraw(balance, amount)
except InsufficientBalance as e:
    print(e.message)