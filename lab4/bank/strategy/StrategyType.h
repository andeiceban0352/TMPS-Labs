
#pragma once
#include <iostream>
#include <vector>
#include <string>
using namespace std;


class SimpleInterestCalculation : public InterestCalculationStrategy {
public:
    double calculateInterest(double balance) const override {
        return balance * 0.02; // 2% interest rate
    }
};

class PremiumInterestCalculation : public InterestCalculationStrategy {
public:
    double calculateInterest(double balance) const override {
        return balance * 0.15; // 15% interest rate
    }
};