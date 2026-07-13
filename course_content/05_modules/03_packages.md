---
title: Packages
level: intermediate
order: 3
---

# Packages

A package is a directory that contains multiple related Python modules.

Packages help organize large projects.

## Example Structure

```text
project/
│
├── main.py
│
└── utils/
    ├── __init__.py
    ├── math_utils.py
    └── string_utils.py
```

## math_utils.py

```python
def square(x):
    return x * x
```

## string_utils.py

```python
def greet(name):
    return f"Hello {name}"
```

## Import a Module

```python
from utils import math_utils

print(math_utils.square(5))
```

## Import Functions

```python
from utils.math_utils import square

print(square(10))
```

## Import Multiple Modules

```python
from utils import math_utils
from utils import string_utils

print(math_utils.square(4))
print(string_utils.greet("Alice"))
```

## Package Initialization

`__init__.py` marks a directory as a package.

Example:

```python
# utils/__init__.py

print("Package loaded")
```

It can also expose commonly used functions.

```python
from .math_utils import square
from .string_utils import greet
```

Now you can write:

```python
from utils import square, greet

print(square(6))
print(greet("Bob"))
```

## Relative Imports

```python
from .math_utils import square
```

The `.` refers to the current package.

## Good Project Structure

```text
project/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── product.py
│
├── services/
│   ├── __init__.py
│   └── auth.py
│
└── utils/
    ├── __init__.py
    ├── file.py
    └── string.py
```

## Practice

1. Create a package named `utils`.
2. Add two modules inside it.
3. Import functions from both modules.
4. Expose selected functions using `__init__.py`.