---
title: Yield Keyword
level: advanced
order: 3
---

# Yield Keyword

The `yield` keyword pauses a function and saves its current state.

When called again, execution continues from where it stopped.

## Example

```python
def demo():

    print("Start")

    yield 1

    print("Middle")

    yield 2

    print("End")


generator = demo()

print(next(generator))
print(next(generator))
```

Output:

```text
Start
1
Middle
2
```

## yield vs return

Return:

```python
def numbers():
    return [1, 2, 3]
```

- Ends the function.
- Returns once.

Yield:

```python
def numbers():

    yield 1
    yield 2
    yield 3
```

- Pauses execution.
- Can return multiple values.

## Generator State

```python
def count():

    x = 1

    while x <= 3:
        yield x
        x += 1


generator = count()

print(next(generator))
print(next(generator))
```

The variable `x` keeps its value.

## Reading Large Files

Without generator:

```python
file = open("large.txt")

lines = file.readlines()
```

Loads everything into memory.

Using generator:

```python
def read_lines(filename):

    with open(filename) as file:

        for line in file:
            yield line


for line in read_lines("large.txt"):
    print(line)
```

## yield from

Combine generators.

```python
def numbers():

    yield from [1, 2, 3]


for n in numbers():
    print(n)
```

## Practice

1. Create a generator that reads a file line by line.
2. Create a generator for Fibonacci numbers.
3. Use `yield from`.