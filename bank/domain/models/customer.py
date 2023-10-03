from abc import ABC, abstractmethod

class Customer(ABC):
    def __init__(self, customer_id, name, accounts):
        self.customer_id = customer_id
        self.name = name
        self.accounts = accounts

    @abstractmethod
    def add_account(self, account):
        pass