#pragma once
#include <iostream>
#include <vector>
#include <string>
using namespace std;



// Concrete Subject - BankAccount
class BankAccount : public Subject, public WithdrawalHandler {
private:
    double balance;
    std::vector<Observer*> observers;
    InterestCalculationStrategy* interestCalculationStrategy;

public:
    BankAccount(InterestCalculationStrategy* strategy)
        : balance(0), interestCalculationStrategy(strategy) {}

    void addObserver(Observer* observer) override {
        observers.push_back(observer);
    }

    void removeObserver(Observer* observer) override {
        auto it = std::find(observers.begin(), observers.end(), observer);
        if (it != observers.end()) {
            observers.erase(it);
        }
    }

    void notifyObservers() override {
        for (Observer* observer : observers) {
            observer->update(balance);
        }
    }

    void handleWithdrawal(double amount, double& balance) override {
        // Use Chain of Responsibility to handle withdrawals
        if (amount <= 1000) {
            balance -= amount;
            std::cout << "Bank Account handled withdrawal of $" << amount << std::endl;
        } else if (successor != nullptr) {
            successor->handleWithdrawal(amount, balance);
        }
    }

    void deposit(double amount) {
        balance += amount;
        std::cout << "Deposited: $" << amount << ", Balance: $" << balance << std::endl;
        notifyObservers();
    }

    void withdraw(double amount) {
        // Use Chain of Responsibility to handle withdrawals
        handleWithdrawal(amount, balance);
        notifyObservers();
    }

    double getBalance() const {
        return balance;
    }

    void setInterestCalculationStrategy(InterestCalculationStrategy* strategy) {
        interestCalculationStrategy = strategy;
    }

    double calculateInterest() const {
        return interestCalculationStrategy->calculateInterest(balance);
    }
};