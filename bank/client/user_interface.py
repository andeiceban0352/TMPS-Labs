from bank.domain.models.bank import Bank
from bank.domain.factory.account_factory import AccountPool , SavingsAccount
from bank.domain.factory.account_factory import CheckingAccount , LoanAccount
from bank.domain.factory.account_factory import ConcreteAccountBuilder
from bank.domain.factory.bank_factory import BankManager
from bank.domain.factory.transaction_factory import TransferTransaction, TransactionProcessor
from bank.domain.factory.customer_factory import VIPCustomer, RegularCustomer

def main():
    bank = Bank()
    account_pool = AccountPool()
    bank_manager = BankManager()

    while True:
        print("\nBank Application Menu:")
        print("1. Create Account")
        print("2. Make Transaction")
        print("3. Withdraw Money")
        print("4. Deposit Money")
        print("5. Check Account Balance")
        print("6. Create VIP Customer")
        print("7. Create Regular Customer")
        print("8. Exit")


        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAccount Types:")
            print("1. Savings Account")
            print("2. Checking Account")
            print("3. Loan Account")

            account_choice = input("Enter the account type (1/2/3): ")
            account_type = None

            if account_choice == "1":
                account_type = SavingsAccount()
            elif account_choice == "2":
                account_type = CheckingAccount()
            elif account_choice == "3":
                account_type = LoanAccount()
            else:
                print("Invalid account type choice.")
                continue

            account_id = input("Enter account ID: ")
            owner_name = input("Enter owner name: ")
            balance = float(input("Enter initial balance: "))

            account_builder = ConcreteAccountBuilder()
            account = account_builder.set_account_id(account_id).set_owner_name(owner_name).set_balance(balance).build()

            bank.add_account(account)
            account_pool.create_account(account_type.clone())

            print(f"Account created successfully: {account.owner_name}")

        elif choice == "2":
            source_account_id = input("Enter source account ID: ")
            destination_account_id = input("Enter destination account ID: ")
            amount = float(input("Enter transaction amount: "))

            transaction = TransferTransaction(source_account_id, destination_account_id, amount)
            success = TransactionProcessor.process_transaction(transaction, bank)

            if success:
                print("Transaction successful")
            else:
                print("Transaction failed")

        elif choice == "3":
            account_id = input("Enter account ID for withdrawal: ")
            amount = float(input("Enter withdrawal amount: "))
            
            account = bank.get_account_by_id(account_id)
            if account:
                if account:
                    account.withdraw(amount)
                    print("Withdrawal successful")
                else:
                    print("Insufficient funds for withdrawal")
            else:
                print("Account not found")

        elif choice == "4":
            account_id = input("Enter account ID for deposit: ")
            amount = float(input("Enter deposit amount: "))
            
            account = bank.get_account_by_id(account_id)
            if account:
                account.deposit(amount)
            else:
                print("Account not found")

        elif choice == "5":
            account_id = input("Enter account ID to check balance: ")
            account = bank.get_account_by_id(account_id)
            if account:
                print(f"Account balance for {account.owner_name}: ${account.balance:.2f}")
            else:
                print("Account not found")

        elif choice == "6":
            customer_id = input("Enter VIP customer ID: ")
            customer_name = input("Enter VIP customer name: ")
            vip_customer = VIPCustomer(customer_id, customer_name, [])
            bank_manager.add_customer(vip_customer)
            print(f"VIP Customer created successfully: {vip_customer.name}")

        elif choice == "7":
            customer_id = input("Enter Regular customer ID: ")
            customer_name = input("Enter Regular customer name: ")
            regular_customer = RegularCustomer(customer_id, customer_name, [])
            bank_manager.add_customer(regular_customer)
            print(f"Regular Customer created successfully: {regular_customer.name}")

        elif choice == "8":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

main()