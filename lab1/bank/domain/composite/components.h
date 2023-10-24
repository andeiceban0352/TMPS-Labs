// #pragma once
// #include <iostream>
// #include <vector>
// using namespace std;


// class BankComponent {
// public:
//     virtual void display() const = 0;
    
// };


// class BankGroup : public BankComponent {
// private:
//     std::vector<BankComponent*> children;

// public:
//     void add(BankComponent* component) {
//         children.push_back(component);
//     }

//     void remove(BankComponent* component) {
//         // Remove the component from children
//         children.erase(std::remove(children.begin(), children.end(), component), children.end());
//     }

//     void display() const override {
//         for (auto component : children) {
//             component->display();
//         }
//     }
// };