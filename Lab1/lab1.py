from abc import ABC, abstractmethod

# Abstract Base Class for Account
class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def get_account_type(self):
        pass

# User interface remains unchanged
class User(ABC):
    @abstractmethod
    def create_account(self):
        pass

# Implementation of User
class BankUser(User):
    def __init__(self, username):
        self.username = username
        self.accounts = []

    def create_account(self):
        account = BankAccount()
        self.accounts.append(account)
        return account

# Implementation of Account
class BankAccount(Account):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def get_account_type(self):
        return "Savings"  # Example implementation, you can customize this

# Application Logic
class BankApplication:
    def __init__(self):
        self.users = []

    def create_user(self, username):
        user = BankUser(username)
        self.users.append(user)
        return user

    def login(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

def main():
    bank = BankApplication()

    while True:
        print("\n1. Create User")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter username: ")
            bank.create_user(username)
            print(f"User '{username}' created successfully!")

        elif choice == "2":
            username = input("Enter username: ")
            user = bank.login(username)
            if user:
                while True:
                    print("\n1. Create Account")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Check Balance")
                    print("5. Get Account Type")
                    print("6. Logout")
                    account_choice = input("Select an option: ")

                    if account_choice == "1":
                        user.create_account()
                        print("Account created successfully!")

                    elif account_choice == "2":
                        account = user.accounts[-1]
                        amount = float(input("Enter the amount to deposit: "))
                        account.deposit(amount)
                        print(f"Deposited {amount} into account. New balance: {account.get_balance()}")

                    elif account_choice == "3":
                        account = user.accounts[-1]
                        amount = float(input("Enter the amount to withdraw: "))
                        account.withdraw(amount)
                        print(f"Withdrew {amount} from account. New balance: {account.get_balance()}")

                    elif account_choice == "4":
                        account = user.accounts[-1]
                        print(f"Account balance: {account.get_balance()}")

                    elif account_choice == "5":
                        account = user.accounts[-1]
                        print(f"Account type: {account.get_account_type()}")

                    elif account_choice == "6":
                        break

        elif choice == "3":
            break

if __name__ == "__main__":
    main()
