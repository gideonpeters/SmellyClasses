class BankAccount:
    INVALID_AMOUNT_ERROR = "Invalid amount"

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError(self.INVALID_AMOUNT_ERROR)
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError(self.INVALID_AMOUNT_ERROR)
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance

    def view_balance(self):
        return self.balance

    def transfer(self, recipient, amount):
        if amount < 0:
            raise ValueError(self.INVALID_AMOUNT_ERROR)
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        recipient.balance += amount