---
title: Defining Functions
level: beginner
order: 1
---

# Defining Functions

Functions group reusable code.

## Basic Function

```python
def greet():
    print("Hello")
```

```python
greet()
```

## Function with Parameters

```python
def greet(name):
    print(f"Hello {name}")
```

```python
greet("Alice")
```

## Return Value

```python
def add(a, b):
    return a + b
```

```python
result = add(5, 3)

print(result)
```

## Practice

1. Create a function to calculate area.
2. Create a function to find the largest of two numbers.