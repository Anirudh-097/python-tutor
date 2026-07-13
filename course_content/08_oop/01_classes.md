---
title: Classes and Objects
level: intermediate
order: 1
---

# Classes and Objects

Object-Oriented Programming (OOP) is a programming style that organizes code using **objects**.

A class is a blueprint for creating objects.

An object is an instance of a class.

## Creating a Class

```python
class Student:
    pass
```

## Creating an Object

```python
class Student:
    pass

student1 = Student()

print(student1)
```

## Attributes

Attributes are variables that belong to an object.

```python
class Student:

    name = "Alice"
    age = 20


student = Student()

print(student.name)
print(student.age)
```

## Constructor

The `__init__()` method runs automatically when an object is created.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Alice", 20)

print(student.name)
print(student.age)
```

## Understanding self

`self` refers to the current object.

```python
class Car:

    def show(self):
        print("This is a car")


car = Car()

car.show()
```

Python internally calls:

```python
Car.show(car)
```

## Instance Methods

Methods are functions inside a class.

```python
class Dog:

    def bark(self):
        print("Woof!")


dog = Dog()

dog.bark()
```

## Updating Attributes

```python
class Person:

    def __init__(self, name):
        self.name = name


person = Person("Bob")

person.name = "John"

print(person.name)
```

## Multiple Objects

```python
class Person:

    def __init__(self, name):
        self.name = name


p1 = Person("Alice")
p2 = Person("Bob")

print(p1.name)
print(p2.name)
```

## Class Attributes

Shared by all objects.

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name


s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school)
print(s2.school)
```

## Practice

1. Create a `Car` class.
2. Add attributes: brand, model, year.
3. Create multiple car objects.
4. Add a method to display car details.