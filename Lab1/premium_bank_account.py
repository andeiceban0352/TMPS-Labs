from account import Account 

class PremiumBankAccount(Account):
    def __init__(self):
        self.balance = 0

    # more than 1 000 000 €
    def deposit(self, amount):  
        self.balance += amount

    # more than 1 000 000 €
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def get_account_type(self):
            print("Premium Bank Account")
            print('''
                    Enhanced features, such as higher interest rates on deposits.
                    Premium debit or credit cards with added benefits like travel insurance, purchase protection, and rewards programs.
                    Discounts on bank services such as wire transfers, safe deposit boxes, or cashier's checks.
                    Dont have limit for withdraws and deposit
                    ''')
