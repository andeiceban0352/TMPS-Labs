#pragma once
#include <iostream>
#include <vector>
#include <string>
using namespace std;


// Subject interface
class Subject {
public:
    virtual void addObserver(Observer* observer) = 0;
    virtual void removeObserver(Observer* observer) = 0;
    virtual void notifyObservers() = 0;
};
