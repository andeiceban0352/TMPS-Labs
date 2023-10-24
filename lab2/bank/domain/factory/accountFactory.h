#pragma once
#include <iostream>
using namespace std;

// Abstract factory for creating accounts
class AccountFactory {
public:
    virtual BankAccount* createAccount(double initialBalance) = 0;
};

// Factory class for BankAccount
class BankAccountFactory : public AccountFactory {
public:
    BankAccount* createAccount(double initialBalance) override {
        return new BankAccount(initialBalance);
    }
};
