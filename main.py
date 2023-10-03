from bank.domain.models.bank import Bank
from bank.domain.factory.account_factory import AccountPool , SavingsAccount
from bank.domain.factory.account_factory import CheckingAccount , LoanAccount
from bank.domain.factory.account_factory import ConcreteAccountBuilder
from bank.domain.factory.bank_factory import BankManager
from bank.domain.factory.transaction_factory import TransferTransaction, TransactionProcessor
from bank.domain.factory.customer_factory import VIPCustomer, RegularCustomer

from abc import ABC, abstractmethod

# The Account class serves as an abstract base class  for defining the common structure and behavior of various types of bank accounts
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


#  is used to represent a concrete implementation of an account. It is a subclass of the abstract Account class and provides a specific implementation of a bank account.
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


# Builder Design Pattern -//////////////////////////////////////////////////////
# separate the construction of a complex object from its representation.
# AccountBuilder class represent the Builder pattern. 
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


# The ConcreteAccountBuilder class is responsible for creating instances of ConcreteAccount with various attributes, allowing you to build accounts with different configurations.
class ConcreteAccountBuilder(AccountBuilder):
    def build(self):
        return ConcreteAccount(self.account_id, self.owner_name, self.balance)



# Prototype Design Pattern - //////////////////////////////////////////////////////
# Prototype pattern is implemented with the AccountPrototype interface and its concrete implementations 
class AccountPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass



# Liskov Substitution Principle  allows for the substitution of derived account types for the base class (AccountPrototype) without affecting the correctness of the program.
# provide a clone method that creates a new instance by copying the existing object's attributes.
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


# provide a clone method that creates a new instance by copying the existing object's attributes.
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


# provide a clone method that creates a new instance by copying the existing object's attributes.
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
    

# Object Pooling Design Pattern - //////////////////////////////////////////////////////
#if instances of a class can be reused, you avoid creating instances of the class by reusing them.
#AccountPool class is an example of object pooling. It allows you to create and retrieve account objects from a pool of pre-created instances. 
# to== manage the object caching. A client with access to a Object pool can avoid creating a new Objects by simply asking the pool for one that has already been instantiated instead.       
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


# The BankManager class manage and keep track of customers who have accounts with the bank
# by adding customers and get id from them
class BankManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer


# The Customer class serves as an abstract base class for different types of customers and defines common attributes and methods
class Customer(ABC):
    def __init__(self, customer_id, name, accounts):
        self.customer_id = customer_id
        self.name = name
        self.accounts = accounts

    @abstractmethod
    def add_account(self, account):
        pass


# The RegularCustomer class  represents a regular customer in the banking application
class RegularCustomer(Customer):
    def add_account(self, account):
        self.accounts.append(account)

# The RegularCustomer class  represents a vip customer in the banking application

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


# The Transaction class serves as a blueprint for creating transaction objects that encapsulate details about a financial transaction.
class Transaction(ABC):
    def __init__(self, source_account_id, destination_account_id, amount):
        self.source_account_id = source_account_id
        self.destination_account_id = destination_account_id
        self.amount = amount

    @abstractmethod
    def execute(self):
        pass


# The TransactionProcessor class handles the execution transactions between different bank accounts
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


# The TransferTransaction class handles the transfer of funds between two accounts.
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
    

# Singleton Design Pattern - //////////////////////////////////////////////////////
# The Bank class is implemented as a Singleton, ensuring that there is only one instance of the bank throughout the application, using the new method to control the creation of instances.
# class Bank(ABC):
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(Bank, cls).__new__(cls)
#             cls._instance.accounts = []
#         return cls._instance

#     def add_account(self, account):
#         self.accounts.append(account)

#     def get_account_by_id(self, account_id):
#         for account in self.accounts:
#             if account.account_id == account_id:
#                 return account
#         return None


if __name__ == '__main__':
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
                if account.balance > amount:
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
