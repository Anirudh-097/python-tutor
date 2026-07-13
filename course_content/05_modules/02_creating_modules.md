---
title: Creating Modules
level: intermediate
order: 2
---

# Creating Modules

Any Python file (`.py`) can be used as a module.

## Example Structure

```text
project/
│
├── main.py
└── calculator.py
```

## calculator.py

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

## Import Module

```python
import calculator

print(calculator.add(5, 3))
print(calculator.subtract(10, 4))
```

## Import Specific Function

```python
from calculator import add

print(add(20, 30))
```

## Module Variables

```python
# config.py

APP_NAME = "My App"
VERSION = "1.0"
```

```python
import config

print(config.APP_NAME)
```

## Module Execution

Every module has a special variable called `__name__`.

```python
print(__name__)
```

When executed directly:

```text
__main__
```

When imported:

```text
calculator
```

## Using `if __name__ == "__main__"`

```python
def greet():
    print("Hello")

if __name__ == "__main__":
    greet()
```

This ensures the code only runs when the file is executed directly, not when imported.

## Practice

1. Create a module containing multiplication and division functions.
2. Import the module into another file.
3. Add constants to a module.
4. Use `if __name__ == "__main__"`.