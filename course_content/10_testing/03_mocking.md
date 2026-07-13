---
title: Mocking
level: advanced
order: 3
---

# Mocking

Mocking replaces real objects with fake objects during testing.

Mocks are useful when testing code that depends on:

- APIs
- Databases
- Files
- External services
- Time-based operations

Python provides the `unittest.mock` module.

## Basic Mock

```python
from unittest.mock import Mock


service = Mock()

service.get_data()

print(service.get_data.called)
```

Output:

```text
True
```

## Setting Return Values

```python
from unittest.mock import Mock


api = Mock()

api.get_user.return_value = {
    "name": "Alice"
}


print(api.get_user())
```

## Mocking a Function

Example:

```python
def get_weather():

    return "Sunny"
```

Test:

```python
from unittest.mock import patch


@patch("weather.get_weather")
def test_weather(mock_weather):

    mock_weather.return_value = "Rainy"

    result = get_weather()

    assert result == "Rainy"
```

## Checking Calls

```python
mock = Mock()

mock.send("hello")

mock.send.assert_called_once_with(
    "hello"
)
```

## Mocking Classes

```python
from unittest.mock import Mock


database = Mock()

database.save.return_value = True


result = database.save("data")

print(result)
```

## MagicMock

`MagicMock` supports Python magic methods.

```python
from unittest.mock import MagicMock


mock = MagicMock()

mock.__len__.return_value = 10


print(len(mock))
```

## Side Effects

Return different values.

```python
from unittest.mock import Mock


mock = Mock()

mock.side_effect = [
    1,
    2,
    3
]


print(mock())
print(mock())
print(mock())
```

## Example: Mocking API Calls

Real code:

```python
import requests


def get_user():

    response = requests.get(
        "https://api.example.com/user"
    )

    return response.json()
```

Test:

```python
from unittest.mock import patch


@patch("requests.get")
def test_get_user(mock_get):

    mock_get.return_value.json.return_value = {
        "id": 1
    }

    result = get_user()

    assert result["id"] == 1
```

## When to Mock

Use mocking when:

- A dependency is slow
- A service is unavailable
- You need predictable results
- Testing error conditions

Avoid mocking simple logic that can be tested directly.

## Practice

1. Mock a database connection.
2. Mock an API request.
3. Verify a function was called.
4. Use `side_effect` to simulate failures.