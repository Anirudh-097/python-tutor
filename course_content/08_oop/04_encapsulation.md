---
title: Encapsulation
level: intermediate
order: 4
---

# Encapsulation

Encapsulation means bundling data and methods together and controlling access to internal data.

Python uses naming conventions to indicate access levels.

## Public Attributes

Accessible anywhere.

```python
class Person:

    def __init__(self, name):
        self.name = name


person = Person("Alice")

print(person.name)
```

## Protected Attributes

A single underscore indicates protected data.

```python
class Person:

    def __init__(self):
        self._age = 20
```

It means:

"Do not access directly unless necessary."

## Private Attributes

Double underscore creates private attributes.

```python
class Account:

    def __init__(self):
        self.__balance = 1000


account = Account()
```

Direct access fails:

```python
print(account.__balance)
```

## Getter Method

```python
class Account:

    def __init__(self):
        self.__balance = 1000


    def get_balance(self):
        return self.__balance


account = Account()

print(account.get_balance())
```

## Setter Method

```python
class Account:

    def __init__(self):
        self.__balance = 0


    def set_balance(self, amount):

        if amount >= 0:
            self.__balance = amount


account = Account()

account.set_balance(500)

print(account.get_balance())
```

## Property Decorator

Pythonic getter/setter approach.

```python
class Person:

    def __init__(self, age):
        self._age = age


    @property
    def age(self):
        return self._age


    @age.setter
    def age(self, value):
        self._age = value


person = Person(20)

person.age = 25

print(person.age)
```

## Practice

1. Create a bank account class.
2. Make balance private.
3. Add deposit and withdraw methods.
4. Validate balance changes.