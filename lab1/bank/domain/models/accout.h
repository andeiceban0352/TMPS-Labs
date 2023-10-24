#pragma once
#include <iostream>
using namespace std;

class Account {
public:
    string accountName;
    string accountNumber;
    virtual void createAccount() = 0;
    virtual void makeTransaction() = 0;
    virtual void withdrawMoney() = 0;
    virtual void depositMoney() = 0;
    virtual void checkAccountBalance() = 0;
};