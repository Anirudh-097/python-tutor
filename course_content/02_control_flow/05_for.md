---
title: For Loop
level: beginner
order: 5
---

# For Loop

The `for` loop iterates over sequences.

## Iterate List

```python
numbers = [1, 2, 3]

for number in numbers:
    print(number)
```

## Iterate String

```python
for ch in "Python":
    print(ch)
```

## range()

```python
for i in range(5):
    print(i)
```

```python
for i in range(1, 6):
    print(i)
```

```python
for i in range(0, 10, 2):
    print(i)
```

## enumerate()

```python
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(index, color)
```

## Practice

1. Print even numbers from 1 to 100.
2. Find the sum of a list.
3. Count vowels in a string.