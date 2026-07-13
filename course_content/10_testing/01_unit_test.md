---
title: Unit Testing
level: advanced
order: 1
---

# Unit Testing

Unit testing is the process of testing individual parts of a program, such as functions or classes.

Python provides the built-in `unittest` module.

## Why Write Tests?

Tests help to:

- Find bugs early
- Prevent breaking existing code
- Document expected behavior
- Refactor code safely

## Example Function

Create a file:

```
calculator.py
```

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

## Creating a Test

Create:

```
test_calculator.py
```

```python
import unittest

from calculator import add, subtract


class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(2, 3)

        self.assertEqual(result, 5)


    def test_subtract(self):
        result = subtract(5, 3)

        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
```

## Running Tests

Run:

```bash
python -m unittest test_calculator.py
```

Output:

```text
..
----------------------------------------------------------------------
Ran 2 tests
OK
```

## Common Assertions

### assertEqual

```python
self.assertEqual(2 + 2, 4)
```

### assertNotEqual

```python
self.assertNotEqual(5, 10)
```

### assertTrue

```python
self.assertTrue(True)
```

### assertFalse

```python
self.assertFalse(False)
```

### assertIsNone

```python
self.assertIsNone(None)
```

## Testing Exceptions

```python
def divide(a, b):

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b
```

Test:

```python
def test_divide_error(self):

    with self.assertRaises(ValueError):
        divide(10, 0)
```

## Setup and Teardown

`setUp()` runs before every test.

```python
class TestExample(unittest.TestCase):

    def setUp(self):
        self.value = 10


    def test_value(self):
        self.assertEqual(self.value, 10)
```

`tearDown()` runs after every test.

```python
def tearDown(self):
    print("Cleaning up")
```

## Testing Classes

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
```

Test:

```python
class TestAccount(unittest.TestCase):

    def test_deposit(self):

        account = BankAccount(100)

        account.deposit(50)

        self.assertEqual(
            account.balance,
            150
        )
```

## Practice

1. Write tests for calculator functions.
2. Test a class with multiple methods.
3. Test exceptions using `assertRaises()`.
4. Create setup data using `setUp()`.