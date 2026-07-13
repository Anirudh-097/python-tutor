---
title: '*args and **kwargs'
level: beginner
order: 3
---

# *args and **kwargs

Use `*args` to accept multiple positional arguments.

## *args

```python
def total(*numbers):
    print(sum(numbers))

total(1, 2, 3)
```

## Iterate

```python
def show(*items):
    for item in items:
        print(item)
```

## **kwargs

```python
def profile(**data):
    print(data)
```

```python
profile(name="Alice", age=20)
```

## Iterate

```python
def profile(**data):
    for key, value in data.items():
        print(key, value)
```

## Practice

1. Sum unlimited numbers.
2. Print all keyword arguments.