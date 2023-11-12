#pragma once
#include <iostream>
#include <vector>
#include <string>
using namespace std;



// Concrete Handler - HeadOffice
class HeadOffice : public WithdrawalHandler {
public:
    void handleWithdrawal(double amount, double& balance) override {
        // Head office can handle any withdrawal amount
        balance -= amount;
        std::cout << "Head Office handled withdrawal of $" << amount << std::endl;
    }
};