# Topic: SOLID Principles


## Author: Ceban Andrei

----

## Objectives:

* Study and understand the SOLID Principles.
* Choose a domain, define its main classes/models/entities and choose the appropriate instantiation mech
* Create a sample project that respects SOLID Principles.


## Theory:

&ensp; &ensp; SOLID is a popular set of design principles that are used in object-oriented software development. SOLID is an acronym that stands for five key design principles: single responsibility principle, open-closed principle, Liskov substitution principle, interface segregation principle, and dependency inversion principle. All five are commonly used by software engineers and provide some important benefits for developers. Implementing SOLID design principles during development will lead to systems that are more maintainable, scalable, testable, and reusable. In the current environment, these principles are used globally by engineers. As a result, to create good code and to use design principles that are competitive while meeting industry standards, it’s essential to utilize these principles.



## Main tasks:
&ensp; &ensp; __1. Choose an OO programming language and a suitable IDE or Editor (No frameworks/libs/engines allowed).__

&ensp; &ensp; __2. Select a domain area for the sample project.__

&ensp; &ensp; __3. Define the main involved classes and think about what instantiation mechanisms are needed.__

&ensp; &ensp; __4. Respect SOLID Principles in your project.__

## Code examples of SOLID Principles:

* Single Responsibility Principle (SRP):
The BankUser class has a single responsibility - managing user-related data and accounts. For example:


```python
from user import User 
from bank_account import BankAccount 

class BankUser(User):
    def __init__(self, username):
        self.username = username
        self.accounts = []
        self.phone_number = None
        self.idnp = None
        self.name = None
        self.surname = None
        self.location = None

    def create_account(self):
        account = BankAccount()
        self.accounts.append(account)
        return account

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_idnp(self, idnp):
        self.idnp = idnp

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_location(self, location):
        self.location = location
```


* Open/Closed Principle (OCP) 
Class Customer is open for extension because you can to add for example another type of customer, if you change something in Customer class you need to change his child classes. And LSP is presented in fact that Customer class can be easely substituted with OrdinaryCustomer class.
```
public void main() {

}
```

* Liskov Substitution Principle (LSP):
```
public void main() {

}
```

* Interface Segregation Principle (ISP):
User and Account interfaces are minimal and focused on their respective roles. For example, the Account interface specifies only the methods relevant to account management:
```
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def get_account_type(self):
        pass


```


* Dependency Inversion Principle (DIP):
Your code uses abstract classes and interfaces effectively to define contracts. For instance, BankUser depends on the abstract User class, and BankAccount depends on the abstract Account class. Here's an example of BankAccount depending on Account:

```
from account import Account 

class BankAccount(Account):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

```

## Conclusions


In conclusion, given laboratory work on SOLID principles emphasized the significance of these fundamental software design principles - Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion. I applied these principles to refactor and enhance a software project, demonstrating their ability to reduce complexity, improve organization, and facilitate long-term maintainability. I also recognized the benefits of SOLID principles in fostering collaboration among developers and ensuring software systems remain adaptable in a rapidly changing environment. As software engineers, integrating these principles into our practices is crucial for creating durable, adaptable, and high-quality software.
