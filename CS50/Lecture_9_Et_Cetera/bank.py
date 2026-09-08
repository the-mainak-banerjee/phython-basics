class Account():
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposite(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount


def main():
    account = Account()
    print("Balance: ", account.balance)
    account.deposite(100)
    print("Balance: ", account.balance)
    account.withdraw(50)
    print("Balance: ", account.balance)


if __name__ == "__main__":
    main()