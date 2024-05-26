class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount

    def print(self):
        print(f"Current balance: ${self.balance}, Interest rate: {self.interest_rate}%")
       

# Create an instance of BankAccount
bank_account = BankAccount("123456789", "John Doe")
bank_account.deposit(1000)
bank_account.withdraw(500)
print("Final balance:", bank_account.get_balance())

# Create an instance of SavingsAccount
savings_account = SavingsAccount("987654321", "Jane Smith", interest_rate=2.5)
savings_account.deposit(5000)
savings_account.apply_interest()
savings_account.print()