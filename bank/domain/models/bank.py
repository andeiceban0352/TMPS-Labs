
from abc import ABC, abstractmethod

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
