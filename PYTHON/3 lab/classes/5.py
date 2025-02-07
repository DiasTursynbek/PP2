class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit {amount}. New balance: {self.balance}")

    def withdraw(self, amount):    #withdraw() (снятие денег)
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawal {amount}. New balance: {self.balance}")



acc = BankAccount("Alice", 100000)
acc.deposit(5000)
acc.withdraw(2000)
acc.withdraw(5000)