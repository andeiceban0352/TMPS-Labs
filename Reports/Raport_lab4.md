# Topic: Behavioral Design Patterns 

## Author: Ceban Andrei FAF-211

## Objectives:

1. Study and understand the Behavioral Design Patterns.

2. As a continuation of the previous laboratory work, think about what communication between software entities might be involed in your system.

3. Create a new Project or add some additional functionalities using behavioral design patterns.

## Theory:

&ensp; &ensp;   Behavioral design patterns are a category of design patterns that focus on the interaction and communication between objects and classes. They provide a way to organize the behavior of objects in a way that is both flexible and reusable, while separating the responsibilities of objects from the specific implementation details. Behavioral design patterns address common problems encountered in object behavior, such as how to define interactions between objects, how to control the flow of messages between objects, or how to define algorithms and policies that can be reused across different objects and classes.


### Observer Design Pattern

The Observer Pattern is a behavioral pattern that allows some objects to notify other objects about changes in their state. It provides a way to react to events happening in other objects without coupling to their classes.

The pattern can be recognized by subscription methods, that store objects in a list and by calls to the update method issued to objects in that list. Here we have the Observer class that has updatre method and Subject class what methods that can be used to manage the observers as add or removing.
With this design pattern we can easily manage customers from a bank by adding them and removing. When the bank make a deposit, each cusomer will be notified by the change, by getting the ammout.
```c++
    class Observer {
    public:
        virtual void update(double balance) = 0;
    };
    
    class Subject {
    public:
        virtual void addObserver(Observer* observer) = 0;
        virtual void removeObserver(Observer* observer) = 0;
        virtual void notifyObservers() = 0;
    };

     Customer customer1("Jony");

    bankAccount.addObserver(&customer4);

```   


### Chain of Responsability Design Pattern

The Chain of Responsability pattern is behavioral design pattern that allows passing request along the chain of potential handlers until one of them handles request.  The pattern is recognizable by behavioral methods of one group of objects that indirectly call the same methods in other objects, while all the objects follow the common interface .
In our code, is implemented the WithdrawalHandler class wich has a handleWithdrawal method and setSuccessor method wich sets the hierarchy of each successor. We have 3 types oh handles : bankemployee, headoffice and branchmanage , where each of them has the same method handleWithdrawal but with different functional which is based on limiting the amount for withdraw.

```c++

    class WithdrawalHandler {
    protected:
        WithdrawalHandler* successor;
    
    public:
        virtual void handleWithdrawal(double amount, double& balance) = 0;
    
        void setSuccessor(WithdrawalHandler* successor) {
            this->successor = successor;
        }
    };

    class BankEmployee : public WithdrawalHandler {
    public:
        void handleWithdrawal(double amount, double& balance) override {
            ...
        }
    };

    class HeadOffice : public WithdrawalHandler {
    public:
        void handleWithdrawal(double amount, double& balance) override {
            ...
        }
    };

    // Create withdrawal handlers
    BankEmployee bankEmployee;
    BranchManager branchManager;
    HeadOffice headOffice;

    // Set up the chain of responsibility
    bankEmployee.setSuccessor(&branchManager);
    branchManager.setSuccessor(&headOffice);
    bankAccount.setSuccessor(&bankEmployee);

```

### Strategy Design Pattern

The Strategy pattern is a behavioral design pattern that turns a set of behaviors into objects and makes them interchangeable inside original context object.Strategy pattern can be recognized by a method that lets a nested object do the actual work, as well as a setter that allows replacing that object with a different one.
Here i implemented InterestCalculationStrategy class which has calculateInterest method for calculating the interest. Then we have 2 more classes with the same method calculateInterest where the functional is different. In code we ca use that by getting the ammount and setting the preferred method simple or vip interest percent.

```c++
    class InterestCalculationStrategy {
    public:
        virtual double calculateInterest(double balance) const = 0;
    };
    
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


    bankAccount.setInterestCalculationStrategy(new PremiumInterestCalculation);
    std::cout << "Interest: $" << bankAccount.calculateInterest() << std::endl;

    bankAccount.setInterestCalculationStrategy(new SimpleInterestCalculation);
    std::cout << "Interest: $" << bankAccount.calculateInterest() << std::endl;
```


## Conclusion

This laboratory solidified my understanding of behavioral patterns in software development and also helped me to understand better how to use them in daily code writing, by making the code more structured and efficient. By using these principles, the code become more optimized and readble also having a high value structure.  
