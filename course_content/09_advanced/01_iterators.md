---
title: Iterators
level: advanced
order: 1
---

# Iterators

An iterator is an object that allows you to access elements one at a time.

Python uses the iterator protocol:

- `__iter__()` returns an iterator
- `__next__()` returns the next value

## Iterable vs Iterator

An iterable is an object that can be looped over.

Examples:

```python
numbers = [1, 2, 3]

for n in numbers:
    print(n)
```

Lists are iterable but not iterators.

```python
numbers = [1, 2, 3]

print(next(numbers))
```

This raises:

```text
TypeError
```

## Creating an Iterator

Use `iter()`.

```python
numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
1
2
3
```

## StopIteration

When there are no more items:

```python
numbers = [1, 2]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
StopIteration
```

## Using Iterator in Loop

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

for item in iterator:
    print(item)
```

## Creating Custom Iterator

```python
class Counter:

    def __init__(self, max):
        self.max = max
        self.current = 0


    def __iter__(self):
        return self


    def __next__(self):

        if self.current >= self.max:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


counter = Counter(5)

for number in counter:
    print(number)
```

## Practical Uses

Iterators are useful for:

- Large datasets
- Reading files
- Streaming data
- Memory optimization

## Practice

1. Create an iterator for counting numbers.
2. Iterate through a tuple using `next()`.
3. Create a custom iterator that returns even numbers.