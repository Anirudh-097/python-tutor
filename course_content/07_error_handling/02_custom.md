---
title: Custom Exceptions
level: intermediate
order: 2
---

# Custom Exceptions

Python allows you to define your own exception classes by inheriting from `Exception`.

## Raising Exceptions

Use the `raise` statement to raise an exception.

```python
age = 15

if age < 18:
    raise Exception("Must be at least 18 years old.")
```

## Raising Built-in Exceptions

```python
marks = -5

if marks < 0:
    raise ValueError("Marks cannot be negative.")
```

## Creating a Custom Exception

```python
class InvalidAgeError(Exception):
    pass
```

## Using a Custom Exception

```python
class InvalidAgeError(Exception):
    pass

age = 15

if age < 18:
    raise InvalidAgeError("Age must be at least 18.")
```

## Handling a Custom Exception

```python
class InvalidAgeError(Exception):
    pass

try:
    age = 16

    if age < 18:
        raise InvalidAgeError("Invalid age.")

except InvalidAgeError as error:
    print(error)
```

## Custom Exception with Constructor

```python
class InvalidSalaryError(Exception):

    def __init__(self, salary):
        super().__init__(f"Invalid salary: {salary}")
```

```python
salary = -500

if salary < 0:
    raise InvalidSalaryError(salary)
```

## Example

```python
def withdraw(balance, amount):

    if amount > balance:
        raise ValueError("Insufficient balance.")

    return balance - amount

print(withdraw(1000, 200))
```

## Practice

1. Create an `InvalidEmailError`.
2. Raise an exception for negative numbers.
3. Handle your custom exception.
4. Validate user input using `raise`.