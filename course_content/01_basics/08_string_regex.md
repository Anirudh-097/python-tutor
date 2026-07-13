---
title: Introduction to Regular Expressions
level: beginner
order: 8
---

# Regular Expressions

Regular expressions (regex) are patterns used to search, match, and extract text.

Python provides the `re` module.

```python
import re
```

## Search

```python
text = "Python 3.13"

match = re.search(r"\d+", text)

print(match.group())
```

## Find All Numbers

```python
import re

text = "10 20 30"

print(re.findall(r"\d+", text))
```

## Match Beginning

```python
import re

print(re.match(r"Python", "Python is fun"))
```

## Check Email Pattern

```python
import re

email = "user@example.com"

print(bool(re.match(r".+@.+\..+", email)))
```

## Replace

```python
import re

text = "apple banana apple"

print(re.sub("apple", "orange", text))
```

## Common Patterns

| Pattern | Meaning |
|---------|---------|
| `.` | Any character |
| `\d` | Digit |
| `\w` | Letter, digit or underscore |
| `\s` | Whitespace |
| `+` | One or more |
| `*` | Zero or more |
| `?` | Optional |

## Practice

1. Extract all numbers from a string.
2. Replace every space with `_`.
3. Check whether a string starts with `"Hello"`.
4. Count all digits in a string.