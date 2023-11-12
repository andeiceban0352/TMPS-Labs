
#pragma once
#include <iostream>
#include <vector>
#include <string>
using namespace std;


// Strategy interface for Strategy Design Pattern
class InterestCalculationStrategy {
public:
    virtual double calculateInterest(double balance) const = 0;
};
