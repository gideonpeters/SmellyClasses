class BankAccount:
    def __init__(self):
        self.balance = 0

    def _validate_amount(self, amount):
        if amount < 0:
            raise ValueError("Invalid amount")

    def deposit(self, amount):
        self._validate_amount(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self._validate_amount(amount)
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance

    def view_balance(self):
        return self.balance

    def transfer(self, recipient, amount):
        self._validate_amount(amount)
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        recipient.balance += amount