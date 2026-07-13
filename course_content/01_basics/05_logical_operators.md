---
title: Logical Operators
level: beginner
order: 5
---

# Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning |
|-----------|---------|
| and | Both conditions must be True |
| or | At least one condition is True |
| not | Reverse the result |

## and

```python
age = 20

print(age >= 18 and age <= 30)
```

## or

```python
print(True or False)
```

```python
print(5 > 10 or 8 > 3)
```

## not

```python
print(not True)
```

```python
print(not 5 > 3)
```

## Combining Conditions

```python
username = "admin"
password = "1234"

print(username == "admin" and password == "1234")
```

## Practice

1. Check whether a number is between 1 and 100.
2. Check if someone is eligible to vote.
3. Use `not` to reverse a condition.