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
            type_account = input("Enter type account : premium / standart : ")
           
            username = input("Enter username: ")
            surname = input("Enter surname: ")
            password = input("Enter password: ")
            phone_number = input("Enter phone number: ")
            idnp = input("Enter ID number: ")
            location = input("Enter location: (MD / RO )")

            user = bank.create_user(username)
            user.set_name(username)
            user.set_surname(surname)
            user.set_password(password)
            user.set_phone_number(phone_number)
            user.set_idnp(idnp)
            user.set_location(location)

            if(type_account == 'standart'):
                user.create_account()
            else:
                user.create_premium_account()

            print(f"User '{username}' created successfully!")

        elif choice == "2":
            username = input("Enter username to acces account: ")
            user = bank.login(username)
            if user:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Profile Info")
                    print("5. Account Type")
                    print("6. Logout")
                    account_choice = input("Select an option: ")

                    if account_choice == "1":
                        account = user.accounts[-1]
                        amount = float(input("Enter the amount to deposit: "))
                        account.deposit(amount)
                        print(f"Deposited {amount} into account. New balance: {account.get_balance()}")

                    elif account_choice == "2":
                        account = user.accounts[-1]
                        amount = float(input("Enter the amount to withdraw: "))
                        account.withdraw(amount)
                        print(f"Withdrew {amount} from account. New balance: {account.get_balance()}")

                    elif account_choice == "3":
                        account = user.accounts[-1]
                        print(f"Account balance: {account.get_balance()}")

                    elif account_choice == "4":
                        user.profile_info()

                    elif account_choice == "5":
                        account = user.accounts[-1]
                        account.get_account_type()

                    elif account_choice == "6":
                        break

        elif choice == "3":
            bank.exit()

if __name__ == "__main__":
    main()