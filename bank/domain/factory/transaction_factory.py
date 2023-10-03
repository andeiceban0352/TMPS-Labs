from abc import ABC, abstractmethod

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