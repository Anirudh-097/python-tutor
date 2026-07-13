---
title: Tuples
level: intermediate
order: 2
---

# Tuples

A tuple is an ordered, immutable collection of items.

## Creating Tuples

```python
numbers = (1, 2, 3)

print(numbers)
```

Single element tuple

```python
value = (10,)

print(type(value))
```

## Accessing Elements

```python
colors = ("red", "green", "blue")

print(colors[0])
print(colors[-1])
```

## Slicing

```python
numbers = (10, 20, 30, 40)

print(numbers[1:3])
```

## Tuple Unpacking

```python
name, age = ("Alice", 20)

print(name)
print(age)
```

## Packing

```python
person = "Bob", 25

print(person)
```

## Useful Methods

```python
numbers = (1, 2, 2, 3)

print(numbers.count(2))
print(numbers.index(3))
```

## Iterating

```python
for item in ("A", "B", "C"):
    print(item)
```

## Why Tuples?

Use tuples when data should not change.

```python
point = (10, 20)
```

## Practice

1. Create a tuple of colors.
2. Access the last element.
3. Unpack a tuple into variables.
4. Count occurrences of a value.