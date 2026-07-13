---
title: Function Arguments
level: beginner
order: 2
---

# Function Arguments

Functions can accept different kinds of arguments.

## Positional Arguments

```python
def greet(name):
    print(name)

greet("Alice")
```

## Keyword Arguments

```python
def greet(name, age):
    print(name, age)

greet(age=20, name="Bob")
```

## Default Arguments

```python
def greet(name="Guest"):
    print(name)

greet()
greet("Alice")
```

## Multiple Parameters

```python
def add(a, b, c):
    return a + b + c

print(add(1, 2, 3))
```

## Practice

1. Create a function with default values.
2. Call a function using keyword arguments.