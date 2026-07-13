---
title: Match Statement
level: beginner
order: 3
---

# Match Statement

Python 3.10 introduced the `match` statement for pattern matching.

## Example

```python
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Unknown")
```

## Multiple Values

```python
grade = "A"

match grade:
    case "A" | "B":
        print("Pass")
    case "C":
        print("Average")
    case _:
        print("Fail")
```

## Practice

1. Print month names.
2. Create a simple calculator using `match`.