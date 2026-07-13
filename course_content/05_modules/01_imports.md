---
title: Importing Modules
level: intermediate
order: 1
---

# Importing Modules

A module is a Python file containing functions, variables, and classes. You can import modules to reuse code instead of writing everything yourself.

## Import a Module

```python
import math

print(math.sqrt(25))
```

## Import Multiple Modules

```python
import math
import random

print(math.pi)
print(random.randint(1, 10))
```

## Import Specific Functions

```python
from math import sqrt, pi

print(sqrt(16))
print(pi)
```

## Import Everything

```python
from math import *

print(sqrt(49))
```

> Avoid `import *` in real projects because it can make code harder to read.

## Module Alias

```python
import math as m

print(m.factorial(5))
```

## Function Alias

```python
from math import sqrt as square_root

print(square_root(64))
```

## Built-in Modules

### math

```python
import math

print(math.ceil(4.2))
print(math.floor(4.8))
print(math.pow(2, 5))
```

### random

```python
import random

print(random.randint(1, 100))
print(random.choice(["red", "green", "blue"]))
```

### datetime

```python
from datetime import datetime

print(datetime.now())
```

## Check Available Members

```python
import math

print(dir(math))
```

## Practice

1. Import the `math` module and calculate the square root of 100.
2. Generate a random number between 1 and 50.
3. Import `pi` directly from `math`.
4. Use an alias while importing a module.