class Bank:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit {amount}. {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal {amount}. {self.balance}")
        else:
            print("Error")

account = Bank("Bank", 1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(800)
