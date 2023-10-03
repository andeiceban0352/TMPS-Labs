# from bank.domain.models.bank import Bank
# from bank.domain.factory.account_factory import AccountPool , SavingsAccount
# from bank.domain.factory.account_factory import CheckingAccount , LoanAccount
# from bank.domain.factory.account_factory import ConcreteAccountBuilder
# from bank.domain.factory.bank_factory import BankManager
# from bank.domain.factory.transaction_factory import TransferTransaction, TransactionProcessor
# from bank.domain.factory.customer_factory import VIPCustomer, RegularCustomer

from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_id, owner_name, balance=0):
        self._account_id = account_id
        self._owner_name = owner_name
        self._balance = balance

    @property
    def account_id(self):
        return self._account_id

    @property
    def owner_name(self):
        return self._owner_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        self._balance = amount

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

class ConcreteAccount(Account):
    def __init__(self, account_id, owner_name, balance=0):
        super().__init__(account_id, owner_name, balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

class AccountBuilder(ABC):
    def __init__(self):
        self.account_id = None
        self.owner_name = None
        self.balance = 0

    def set_account_id(self, account_id):
        self.account_id = account_id
        return self

    def set_owner_name(self, owner_name):
        self.owner_name = owner_name
        return self

    def set_balance(self, balance):
        self.balance = balance
        return self

    @abstractmethod
    def build(self):
        pass

class ConcreteAccountBuilder(AccountBuilder):
    def build(self):
        return ConcreteAccount(self.account_id, self.owner_name, self.balance)


class AccountPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class SavingsAccount(AccountPrototype):
    def __init__(self):
        self._account_id = None
        self._owner_name = None
        self._balance = 0

    def set_account_id(self, account_id):
        self._account_id = account_id

    def set_owner_name(self, owner_name):
        self._owner_name = owner_name

    def clone(self):
        new_account = SavingsAccount()
        new_account.set_account_id(self._account_id)
        new_account.set_owner_name(self._owner_name)
        new_account.balance = self._balance
        return new_account

class CheckingAccount(AccountPrototype):
    def __init__(self):
        self._account_id = None
        self._owner_name = None
        self._balance = 0

    def set_account_id(self, account_id):
        self._account_id = account_id

    def set_owner_name(self, owner_name):
        self._owner_name = owner_name

    def clone(self):
        new_account = CheckingAccount()
        new_account.set_account_id(self._account_id)
        new_account.set_owner_name(self._owner_name)
        new_account.balance = self._balance
        return new_account

class LoanAccount(AccountPrototype):
    def __init__(self):
        self._account_id = None
        self._owner_name = None
        self._balance = 0

    def set_account_id(self, account_id):
        self._account_id = account_id

    def set_owner_name(self, owner_name):
        self._owner_name = owner_name

    def clone(self):
        new_account = LoanAccount()
        new_account.set_account_id(self._account_id)
        new_account.set_owner_name(self._owner_name)
        new_account.balance = self._balance
        return new_account

    @property
    def owner_name(self):
        return self._owner_name
    
        
class AccountPool:
    def __init__(self):
        self._accounts = []

    def create_account(self, account_prototype):
        account = account_prototype.clone()
        self._accounts.append(account)
        return account

    def get_account(self):
        if self._accounts:
            return self._accounts.pop()
        else:
            return None



class BankManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer


class Customer(ABC):
    def __init__(self, customer_id, name, accounts):
        self.customer_id = customer_id
        self.name = name
        self.accounts = accounts

    @abstractmethod
    def add_account(self, account):
        pass

class RegularCustomer(Customer):
    def add_account(self, account):
        self.accounts.append(account)

class VIPCustomer(Customer):
    def __init__(self, customer_id, name, accounts, vip_points=0):
        super().__init__(customer_id, name, accounts)
        self._vip_points = vip_points

    @property
    def vip_points(self):
        return self._vip_points

    def add_account(self, account):
        self.accounts.append(account)

    def earn_vip_points(self, points):
        self._vip_points += points




class Transaction(ABC):
    def __init__(self, source_account_id, destination_account_id, amount):
        self.source_account_id = source_account_id
        self.destination_account_id = destination_account_id
        self.amount = amount

    @abstractmethod
    def execute(self):
        pass

class TransactionProcessor:
    @staticmethod
    def process_transaction(transaction, bank):
        source_account = bank.get_account_by_id(transaction.source_account_id)
        destination_account = bank.get_account_by_id(transaction.destination_account_id)

        if source_account and destination_account:
            if source_account.balance >= transaction.amount:
                source_account.balance -= transaction.amount
                destination_account.balance += transaction.amount
                return True
        return False


class TransferTransaction(Transaction):
    def __init__(self, source_account_id, destination_account_id, amount):
        self.source_account_id = source_account_id
        self.destination_account_id = destination_account_id
        self.amount = amount

    def execute(self, bank):
        source_account = bank.get_account_by_id(self.source_account_id)
        destination_account = bank.get_account_by_id(self.destination_account_id)

        if source_account and destination_account:
            if source_account.balance >= self.amount:
                source_account.balance -= self.amount
                destination_account.balance += self.amount
                return True
        return False
    



class Bank(ABC):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Bank, cls).__new__(cls)
            cls._instance.accounts = []
        return cls._instance

    def add_account(self, account):
        self.accounts.append(account)

    def get_account_by_id(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None

def main():
    bank = Bank()
    account_pool = AccountPool()
    bank_manager = BankManager()

    while True:
        print("\nBank Application Menu:")
        print("1. Create Account")
        print("2. Make Transaction")
        print("3. Withdraw Money")
        print("4. Deposit Money")
        print("5. Check Account Balance")
        print("6. Create VIP Customer")
        print("7. Create Regular Customer")
        print("8. Exit")


        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAccount Types:")
            print("1. Savings Account")
            print("2. Checking Account")
            print("3. Loan Account")

            account_choice = input("Enter the account type (1/2/3): ")
            account_type = None

            if account_choice == "1":
                account_type = SavingsAccount()
            elif account_choice == "2":
                account_type = CheckingAccount()
            elif account_choice == "3":
                account_type = LoanAccount()
            else:
                print("Invalid account type choice.")
                continue

            account_id = input("Enter account ID: ")
            owner_name = input("Enter owner name: ")
            balance = float(input("Enter initial balance: "))

            account_builder = ConcreteAccountBuilder()
            account = account_builder.set_account_id(account_id).set_owner_name(owner_name).set_balance(balance).build()

            bank.add_account(account)
            account_pool.create_account(account_type.clone())

            print(f"Account created successfully: {account.owner_name}")

        elif choice == "2":
            source_account_id = input("Enter source account ID: ")
            destination_account_id = input("Enter destination account ID: ")
            amount = float(input("Enter transaction amount: "))

            transaction = TransferTransaction(source_account_id, destination_account_id, amount)
            success = TransactionProcessor.process_transaction(transaction, bank)

            if success:
                print("Transaction successful")
            else:
                print("Transaction failed")

        elif choice == "3":
            account_id = input("Enter account ID for withdrawal: ")
            amount = float(input("Enter withdrawal amount: "))
            
            account = bank.get_account_by_id(account_id)
            if account:
                if account:
                    account.withdraw(amount)
                    print("Withdrawal successful")
                else:
                    print("Insufficient funds for withdrawal")
            else:
                print("Account not found")

        elif choice == "4":
            account_id = input("Enter account ID for deposit: ")
            amount = float(input("Enter deposit amount: "))
            
            account = bank.get_account_by_id(account_id)
            if account:
                account.deposit(amount)
            else:
                print("Account not found")

        elif choice == "5":
            account_id = input("Enter account ID to check balance: ")
            account = bank.get_account_by_id(account_id)
            if account:
                print(f"Account balance for {account.owner_name}: ${account.balance:.2f}")
            else:
                print("Account not found")

        elif choice == "6":
            customer_id = input("Enter VIP customer ID: ")
            customer_name = input("Enter VIP customer name: ")
            vip_customer = VIPCustomer(customer_id, customer_name, [])
            bank_manager.add_customer(vip_customer)
            print(f"VIP Customer created successfully: {vip_customer.name}")

        elif choice == "7":
            customer_id = input("Enter Regular customer ID: ")
            customer_name = input("Enter Regular customer name: ")
            regular_customer = RegularCustomer(customer_id, customer_name, [])
            bank_manager.add_customer(regular_customer)
            print(f"Regular Customer created successfully: {regular_customer.name}")

        elif choice == "8":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

main()