---
title: Try Except
level: intermediate
order: 1
---

# Try Except

Errors that occur while a program is running are called **exceptions**. Python provides the `try` and `except` statements to handle exceptions gracefully.

## Basic Example

```python
try:
    number = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## Handling Multiple Exceptions

```python
try:
    number = int("abc")
except ValueError:
    print("Invalid number.")
```

```python
try:
    items = [1, 2, 3]

    print(items[5])
except IndexError:
    print("Index out of range.")
```

## Multiple Except Blocks

```python
try:
    value = int(input("Enter a number: "))
    print(10 / value)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## Catching Multiple Exceptions

```python
try:
    value = int(input())
    print(100 / value)

except (ValueError, ZeroDivisionError):
    print("Something went wrong.")
```

## Generic Exception

```python
try:
    result = 10 / 0

except Exception as error:
    print(error)
```

## else Block

The `else` block executes only if no exception occurs.

```python
try:
    number = int("10")

except ValueError:
    print("Invalid")

else:
    print(number)
```

## finally Block

The `finally` block always executes.

```python
try:
    file = open("notes.txt")

finally:
    file.close()
```

A better approach is to use `with` when working with files.

```python
with open("notes.txt") as file:
    print(file.read())
```

## Complete Example

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print(number)

finally:
    print("Program finished.")
```

## Common Exceptions

| Exception | Description |
|-----------|-------------|
| `ValueError` | Invalid value |
| `TypeError` | Wrong data type |
| `IndexError` | Invalid list index |
| `KeyError` | Missing dictionary key |
| `FileNotFoundError` | File does not exist |
| `ZeroDivisionError` | Division by zero |

## Practice

1. Handle division by zero.
2. Handle invalid integer input.
3. Handle missing dictionary keys.
4. Use `else` and `finally` in a program.