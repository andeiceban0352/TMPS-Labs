#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include "./bank/domain/models/transaction.h"
#include "./bank/domain/models/accout.h"
#include "./bank/domain/models/customer.h"
#include "./bank/domain/models/bankAccount.h"
#include "./bank/domain/models/bank.h"
#include "./bank/domain/builder/customerBuilder.h"
#include "./bank/domain/factory/accountFactory.h"
#include "./bank/client/bankApplicationMenu.h"

using namespace std;

// sudo g++ -std=c++14 main2.cpp -o a.out
// command to run


int main() {
    BankApplicationMenu bankApp;
    Bank& bank = Bank::getInstance();
    AccountFactory* factory = new BankAccountFactory(); // Create an instance of the BankAccountFactory

    int choice;
    string accountNumber;
    double initialBalance;
    do {
        cout << "\nBank Application Menu:" << endl;
        cout << "1. Create Account" << endl;
        cout << "2. Make Transaction" << endl;
        cout << "3. Withdraw Money" << endl;
        cout << "4. Deposit Money" << endl;
        cout << "5. Check Account Balance" << endl;
        cout << "6. Create VIP Customer" << endl;
        cout << "7. Create Regular Customer" << endl;
        cout << "8. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        string accountNumber;
        double amount;
        double balance;
        CustomerBuilder customerBuilder;
        Customer customer = customerBuilder.setName("").setAge(0).setAddress("").setIsVIP("").build();           
        BankAccount* account = bankApp.acquireBankAccount(1000); // Assuming initial balance is 1000
        BankAccount* newAccount;
        switch (choice) {
            case 1:
                cout << "Enter the account number: ";
                cin >> accountNumber;
                cout << "Enter the initial balance: ";
                cin >> initialBalance;
                // Use the factory to create an account
                newAccount = factory->createAccount(initialBalance);
                // Add the new account to the bank's accounts
                bank.createAccount(accountNumber, newAccount);
                break;
                // cout << "Enter the account number: ";
                // cin >> accountNumber;
                // cout << "Enter the initial balance: ";
                // cin >> initialBalance;
                // bank.createAccount(accountNumber, initialBalance);
                // bankApp.createAccount();
                break;
            case 2:
                bankApp.makeTransaction();
                break;
            case 3:
                cout << "Enter account number: ";
                cin >> accountNumber;
                cout << "Enter amount to withdraw: ";
                cin >> amount;

                account->withdraw(amount);
                bankApp.releaseBankAccount(account);
                break;
                
                // bank.withdrawMoney(accountNumber, amount);
                // break;
                // bankApp.withdrawMoney();
                break;
            case 4:
                cout << "Enter account number: ";
                cin >> accountNumber;
                cout << "Enter amount to deposit: ";
                cin >> amount;
                bank.depositMoney(accountNumber, amount);
                break;
            case 5:
                cout << "Enter account number: ";
                cin >> accountNumber;
                balance = bank.checkAccountBalance(accountNumber);
                if (balance != 0) {
                    cout << "Current account balance: " << balance << endl;
                }
                break;
            case 6:
                // bankApp.createVIPCustomer();
                
                customer = bankApp.createCustomer();
                cout << "Customer created successfully. Details:" << endl;
                customer.displayCustomerDetails();
                break;
                
            case 7:
                bankApp.createRegularCustomer();
                break;
            case 8:
                cout << "Exiting..." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 8);

    return 0;
}
