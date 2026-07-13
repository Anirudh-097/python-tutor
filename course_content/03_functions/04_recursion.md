---
title: Recursion
level: beginner
order: 4
---

# Recursion

A recursive function calls itself.

## Factorial

```python
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

## Countdown

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)
```

## Practice

1. Print numbers recursively.
2. Calculate factorial.
3. Calculate Fibonacci numbers.