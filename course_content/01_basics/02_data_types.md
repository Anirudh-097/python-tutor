---
title: Data Types
level: beginner
order: 2
---

# Data Types

Python supports several built-in data types.

| Type | Example |
|------|---------|
| int | `10` |
| float | `3.14` |
| str | `"hello"` |
| bool | `True` |
| list | `[1,2,3]` |
| tuple | `(1,2,3)` |
| set | `{1,2,3}` |
| dict | `{"a":1}` |
| NoneType | `None` |

## Integer

```python
age = 25
print(type(age))
```

## Float

```python
price = 99.99
print(type(price))
```

## String

```python
name = "Alice"
print(type(name))
```

## Boolean

```python
is_logged_in = True
print(type(is_logged_in))
```

## List

```python
numbers = [1, 2, 3]
print(numbers)
```

## Tuple

```python
point = (10, 20)
print(point)
```

## Set

```python
colors = {"red", "green", "blue"}
print(colors)
```

## Dictionary

```python
student = {
    "name": "Alice",
    "age": 20
}

print(student)
```

## None

```python
result = None
print(result)
```

## Checking Type

```python
print(type(10))
print(type(2.5))
print(type("Python"))
print(type(False))
```

## Type Conversion

```python
x = "10"

print(int(x))
print(float(x))
```

```python
age = 20

print(str(age))
```

## Practice

1. Create one variable of every built-in type.
2. Print the type of each variable.
3. Convert `"100"` into an integer.
4. Convert `10` into a string.