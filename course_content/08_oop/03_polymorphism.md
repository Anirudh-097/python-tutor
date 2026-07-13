---
title: Polymorphism
level: intermediate
order: 3
---

# Polymorphism

Polymorphism means "many forms".

The same method name can behave differently for different objects.

## Method Overriding

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

## Same Interface

```python
class Bird:

    def move(self):
        print("Flying")


class Fish:

    def move(self):
        print("Swimming")


animals = [
    Bird(),
    Fish()
]


for animal in animals:
    animal.move()
```

## Duck Typing

Python focuses on behavior instead of object type.

```python
class Duck:

    def speak(self):
        print("Quack")


class Person:

    def speak(self):
        print("Hello")


def make_sound(obj):
    obj.speak()


make_sound(Duck())
make_sound(Person())
```

## Operator Polymorphism

The same operator behaves differently.

```python
print(5 + 10)

print("Hello " + "Python")
```

## Function Polymorphism

```python
print(len("Python"))

print(len([1, 2, 3]))
```

## Practice

1. Create `Car` and `Bike` classes with a `drive()` method.
2. Create a loop calling the same method.
3. Demonstrate duck typing.