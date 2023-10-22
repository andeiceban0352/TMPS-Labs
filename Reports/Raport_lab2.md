# Topic: Creational Design Patterns Principles

## Author: Ceban Andrei FAF-211

## Objectives:

1. Study and understand the Creational Design Patterns.

2. Choose a domain, define its main classes/models/entities and choose the appropriate instantiation mechanisms.

3. Use some creational design patterns for object instantiation in a sample project.

## Theory:

&ensp; &ensp; Creational design patterns encompass a set of design principles centered around the creation of objects. They offer a means to generate objects in a versatile and organized manner, all while separating the client code from the intricacies of object creation. These patterns tackle common issues encountered during object creation, such as constructing objects with varying initialization parameters, generating objects based on specific conditions, or ensuring the existence of only a single instance of an object. There exist numerous creational design patterns, each with its own unique advantages and disadvantages, ideally suited for addressing particular challenges linked to object creation. By integrating creational design patterns, developers can enhance the adaptability, maintainability, and scalability of their code.


### Singleton Design Pattern

The Singleton pattern guarantees that a class has just a single instance and offers a universal entry point for accessing it. This proves beneficial for functionalities like logging, driver objects, caching, thread pools, or managing database connections.

The `Bank` class is implemented as a Singleton, ensuring that there is only one instance of the bank throughout the application, using the getInstance method to control the creation of instances.

```c++
    class Bank {
    private:
        static Bank* instance;

        map<string, BankAccount*> accounts;
        queue<BankAccount*> accountPool;  // Pool of BankAccount objects

        // Private constructor to prevent direct instantiation
        Bank() {}

    public:
        // singleton principle, only one instance of bank will be in this app
        static Bank& getInstance() {
            static Bank instance; // Guaranteed to be destroyed.
                                // Instantiated on first use.
            return instance;
        }
    }

```

### Builder Design Pattern

The builder pattern is a design pattern designed to provide a flexible solution to various object creation problems in object-oriented programming

The Builder design pattern is used to construct a complex object step by step. The CustomerBuilder class is a ConcreteBuilder that is used to construct the Customer object. The Customer class seems to be the Product being constructed, with name, age, address, and isVIP as its attributes. The CustomerBuilder class provides methods to set each of these attributes step by step, allowing for the construction of a Customer object in a controlled and organized manner.

```c++
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
```

### Factory Design Pattern

Prototype design pattern is used when the Object creation is a costly affair and requires a lot of time and resources and you have a similar object already existing

The Prototype design pattern allows you to create new objects by copying an existing object, known as a prototype. In the code, the AccountFactory class, which is the factory interface, defining the method createAccount for creating BankAccount objects. The BankAccountFactory is a concrete factory class that inherits from the AccountFactory and provides an implementation for the createAccount method, creating instances of the BankAccount class.

```c++
    // Abstract factory for creating accounts
    class AccountFactory {
    public:
        virtual BankAccount* createAccount(double initialBalance) = 0;
    };

    // Factory class for BankAccount
    class BankAccountFactory : public AccountFactory {
    public:
        BankAccount* createAccount(double initialBalance) override {
            return new BankAccount(initialBalance);
        }
    };

```

### Object Pooling Design Pattern

The object pool pattern is a software creational design pattern that uses a set of initialized objects kept ready to use – a "pool" – rather than allocating and destroying them on demand. 
Object Pooling is used to manage the object caching. It can significantly improve performance by reusing objects instead of creating them a new each time they are needed.

The Object Pooling design pattern is used to manage a pool of reusable objects to reduce the overhead of object creation. In the code,  The accountPool maintains a set of BankAccount objects that can be reused when needed. The acquireAccount function retrieves an available BankAccount from the pool, and if the pool is empty, it creates a new BankAccount object. The releaseAccount function returns the BankAccount object back to the pool for future reuse.

```c++


    class Bank {
    private:

        queue<BankAccount*> accountPool;  // Pool of BankAccount objects
        ...
    }
        // Object Pooling
    BankAccount* acquireAccount(double initialBalance) {
        if (accountPool.empty()) {
            return new BankAccount(initialBalance);
        } else {
            BankAccount* account = accountPool.front();
            accountPool.pop();
            account->deposit(initialBalance);  // Reset the balance
            return account;
        }
    }

    void releaseAccount(BankAccount* account) {
        accountPool.push(account);  // Release the account back to the pool
    }


```

## Conclusion

This laboratory work not only deepened my appreciation for the importance of design patterns in software development but also underscored their crucial role in crafting robust and efficient software solutions. By implementing these design patterns, I witnessed firsthand how they can greatly enhance code organization, maintainability, and scalability. These design patterns serve as valuable tools in the developer's toolkit, offering proven solutions to recurring design challenges and promoting best practices in software engineering.
