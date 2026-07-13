---
title: Sets
level: intermediate
order: 3
---

# Sets

A set is an unordered collection of unique items.

## Creating Sets

```python
numbers = {1, 2, 3}

print(numbers)
```

Duplicates are removed automatically.

```python
numbers = {1, 2, 2, 3}

print(numbers)
```

## Adding Elements

```python
numbers = {1, 2}

numbers.add(3)

print(numbers)
```

## Removing Elements

```python
numbers.remove(2)

print(numbers)
```

```python
numbers.discard(5)
```

## Union

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

## Intersection

```python
print(a & b)
```

## Difference

```python
print(a - b)
```

## Symmetric Difference

```python
print(a ^ b)
```

## Membership

```python
colors = {"red", "green"}

print("red" in colors)
```

## Iterating

```python
for item in {"apple", "banana"}:
    print(item)
```

## Removing Duplicates

```python
numbers = [1, 2, 2, 3, 3, 4]

unique = list(set(numbers))

print(unique)
```

## Practice

1. Create two sets.
2. Find union.
3. Find intersection.
4. Remove duplicates from a list.