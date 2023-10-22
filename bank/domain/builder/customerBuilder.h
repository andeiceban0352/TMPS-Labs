#pragma once
#include <iostream>
using namespace std;

// builder design ppattern
class CustomerBuilder{
public:
    Customer customer;

public:
    CustomerBuilder() : customer("", 0, "", "") {}


    CustomerBuilder& setName(const string& name) {
        customer.name = name;
        return *this;
    }

    CustomerBuilder& setAge(int age) {
        customer.age = age;
        return *this;
    }

    CustomerBuilder& setAddress(const string& address) {
        customer.address = address;
        return *this;
    }

    CustomerBuilder& setIsVIP(string isVIP) {
        customer.isVIP = isVIP;
        return *this;
    }

    Customer build() {
        return customer;
    }
};
