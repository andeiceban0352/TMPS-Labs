#pragma once
#include <iostream>
using namespace std;

class BankAccount  {
private:
    double balance;

public:
    BankAccount(double initialBalance) : balance(initialBalance) {}

    double getBalance() const {
        return balance;
    }

    bool withdraw(double amount) {
        if (amount > balance) {
            cout << "Insufficient balance." << endl;
            return false;
        }
        balance -= amount;
        cout << "Withdrawal successful. Current balance: " << balance << endl;
        return true;
    }

    void deposit(double amount) {
        balance += amount;
        cout << "Deposit successful. Current balance: " << balance << endl;
    }
};