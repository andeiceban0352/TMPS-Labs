#pragma once
#include <iostream>
using namespace std;


// Concrete implementation of Bank Application Menu
class BankApplicationMenu : public Account, public VIPCustomer, public RegularCustomer {
public:

    BankAccount* acquireBankAccount(double initialBalance) {
        return Bank::getInstance().acquireAccount(initialBalance);
    }

    void releaseBankAccount(BankAccount* account) {
        Bank::getInstance().releaseAccount(account);
    }

    Customer createCustomer() {
        CustomerBuilder customerBuilder;
        string name, address;
        int age;
        string isVIP;

        cout << "Enter customer's name: ";
        cin >> name;
        cout << "Enter customer's age: ";
        cin >> age;
        cout << "Enter customer's address: ";
        cin >> address;
        cout << "Is the customer a VIP? (1 for Yes, 0 for No): ";
        cin >> isVIP;

        return customerBuilder.setName(name).setAge(age).setAddress(address).setIsVIP(isVIP).build();
    }
    void createAccount() override {
        cout << "Enter the account name: ";
        cin >> accountName;
        cout << "Enter the account number: ";
        cin >> accountNumber;
        cout << "Account created successfully." << endl;
    }

    void makeTransaction() override {
        Transaction transaction;
        string sender, receiver;
        double amount;

        cout << "Enter sender's name: ";
        cin >> sender;
        cout << "Enter receiver's name: ";
        cin >> receiver;
        cout << "Enter the amount: ";
        cin >> amount;

        transaction.performTransaction(sender, receiver, amount);
    }

    void withdrawMoney() override {
        BankAccount account(1000); // Assuming initial balance is 1000
        double amount;
        cout << "Enter amount to withdraw: ";
        cin >> amount;
        account.withdraw(amount);
    }

    void depositMoney() override {
        BankAccount account(1000); // Assuming initial balance is 1000
        double amount;
        cout << "Enter amount to deposit: ";
        cin >> amount;
        account.deposit(amount);
    }

    void checkAccountBalance() override {
        BankAccount account(1000); // Assuming initial balance is 1000
        cout << "Current account balance: " << account.getBalance() << endl;
    }

    void createVIPCustomer() override {
        string name, address;
        int age;
        string isVIP = "Yes";

        cout << "Enter VIP customer's name: ";
        cin >> name;
        cout << "Enter VIP customer's age: ";
        cin >> age;
        cout << "Enter VIP customer's address: ";
        cin >> address;

        Customer vipCustomer(name, age, address, isVIP);
        cout << "VIP Customer created successfully. Details:" << endl;
        vipCustomer.displayCustomerDetails();
    }

    void createRegularCustomer() override {
        string name, address;
        int age;
        string isVIP = "No";

        cout << "Enter regular customer's name: ";
        cin >> name;
        cout << "Enter regular customer's age: ";
        cin >> age;
        cout << "Enter regular customer's address: ";
        cin >> address;

        Customer regularCustomer(name, age, address, isVIP);
        cout << "Regular Customer created successfully. Details:" << endl;
        regularCustomer.displayCustomerDetails();
    }
};
