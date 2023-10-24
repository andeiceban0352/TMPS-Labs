# Topic: Structural Design Patterns 

## Author: Ceban Andrei FAF-211

## Objectives:

1. Study and understand the Structural Design Patterns.

2. As a continuation of the previous laboratory work, think about the functionalities that your system will need to provide to the user.

3. Implement some additional functionalities, or create a new project using structural design patterns.

## Theory:

&ensp; &ensp; Structural design patterns are a category of design patterns that focus on the composition of classes and objects to form larger structures and systems. They provide a way to organize objects and classes in a way that is both flexible and efficient, while allowing for the reuse and modification of existing code. Structural design patterns address common problems encountered in the composition of classes and objects, such as how to create new objects that inherit functionality from existing objects, how to create objects that share functionality without duplicating code, or how to define relationships between objects in a flexible and extensible way.


### Adapter Design Pattern

The Adapter Pattern allows objects with incompatible interfaces to collaborate. It acts as a bridge between two incompatible interfaces. It is used when an object needs to work with another object that has an incompatible interface.

Bank Adapter class serves as an adapter for the BankInterface. It adapts the interface of the Bank class to the interface specified by the BankInterface. The BankAdapter class implements the BankInterface and internally uses an instance of the Bank class

```c++
    class BankInterface {
    public:
        ....
    };
    
    
    class BankAdapter : public BankInterface {
    private:
        Bank& bank;
    
    public:
        BankAdapter(Bank& bank) : bank(bank) {}
    
        void createAccount(const string& accountNumber, BankAccount* account) override {
            ....
        }
    
        void withdrawMoney(const string& accountNumber, double amount) override {
            ....
        }
    
        void depositMoney(const string& accountNumber, double amount) override {
            ....
        }
    
        double checkAccountBalance(const string& accountNumber) override {
            ....
        }
    };

```

### Composite Design Pattern

The Composite pattern describes a group of objects that are treated the same way as a single instance of the same type of object. The intent of a composite is to "compose" objects into tree structures to represent part-whole hierarchies.

Component -> BankComponent: Is the base interface or abstract class for all components in the composition. It declares the interface for objects in the composition, including methods for adding, removing, etc.

Leaf -> BankLeaf: This represents the end objects in the composition. It implements the BankComponent interface and represents individual objects in the composition. In this case, it represents individual bank accounts.

Composite -> BankComposite: This represents the complex components that can have children. It implements the BankComponent interface and provides the mechanisms to manage its child components, here representing a composite of bank accounts.

```c++

    class BankComponent {
    public:
        virtual void add(BankComponent* component) = 0;
        ...
    };
    
    class BankLeaf : public BankComponent {
    private:
        BankAccount* account;
    
    public:
        BankLeaf(BankAccount* acc) : account(acc) {}
    
        void add(BankComponent* component) override {
            // Leaf node cannot add components
            cout << "Cannot add to a leaf." << endl;
        }
    
        ...
    };
    
    class BankComposite : public BankComponent {
    private:
        vector<BankComponent*> accounts;
    
    public:
        void add(BankComponent* component) override {
            accounts.push_back(component);
        }
    
        ...
```

### Decorator Design Pattern

Decorator is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

Here in the example the BankApplicationMenuDecorator extends BankApplicationMenu,modify the behavior of the checkAccountBalance class dynamically, without affecting the behavior of other objects from the same class.

```c++
    class BankApplicationMenuDecorator : public BankApplicationMenu {
    private:
        BankInterface* bankAdapter;
    
    public:
        BankApplicationMenuDecorator(BankInterface* interface) : bankAdapter(interface) {}
    
        void checkAccountBalance() override {
            ...
        }
    };

```

### Facade Pooling Design Pattern

The Facade Pattern is a structural design pattern that provides a simplified interface to a larger body of code, such as a class library. It hides the complexities of the underlying system and provides a simpler interface for the client to interact with. The main goal of the 

BankFacade class acts as a facade to the more complex operations of the BankApplicationMenu and Bank classes. It provides a simplified interface for clients to interact with the underlying banking system without needing to understand its complexities. The clients can use the BankFacade to perform operations like creating accounts, making transactions, withdrawing and depositing money, checking account balances, and creating different types of customers.

```c++

    class BankFacade {
    private:
        BankApplicationMenu bankApp;
        Bank& bank;
    
    public:
        BankFacade() : bank(Bank::getInstance()) {}
    
        void createAccount(const string& accountNumber, double initialBalance) {
            BankAccount* newAccount = bank.acquireAccount(initialBalance);
            bank.createAccount(accountNumber, newAccount);
        }
    
        void makeTransaction() {
            ...
        }
    
        void withdrawMoney(const string& accountNumber, double amount) {
           ...
        }
    
        void depositMoney(const string& accountNumber, double amount) {
           ...
        }
    
        double checkAccountBalance(const string& accountNumber) {
            ...
        }
    
        Customer createCustomer() {
            ...
        }
    
        void createVIPCustomer() {
            ...
        }
    
        void createRegularCustomer() {
            ...
        }
    };


```

## Conclusion

This laboratory solidified my understanding of design patterns in software development and also highlighted their indispensable role in constructing resilient and efficient software solutions. Through the practical implementation of the Facade, Decorator, Composite, and Adapter design patterns, I gained valuable insights into how they contribute to meticulous code organization, enhanced maintainability, and scalable software architectures. These design patterns emerged as indispensable assets in the developer's arsenal, providing concrete solutions to recurring design complexities and promoting the adoption of best practices in software engineering. They not only simplify the integration of disparate components but also enable the seamless augmentation of functionalities, the dynamic structuring of hierarchical relationships, and the seamless adaptation of incompatible interfaces.
