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
* Any new account type  inherit  Account class and implement the get_account_type method.
So, we can easily add new account types by creating classes that inherit from Account without modifying the existing code. This adheres to the Open/Closed Principle, as you can extend the functionality without modifying the existing codebase.

```python
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

    def get_account_type(self):
            print("Bank Account")

```

* Liskov Substitution Principle (LSP):
THe BankUser class manages user accounts. The LSP implies that derived classes should be substitutable for their base classes without affecting the correctness of the program. Here's an example:
```python
class BankUser(User):
    def __init__(self, username):
        # ...
    
    def create_account(self):
        # ...

    def set_phone_number(self, phone_number):
        # ...

    # Other methods...

    def profile_info(self):
        # ...

```
Now, if we want to create a specialized type of bank user, ex:PremiumBankUser. You can create a subclass of BankUser to represent premium users. 
PremiumBankUser is a subclass of BankUser, which means it inherits the same interface as BankUser , it won't break the program's correctness because it follows the same interface and behaviors as its parent class.

* Interface Segregation Principle (ISP):
User and Account interfaces are minimal and focused on their respective roles. For example, the Account interface specifies only the methods relevant to account management:
```python
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

```python
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


The importance of the fundamental software design principles of Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion was highlighted through laboratory work on the SOLID principles. The use of SOLID principles helps produce not only good architecture but efficient architecture. It is also about separating concerns and creating a design that allows sustainable development. When the developer builds software following a bad design, the code can become inflexible and more brittle. Small changes in the software can result in bugs. For these reasons, we should follow SOLID Principles.
