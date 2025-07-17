# All property decorators together, full Example: @property, @setter, and @deleter

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        print("Getting balance...")
        return self._balance

    @balance.setter
    def balance(self, amount):
        print("Setting balance...")
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount

    @balance.deleter
    def balance(self):
        print("Deleting balance...")
        self._balance = 0


acc = BankAccount(10000)
print(acc.balance)

acc.balance = 5000
print(acc.balance)

del acc.balance
print(acc.balance)