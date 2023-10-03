from abc import ABC, abstractmethod
from bank.domain.models.account import Account

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