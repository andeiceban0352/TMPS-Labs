#pragma once
#include <iostream>
using namespace std;


class Bank {
private:
    static Bank* instance;

    map<string, BankAccount*> accounts;
    queue<BankAccount*> accountPool;  // Pool of BankAccount objects

    // Private constructor to prevent direct instantiation
    Bank() {}

public:
    // singleton principle, only one instance of bank will be in this app
    static Bank& getInstance() {
        static Bank instance; // Guaranteed to be destroyed.
                            // Instantiated on first use.
        return instance;
    }


    // Object Pooling
    BankAccount* acquireAccount(double initialBalance) {
        if (accountPool.empty()) {
            return new BankAccount(initialBalance);
        } else {
            BankAccount* account = accountPool.front();
            accountPool.pop();
            account->deposit(initialBalance);  // Reset the balance
            return account;
        }
    }

    void releaseAccount(BankAccount* account) {
        accountPool.push(account);  // Release the account back to the pool
    }

    void createAccount(const string& accountNumber, BankAccount* account) {
        accounts[accountNumber] = account;
        cout << "Account created successfully." << endl;
    }

    // void createAccount(const string& accountNumber, double initialBalance) {
    //     accounts[accountNumber] = new BankAccount(initialBalance);
    //     cout << "Account created successfully." << endl;
    // }

    bool withdrawMoney(const string& accountNumber, double amount) {
        if (accounts.find(accountNumber) != accounts.end()) {
            return accounts[accountNumber]->withdraw(amount);
        } else {
            cout << "Account not found." << endl;
            return false;
        }
    }

    void depositMoney(const string& accountNumber, double amount) {
        if (accounts.find(accountNumber) != accounts.end()) {
            accounts[accountNumber]->deposit(amount);
        } else {
            cout << "Account not found." << endl;
        }
    }

    double checkAccountBalance(const string& accountNumber) {
        if (accounts.find(accountNumber) != accounts.end()) {
            return accounts[accountNumber]->getBalance();
        } else {
            cout << "Account not found." << endl;
            return 0;
        }
    }
};