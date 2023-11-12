#pragma once
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Concrete Handler - BankEmployee
class BankEmployee : public WithdrawalHandler {
public:
    void handleWithdrawal(double amount, double& balance) override {
        if (amount <= 1000) {
            balance -= amount;
            std::cout << "Bank Employee handled withdrawal of $" << amount << std::endl;
        } else if (successor != nullptr) {
            successor->handleWithdrawal(amount, balance);
        }
    }
};