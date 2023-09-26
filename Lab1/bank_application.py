from bank_user import BankUser 


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

    def exit(self,):
        print("Exit application")
        return exit()