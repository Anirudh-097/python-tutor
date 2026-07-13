---
title: Lambda Functions
level: beginner
order: 5
---

# Lambda Functions

Lambda functions are anonymous one-line functions.

## Basic Lambda

```python
square = lambda x: x * x

print(square(5))
```

## Multiple Parameters

```python
add = lambda a, b: a + b

print(add(5, 3))
```

## sorted()

```python
students = [
    ("Bob", 70),
    ("Alice", 90),
    ("John", 80)
]

students.sort(key=lambda student: student[1])

print(students)
```

## map()

```python
numbers = [1, 2, 3]

print(list(map(lambda x: x * 2, numbers)))
```

## filter()

```python
numbers = [1, 2, 3, 4, 5]

print(list(filter(lambda x: x % 2 == 0, numbers)))
```

## Practice

1. Square a number using lambda.
2. Sort a list of tuples.
3. Filter even numbers.