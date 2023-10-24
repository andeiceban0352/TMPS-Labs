#pragma once
#include <iostream>
using namespace std;

class Customer  {
public:
    string name;
    int age;
    string address;
    string isVIP;

public:
    Customer(string name, int age, string address, string isVIP) : name(name), age(age), address(address), isVIP(isVIP) {}

    void displayCustomerDetails() {
        cout << "Customer Name: " << name << endl;
        cout << "Customer Age: " << age << endl;
        cout << "Customer Address: " << address << endl;
        // cout << "Is VIP: " << (isVIP ? "Yes" : "No") << endl;
    }
};


// VIP Customer class
class VIPCustomer {
public:
    virtual void createVIPCustomer() = 0;
};

// Regular Customer class
class RegularCustomer {
public:
    virtual void createRegularCustomer() = 0;
};