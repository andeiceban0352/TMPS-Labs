
#pragma once
#include <iostream>
#include <vector>
#include <string>
using namespace std;


// Observer interface
class Observer {
public:
    virtual void update(double balance) = 0;
};
