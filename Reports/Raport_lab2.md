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

The `Bank` class is implemented as a Singleton, ensuring that there is only one instance of the bank throughout the application, using the __new__ method to control the creation of instances.

```python
class Bank(ABC):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Bank, cls).__new__(cls)
            cls._instance.accounts = []
        return cls._instance
```

### Builder Design Pattern

The builder pattern is a design pattern designed to provide a flexible solution to various object creation problems in object-oriented programming

The Builder design pattern is used to construct a complex object step by step. In the code, the `AccountBuilder` and `ConcreteAccountBuilder` classes represent the Builder pattern. The ConcreteAccountBuilder class is responsible for creating instances of ConcreteAccount with various attributes, allowing you to build accounts with different configurations.

```python
class AccountBuilder(ABC):
    # ...

class ConcreteAccountBuilder(AccountBuilder):
    # ...
```

### Prototype Design Pattern

Prototype design pattern is used when the Object creation is a costly affair and requires a lot of time and resources and you have a similar object already existing

The Prototype design pattern allows you to create new objects by copying an existing object, known as a prototype. In the code, the Prototype pattern is implemented with the `AccountPrototype` interface and its concrete implementations (`SavingsAccount`, `CheckingAccount`, `LoanAccount`). These classes provide a clone method that creates a new instance by copying the existing object's attributes.

```python
class AccountPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class SavingsAccount(AccountPrototype):
    # ...

class CheckingAccount(AccountPrototype):
    # ...

class LoanAccount(AccountPrototype):
```

### Object Pooling Design Pattern

The object pool pattern is a software creational design pattern that uses a set of initialized objects kept ready to use – a "pool" – rather than allocating and destroying them on demand. 
Object Pooling is used to manage the object caching. It can significantly improve performance by reusing objects instead of creating them a new each time they are needed.

The Object Pooling design pattern is used to manage a pool of reusable objects to reduce the overhead of object creation. In the code, the `AccountPool` class is an example of object pooling. It allows you to create and retrieve account objects from a pool of pre-created instances.

```python
class AccountPool:
    # ...

    def create_account(self, account_prototype):
        # ...

    def get_account(self):
        # ...
```

## Conclusion

This laboratory work not only deepened my appreciation for the importance of design patterns in software development but also underscored their crucial role in crafting robust and efficient software solutions. By implementing these design patterns, I witnessed firsthand how they can greatly enhance code organization, maintainability, and scalability. These design patterns serve as valuable tools in the developer's toolkit, offering proven solutions to recurring design challenges and promoting best practices in software engineering.
