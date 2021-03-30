class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02)

    def make_deposit(self):
        self.account.deposit(300)
        print(self.account.balance)
        return self

    def make_withdrawal(self):
        self.account.withdraw(100)
        print(self.account.balance)
        return self

    def display_user_balance(self):
        print(f"Balance: {self.account.balance}")
        return self


class BankAccount:
    def __init__(self, int_rate):
        self.int_rate = int_rate
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
timmy = User("Timmy Lew", "timmy@python.com")

checking = BankAccount(0.01)
savings = BankAccount(0.05)

guido.make_deposit().make_withdrawal().display_user_balance()
