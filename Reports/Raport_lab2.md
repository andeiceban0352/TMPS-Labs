# Topic: Creational Design Patterns Principles

## Author: Ceban Andrei FAF-211

## Objectives:

1. Study and understand the Creational Design Patterns.

2. Choose a domain, define its main classes/models/entities and choose the appropriate instantiation mechanisms.

3. Use some creational design patterns for object instantiation in a sample project.

## Theory:

&ensp; &ensp; Creational design patterns are a category of design patterns that focus on the process of object creation. They provide a way to create objects in a flexible and controlled manner, while decoupling the client code from the specifics of object creation. Creational design patterns address common problems encountered in object creation, such as how to create objects with different initialization parameters, how to create objects based on certain conditions, or how to ensure that only a single instance of an object is created. There are several creational design patterns that have their own strengths and weaknesses. Each of it is best suited for solving specific problems related to object creation. By using creational design patterns, developers can improve the flexibility, maintainability, and scalability of their code.

The project is a User Management System, which handles CRUD operations for users.

### Singleton Design Pattern

The Singleton pattern ensures that a class has only one instance and provides a global point to access it. This is useful for logging, driver objects, caching, thread pools, or database connections.

In the `UserService` class, the Singleton pattern is implemented to ensure that only one instance of `UserService` exists.

```python

```

### Builder Design Pattern

The Builder pattern is used to construct a complex object step by step. It provides a clear separation between the construction and representation of an object.

In the `UserDTO` class, the Builder pattern is implemented to allow the creation of `UserDTO` objects in a step-by-step manner.

```python

```

### Prototype Design Pattern

The Prototype pattern is used for creating new objects by copying existing objects. It is particularly useful when object creation is costly.

In the `User` class, the Prototype pattern is implemented using the `clone` method.

```python

```

### Object Pooling Design Pattern

Object Pooling is used to manage the object caching. It can significantly improve performance by reusing objects instead of creating them anew each time they are needed.

In the `UserRepository` class, Object Pooling is implemented to manage `User` objects.

```python

```

## Conclusion

This laboratory work helped me to understand the importance of design patterns in software development. Implementing these patterns made the code more organized, maintainable, and scalable.