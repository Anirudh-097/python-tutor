---
title: Lists
level: intermediate
order: 1
---

# Lists

A list is an ordered, mutable collection of items. Lists can store values of different data types.

## Creating Lists

```python
numbers = [1, 2, 3, 4]
print(numbers)
```

```python
mixed = [1, "Python", 3.14, True]
print(mixed)
```

## Accessing Elements

```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[-1])
```

## Slicing

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
```

## Modifying Elements

```python
fruits = ["apple", "banana", "orange"]

fruits[1] = "grape"

print(fruits)
```

## Adding Elements

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

```python
numbers.insert(1, 100)

print(numbers)
```

```python
numbers.extend([5, 6, 7])

print(numbers)
```

## Removing Elements

```python
numbers = [1, 2, 3, 4]

numbers.remove(2)

print(numbers)
```

```python
numbers.pop()

print(numbers)
```

```python
del numbers[0]

print(numbers)
```

## Useful Methods

```python
numbers = [5, 2, 8, 1]

numbers.sort()
print(numbers)
```

```python
numbers.reverse()
print(numbers)
```

```python
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
```

## Iterating

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

## List Comprehension

```python
squares = [x * x for x in range(6)]

print(squares)
```

```python
evens = [x for x in range(10) if x % 2 == 0]

print(evens)
```

## Nested Lists

```python
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[1][0])
```

## Practice

1. Create a list of five numbers.
2. Add and remove elements.
3. Sort the list.
4. Create a list of squares using list comprehension.