from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def create_account(self):
        pass
    
    @abstractmethod
    def set_name(self):
        pass

    @abstractmethod
    def set_surname(self):
        pass

    @abstractmethod
    def set_password(self):
        pass

    @abstractmethod
    def set_phone_number(self):
        pass

    @abstractmethod
    def set_name(self):
        pass

    @abstractmethod
    def set_location(self):
        pass

    @abstractmethod
    def profile_info(self):
        pass