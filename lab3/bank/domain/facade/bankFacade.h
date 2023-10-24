#pragma once
#include <iostream>
using namespace std;

class BankFacade {
private:
    BankApplicationMenu bankApp;
    Bank& bank;

public:
    BankFacade() : bank(Bank::getInstance()) {}

    void createAccount(const string& accountNumber, double initialBalance) {
        BankAccount* newAccount = bank.acquireAccount(initialBalance);
        bank.createAccount(accountNumber, newAccount);
    }

    void makeTransaction() {
        bankApp.makeTransaction();
    }

    void withdrawMoney(const string& accountNumber, double amount) {
        bank.withdrawMoney(accountNumber, amount);
    }

    void depositMoney(const string& accountNumber, double amount) {
        bank.depositMoney(accountNumber, amount);
    }

    double checkAccountBalance(const string& accountNumber) {
        return bank.checkAccountBalance(accountNumber);
    }

    Customer createCustomer() {
        return bankApp.createCustomer();
    }

    void createVIPCustomer() {
        bankApp.createVIPCustomer();
    }

    void createRegularCustomer() {
        bankApp.createRegularCustomer();
    }
};
