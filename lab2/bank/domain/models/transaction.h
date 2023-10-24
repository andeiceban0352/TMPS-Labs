#include <iostream>
using namespace std;


class Transaction {
public:
    void performTransaction(string sender, string receiver, double amount) {
        cout << "Transaction details:" << endl;
        cout << "Sender: " << sender << endl;
        cout << "Receiver: " << receiver << endl;
        cout << "Amount: " << amount << endl;
        cout << "Transaction completed successfully." << endl;
    }
};