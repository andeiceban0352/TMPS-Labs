#pragma once
#include <iostream>
using namespace std;

class BankApplicationMenuDecorator {
private:
    BankInterface* bankAdapter;

public:
    BankApplicationMenuDecorator(BankInterface* interface) : bankAdapter(interface) {}

    void checkAccountBalance()  {
        string accountNumber;

        cout << "Enter account number: ";
        cin >> accountNumber;
        double balance = bankAdapter->checkAccountBalance(accountNumber);
        // balance = bank.checkAccountBalance(accountNumber);
        if (balance != 0) {
            cout << "Current account balance: " << balance << endl;
        }
    }
};