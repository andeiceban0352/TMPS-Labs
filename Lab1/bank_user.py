
from user import User 
from bank_account import BankAccount 
from premium_bank_account import PremiumBankAccount 


class BankUser(User):
    def __init__(self, username):
        self.username = username
        self.accounts = []
        self.phone_number = None
        self.idnp = None
        self.name = None
        self.surname = None
        self.location = None

    def create_account(self):
        account = BankAccount()
        self.accounts.append(account)
        return account

    def create_premium_account(self):
        account = PremiumBankAccount()
        self.accounts.append(account)
        return account

    def set_name(self, name):
        self.name = name
        
    def set_surname(self, surname):
        self.surname = surname

    def set_password(self, password):
        self.password = password
        
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_idnp(self, idnp):
        self.idnp = idnp

    def set_location(self, location):
        self.location = location

    def profile_info(self):
        print("\n Profile info:")
        print(f"Username: {self.username}")
        print(f"Surname: {self.surname}")
        print(f"Phone Number: {self.phone_number}")
        print(f"IDNP: {self.idnp}")
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
