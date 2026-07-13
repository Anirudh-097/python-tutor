---
title: While Loop
level: beginner
order: 4
---

# While Loop

A `while` loop executes as long as its condition is `True`.

## Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## Infinite Loop

```python
while True:
    print("Running")
    break
```

## User Input

```python
password = ""

while password != "python":
    password = input("Password: ")

print("Access Granted")
```

## Practice

1. Print numbers from 1 to 20.
2. Find the sum of first 100 numbers.
3. Print a multiplication table.