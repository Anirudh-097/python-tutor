---
title: functools Module
level: advanced
order: 5
---

# functools

`functools` provides higher-order functions for working with functions.

```python
import functools
```

## reduce()

Applies a function repeatedly to items.

```python
from functools import reduce


numbers = [1, 2, 3, 4]

result = reduce(
    lambda x, y: x + y,
    numbers
)

print(result)
```

Output:

```text
10
```

## partial()

Creates a new function with some arguments fixed.

```python
from functools import partial


def multiply(a, b):
    return a * b


double = partial(multiply, 2)

print(double(5))
```

Output:

```text
10
```

## wraps()

Preserves function metadata in decorators.

Without wraps:

```python
def decorator(func):

    def wrapper():
        return func()

    return wrapper
```

With wraps:

```python
from functools import wraps


def decorator(func):

    @wraps(func)
    def wrapper():
        return func()

    return wrapper
```

## lru_cache()

Caches function results.

```python
from functools import lru_cache


@lru_cache
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))
```

## Practical Uses

`functools` helps with:

- Function composition
- Performance optimization
- Decorator creation
- Functional programming

## Practice

1. Use `reduce()` to multiply numbers.
2. Use `partial()` to create specialized functions.
3. Optimize Fibonacci using `lru_cache`.