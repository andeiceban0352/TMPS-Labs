from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def create_account(self):
        pass

    @abstractmethod
    def profile_info(self):
        pass
