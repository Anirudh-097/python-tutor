---
title: Inheritance
level: intermediate
order: 2
---

# Inheritance

Inheritance allows one class to reuse properties and methods from another class.

The existing class is called the **parent class**.

The new class is called the **child class**.

## Basic Inheritance

```python
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):
    pass


dog = Dog()

dog.speak()
```

## Adding New Methods

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


dog = Dog()

dog.eat()
dog.bark()
```

## Overriding Methods

A child class can replace a parent method.

```python
class Animal:

    def sound(self):
        print("Some sound")


class Dog(Animal):

    def sound(self):
        print("Woof")


dog = Dog()

dog.sound()
```

## Using super()

`super()` calls the parent class method.

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Max", "Labrador")

print(dog.name)
print(dog.breed)
```

## Multiple Inheritance

A class can inherit from multiple classes.

```python
class A:
    def show_a(self):
        print("A")


class B:
    def show_b(self):
        print("B")


class C(A, B):
    pass


obj = C()

obj.show_a()
obj.show_b()
```

## Types of Inheritance

- Single inheritance
- Multiple inheritance
- Multilevel inheritance
- Hierarchical inheritance

## Practice

1. Create an `Animal` parent class.
2. Create `Dog` and `Cat` child classes.
3. Override a method.
4. Use `super()`.