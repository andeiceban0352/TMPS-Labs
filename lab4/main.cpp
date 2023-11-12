#include <iostream>
#include <vector>
#include <string>

#include "./bank/chainofresponsability/WithdrawalHandler.h"
#include "./bank/chainofresponsability/BankEmployee.h"
#include "./bank/chainofresponsability/BranchManager.h"
#include "./bank/chainofresponsability/HeadOffice.h"
#include "./bank/observer/Observer.h"
#include "./bank/observer/Subject.h"
#include "./bank/strategy/Strategy.h"
#include "./bank/strategy/StrategyType.h"
#include "./bank/models/BankAccount.h"
#include "./bank/models/Customer.h"


// sudo g++ -std=c++14 main.cpp -o a.out

int main() {
    // Create a bank account
    BankAccount bankAccount(new SimpleInterestCalculation);

    // Create customers as observers
    Customer customer1("Jony");
    Customer customer2("Tommy");
    Customer customer3("Boby");
    Customer customer4("Andy");

    // Add customers as observers to the bank account
    bankAccount.addObserver(&customer1);
    bankAccount.addObserver(&customer2);
    bankAccount.addObserver(&customer3);
    bankAccount.addObserver(&customer4);

    // Create withdrawal handlers
    BankEmployee bankEmployee;
    BranchManager branchManager;
    HeadOffice headOffice;

    // Set up the chain of responsibility
    bankEmployee.setSuccessor(&branchManager);
    branchManager.setSuccessor(&headOffice);
    bankAccount.setSuccessor(&bankEmployee);

    // Perform transactions
    bankAccount.deposit(10000);
    bankAccount.withdraw(500);
    bankAccount.withdraw(2500);
    bankAccount.withdraw(7000);


    // Remove one observer (customer2)
    bankAccount.removeObserver(&customer2);

    // Perform another transaction
    bankAccount.deposit(900);

    bankAccount.setInterestCalculationStrategy(new PremiumInterestCalculation);
    std::cout << "Interest: $" << bankAccount.calculateInterest() << std::endl;

    bankAccount.setInterestCalculationStrategy(new SimpleInterestCalculation);
    std::cout << "Interest: $" << bankAccount.calculateInterest() << std::endl;


    return 0;
}
