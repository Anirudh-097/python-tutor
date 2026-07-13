---
title: Magic Methods
level: intermediate
order: 5
---

# Magic Methods

Magic methods are special methods surrounded by double underscores.

They allow objects to interact with Python's built-in operations.

## __init__

Called when creating an object.

```python
class Person:

    def __init__(self, name):
        self.name = name


person = Person("Alice")
```

## __str__

Controls string representation.

```python
class Person:

    def __init__(self, name):
        self.name = name


    def __str__(self):
        return self.name


person = Person("Alice")

print(person)
```

## __repr__

Developer-friendly representation.

```python
class Student:

    def __repr__(self):
        return "Student()"
```

## __len__

Allows using `len()`.

```python
class Team:

    def __init__(self, players):
        self.players = players


    def __len__(self):
        return len(self.players)


team = Team(["A", "B", "C"])

print(len(team))
```

## Operator Overloading

### __add__

```python
class Number:

    def __init__(self, value):
        self.value = value


    def __add__(self, other):
        return self.value + other.value


a = Number(10)
b = Number(20)

print(a + b)
```

## Comparison Methods

```python
class Person:

    def __init__(self, age):
        self.age = age


    def __lt__(self, other):
        return self.age < other.age


a = Person(20)
b = Person(30)

print(a < b)
```

## Common Magic Methods

| Method | Purpose |
|--------|---------|
| `__init__` | Constructor |
| `__str__` | String display |
| `__repr__` | Debug representation |
| `__len__` | Length |
| `__add__` | Addition |
| `__eq__` | Equality |
| `__lt__` | Less than |

## Practice

1. Create a `Book` class.
2. Implement `__str__`.
3. Implement `__len__`.
4. Overload the `+` operator.