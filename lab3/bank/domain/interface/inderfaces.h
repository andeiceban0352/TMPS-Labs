#pragma once
#include <iostream>
using namespace std;

// Component Interface
class BankInterface {
public:
    virtual void createAccount(const string &accountNumber, BankAccount *account) = 0;
    virtual void depositMoney(const string &accountNumber, double amount) = 0;
    virtual double checkAccountBalance(const string &accountNumber) = 0;
};