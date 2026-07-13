---
title: Generators
level: advanced
order: 2
---

# Generators

Generators are special functions that return values one at a time instead of storing all values in memory.

Generators use the `yield` keyword.

## Normal Function

```python
def numbers():
    return [1, 2, 3, 4, 5]


print(numbers())
```

The complete list is created in memory.

## Generator Function

```python
def numbers():

    yield 1
    yield 2
    yield 3


for n in numbers():
    print(n)
```

Output:

```text
1
2
3
```

## Generator Object

```python
def count():

    yield 1
    yield 2
    yield 3


result = count()

print(result)
```

Output:

```text
<generator object>
```

## Using next()

```python
def numbers():

    yield 10
    yield 20
    yield 30


generator = numbers()

print(next(generator))
print(next(generator))
```

## Generator Expression

Similar to list comprehension.

List:

```python
numbers = [x*x for x in range(10)]
```

Generator:

```python
numbers = (x*x for x in range(10))
```

## Memory Difference

List:

```python
numbers = [x for x in range(1000000)]
```

Generator:

```python
numbers = (x for x in range(1000000))
```

Generators do not store all values.

## Infinite Generator

```python
def infinite():

    number = 0

    while True:
        yield number
        number += 1


values = infinite()

print(next(values))
print(next(values))
print(next(values))
```

## Practice

1. Create a generator for numbers 1-10.
2. Create a generator for even numbers.
3. Convert a list comprehension into a generator expression.