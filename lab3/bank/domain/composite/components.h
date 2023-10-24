#pragma once
#include <iostream>
#include <vector>
using namespace std;


// Composite pattern
class BankComponent {
public:
    virtual void add(BankComponent* component) = 0;
    virtual void remove(BankComponent* component) = 0;
    virtual void displayAccountDetails() = 0;
    virtual double getBalance() = 0;
};

class BankLeaf : public BankComponent {
private:
    BankAccount* account;

public:
    BankLeaf(BankAccount* acc) : account(acc) {}

    void add(BankComponent* component) override {
        // Leaf node cannot add components
        cout << "Cannot add to a leaf." << endl;
    }

    void remove(BankComponent* component) override {
        // Leaf node cannot remove components
        cout << "Cannot remove from a leaf." << endl;
    }

    void displayAccountDetails() override {
        cout << "Account Details:" << endl;
        cout << "Balance: " << account->getBalance() << endl;
    }

    double getBalance() override {
        return account->getBalance();
    }
};

class BankComposite : public BankComponent {
private:
    vector<BankComponent*> accounts;

public:
    void add(BankComponent* component) override {
        accounts.push_back(component);
    }

    void remove(BankComponent* component) override {
        auto it = find(accounts.begin(), accounts.end(), component);
        if (it != accounts.end()) {
            accounts.erase(it);
        }
    }

    void displayAccountDetails() override {
        for (auto account : accounts) {
            account->displayAccountDetails();
        }
    }

    double getBalance() override {
        double totalBalance = 0;
        for (auto account : accounts) {
            totalBalance += account->getBalance();
        }
        return totalBalance;
    }
};
