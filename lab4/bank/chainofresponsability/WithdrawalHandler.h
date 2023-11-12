#pragma once
#include <iostream>
#include <vector>
#include <string>
using namespace std;


// Handler interface for Chain of Responsibility
class WithdrawalHandler {
protected:
    WithdrawalHandler* successor;

public:
    virtual void handleWithdrawal(double amount, double& balance) = 0;

    void setSuccessor(WithdrawalHandler* successor) {
        this->successor = successor;
    }
};
