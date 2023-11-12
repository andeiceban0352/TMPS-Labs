
#pragma once
#include <iostream>
#include <vector>
#include <string>
using namespace std;


// Concrete Observer - Customer
class Customer : public Observer {
private:
    std::string name;

public:
    Customer(const std::string& name) : name(name) {}

    void update(double balance) override {
        std::cout << "Customer " << name << " - Updated Balance: $" << balance << std::endl;
    }
};
