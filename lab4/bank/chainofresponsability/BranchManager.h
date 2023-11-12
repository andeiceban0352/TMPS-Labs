#pragma once
#include <iostream>
#include <vector>
#include <string>
using namespace std;



// Concrete Handler - BranchManager
class BranchManager : public WithdrawalHandler {
public:
    void handleWithdrawal(double amount, double& balance) override {
        if (amount <= 5000) {
            balance -= amount;
            std::cout << "Branch Manager handled withdrawal of $" << amount << std::endl;
        } else if (successor != nullptr) {
            successor->handleWithdrawal(amount, balance);
        }
    }
};