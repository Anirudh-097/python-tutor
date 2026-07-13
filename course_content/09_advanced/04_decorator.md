---
title: Decorators
level: advanced
order: 4
---

# Decorators

A decorator is a function that modifies the behavior of another function.

Decorators use the `@` syntax.

## Functions are Objects

```python
def greet():
    return "Hello"


message = greet

print(message())
```

## Basic Decorator

```python
def decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@decorator
def greet():
    print("Hello")


greet()
```

Output:

```text
Before function
Hello
After function
```

## Decorator with Arguments

```python
def decorator(func):

    def wrapper(name):
        print("Running function")
        func(name)

    return wrapper


@decorator
def greet(name):
    print(f"Hello {name}")


greet("Alice")
```

## Returning Values

```python
def decorator(func):

    def wrapper():
        result = func()
        return result.upper()

    return wrapper


@decorator
def message():
    return "hello"


print(message())
```

## Multiple Decorators

```python
def first(func):

    def wrapper():
        print("First")
        func()

    return wrapper


def second(func):

    def wrapper():
        print("Second")
        func()

    return wrapper


@first
@second
def hello():
    print("Hello")


hello()
```

## Built-in Decorators

Common decorators:

```python
@property
@staticmethod
@classmethod
```

## Practice

1. Create a decorator that logs function execution.
2. Create a decorator that measures execution time.
3. Create a decorator that checks permissions.