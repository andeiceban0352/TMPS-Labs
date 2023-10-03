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