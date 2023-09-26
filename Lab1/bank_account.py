from account import Account 

class BankAccount(Account):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if(amount > 10000):
            self.balance = 0
            print("You can not deposit more than 10000€, please make a premium account")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def get_account_type(self):
            print("Standart Bank Account")
            print('''
                    Basic features for day-to-day banking, such as deposits, withdrawals, and electronic payments.
                    Typically comes with a basic debit card.
                    Minimal or no interest on the account balance.
                    Have limit for withdraws and deposit no more than 10000€
                    ''')