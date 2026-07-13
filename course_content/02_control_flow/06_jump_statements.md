---
title: Jump Statements
level: beginner
order: 6
---

# Jump Statements

Jump statements change the normal flow of loops.

## break

Stops the loop.

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

## continue

Skips the current iteration.

```python
for i in range(6):
    if i == 3:
        continue

    print(i)
```

## pass

Placeholder for future code.

```python
for i in range(5):
    pass
```

## Example

```python
for ch in "Python":
    if ch == "h":
        continue

    print(ch)
```

## Practice

1. Stop a loop when number becomes 10.
2. Skip all even numbers.
3. Create an empty function using `pass`.