#pragma once
#include <iostream>
using namespace std;

class BankInterface {
public:
    virtual void createAccount(const string& accountNumber, BankAccount* account) = 0;
    virtual void withdrawMoney(const string& accountNumber, double amount) = 0;
    virtual void depositMoney(const string& accountNumber, double amount) = 0;
    virtual double checkAccountBalance(const string& accountNumber) = 0;
};

// Create an adapter for the Bank class
class BankAdapter : public BankInterface {
private:
    Bank& bank;

public:
    BankAdapter(Bank& bank) : bank(bank) {}

    void createAccount(const string& accountNumber, BankAccount* account) override {
        bank.createAccount(accountNumber, account);
    }

    void withdrawMoney(const string& accountNumber, double amount) override {
        bank.withdrawMoney(accountNumber, amount);
    }

    void depositMoney(const string& accountNumber, double amount) override {
        bank.depositMoney(accountNumber, amount);
    }

    double checkAccountBalance(const string& accountNumber) override {
        return bank.checkAccountBalance(accountNumber);
    }
};