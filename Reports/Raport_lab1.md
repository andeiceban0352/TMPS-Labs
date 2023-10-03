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
&ensp; &ensp; __1. Choose an OOP programming language and a suitable IDE or Editor (No frameworks/libs/engines allowed).__

&ensp; &ensp; __2. Select a domain area for the sample project.__

&ensp; &ensp; __3. Define the main involved classes and think about what instantiation mechanisms are needed.__

&ensp; &ensp; __4. Respect SOLID Principles in your project.__

## Code examples of SOLID Principles:

* Single Responsibility Principle (SRP):
Classes like Bank, AccountPool, BankManager, and TransactionProcessor have single responsibilities, such as managing accounts, customers, and processing transactions.


```python
class BankManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer

class TransactionProcessor:
    @staticmethod
    def process_transaction(transaction, bank):
        source_account = bank.get_account_by_id(transaction.source_account_id)
        destination_account = bank.get_account_by_id(transaction.destination_account_id)

        if source_account and destination_account:
            if source_account.balance >= transaction.amount:
                source_account.balance -= transaction.amount
                destination_account.balance += transaction.amount
                return True
        return False
```


* Open/Closed Principle (OCP)
The code is open for extension but closed for modification. You can add new account types by creating new prototypes (SavingsAccount, CheckingAccount, LoanAccount) without modifying the existing code.

```python
class Account(ABC):
     # ...

class SavingsAccount(AccountPrototype):
    # ...

class CheckingAccount(AccountPrototype):
     # ...


class LoanAccount(AccountPrototype):
    # ...
```

* Liskov Substitution Principle (LSP):
The code allows for the substitution of derived account types (SavingsAccount, CheckingAccount, LoanAccount) for the base class (Account) without affecting the correctness of the program.

```python
class SavingsAccount(AccountPrototype):
    def __init__(self):
        self._account_id = None
        self._owner_name = None
        self._balance = 0

    def set_account_id(self, account_id):
        self._account_id = account_id

    def set_owner_name(self, owner_name):
        self._owner_name = owner_name

    def clone(self):
        new_account = SavingsAccount()
        new_account.set_account_id(self._account_id)
        new_account.set_owner_name(self._owner_name)
        new_account.balance = self._balance
        return new_account

class CheckingAccount(AccountPrototype):
    def __init__(self):
        self._account_id = None
        self._owner_name = None
        self._balance = 0

     # ...


class LoanAccount(AccountPrototype):
    def __init__(self):
        self._account_id = None
        self._owner_name = None
        self._balance = 0

    # ... 
```


* Interface Segregation Principle (ISP):
The code follows the Interface Segregation Principle by defining separate interfaces (e.g., Account, AccountBuilder, AccountPrototype, Transaction, Customer) with specific sets of methods for different purposes.

```python
class Account(ABC):
    def __init__(self, account_id, owner_name, balance=0):
        self._account_id = account_id
        self._owner_name = owner_name
        self._balance = balance

class AccountBuilder(ABC):
    def __init__(self):
        self.account_id = None
        self.owner_name = None
        self.balance = 0
    @abstractmethod
    def build(self):
        pass

class AccountPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass


```


* Dependency Inversion Principle (DIP):
The code follows the Dependency Inversion Principle by abstracting the Account and AccountBuilder classes as well as the Transaction classes, allowing for flexible extension and interchangeability of concrete implementations.

```python 
class Account(ABC):
    def __init__(self, account_id, owner_name, balance=0):
        self._account_id = account_id
        self._owner_name = owner_name
        self._balance = balance

    @property
    def account_id(self):
        return self._account_id

    @property
    def owner_name(self):
        return self._owner_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        self._balance = amount

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

```

## Conclusions


The importance of the fundamental software design principles of Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion was highlighted through laboratory work on the SOLID principles. The use of SOLID principles helps produce not only good architecture but efficient architecture. It is also about separating concerns and creating a design that allows sustainable development. When the developer builds software following a bad design, the code can become inflexible and more brittle. Small changes in the software can result in bugs. For these reasons, we should follow SOLID Principles.
