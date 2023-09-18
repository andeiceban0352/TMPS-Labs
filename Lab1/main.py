from bank_user import BankUser 
from bank_application import BankApplication 
    


def main():
    bank = BankApplication()

    while True:
        print("\n1. Create User")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter username: ")
            phone_number = input("Enter phone number: ")
            idnp = input("Enter ID number: ")
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            location = input("Enter location: ")

            user = bank.create_user(username)
            user.set_phone_number(phone_number)
            user.set_idnp(idnp)
            user.set_name(name)
            user.set_surname(surname)
            user.set_location(location)

            print(f"User '{username}' created successfully!")

        elif choice == "2":
            username = input("Enter username: ")
            user = bank.login(username)
            if user:
                while True:
                    print("\n1. Create Account")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Check Balance")
                    print("5. Profile Info")
                    print("6. Account Type")
                    print("7. Logout")
                    account_choice = input("Select an option: ")

                    if account_choice == "1":
                        user.create_account()
                        print("Account created successfully!")

                    elif account_choice == "2":
                        account = user.accounts[-1]
                        amount = float(input("Enter the amount to deposit: "))
                        account.deposit(amount)
                        print(f"Deposited {amount} into account. New balance: {account.get_balance()}")

                    elif account_choice == "3":
                        account = user.accounts[-1]
                        amount = float(input("Enter the amount to withdraw: "))
                        account.withdraw(amount)
                        print(f"Withdrew {amount} from account. New balance: {account.get_balance()}")

                    elif account_choice == "4":
                        account = user.accounts[-1]
                        print(f"Account balance: {account.get_balance()}")

                    elif account_choice == "5":
                        user.profile_info()

                    elif account_choice == "6":
                        account = user.accounts[-1]
                        account.get_account_type()

                    elif account_choice == "7":
                        break

        elif choice == "3":
            break

if __name__ == "__main__":
    main()
