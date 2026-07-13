---
title: Pytest
level: advanced
order: 2
---

# Pytest

Pytest is a popular Python testing framework.

It is simpler and more powerful than `unittest`.

Install:

```bash
pip install pytest
```

## Test File Naming

Pytest automatically discovers files:

```
test_*.py
*_test.py
```

Example:

```
project/

├── calculator.py
└── test_calculator.py
```

## Simple Test

`calculator.py`

```python
def add(a, b):
    return a + b
```

`test_calculator.py`

```python
from calculator import add


def test_add():

    result = add(2, 3)

    assert result == 5
```

## Running Tests

Run:

```bash
pytest
```

Example output:

```text
1 passed
```

## Multiple Tests

```python
def test_add():

    assert add(1, 2) == 3


def test_add_negative():

    assert add(-1, -2) == -3
```

## Fixtures

Fixtures provide reusable test data.

```python
import pytest


@pytest.fixture
def numbers():

    return [1, 2, 3]
```

Using fixture:

```python
def test_sum(numbers):

    assert sum(numbers) == 6
```

## Fixture Setup

```python
@pytest.fixture
def database():

    db = create_database()

    yield db

    db.close()
```

Code after `yield` is cleanup.

## Parametrize Tests

Run the same test with multiple values.

```python
import pytest


@pytest.mark.parametrize(
    "number,result",
    [
        (2, 4),
        (3, 9),
        (4, 16)
    ]
)
def test_square(number, result):

    assert number * number == result
```

## Testing Exceptions

```python
import pytest


def divide(a, b):

    if b == 0:
        raise ValueError()

    return a / b


def test_divide_error():

    with pytest.raises(ValueError):

        divide(10, 0)
```

## Markers

Mark special tests.

```python
@pytest.mark.slow
def test_large_operation():

    pass
```

Run:

```bash
pytest -m slow
```

## Useful Commands

Run all tests:

```bash
pytest
```

Verbose output:

```bash
pytest -v
```

Specific file:

```bash
pytest test_math.py
```

Stop after first failure:

```bash
pytest -x
```

## Practice

1. Rewrite unittest examples using pytest.
2. Create fixtures for common data.
3. Use parametrized tests.
4. Create custom pytest markers.