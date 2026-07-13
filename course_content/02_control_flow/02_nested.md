---
title: Nested Conditions
level: beginner
order: 2
---

# Nested Conditions

An `if` statement can contain another `if` statement.

## Example

```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
```

## Example

```python
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Unknown user")
```

## Practice

1. Check age and citizenship.
2. Check username and password.
3. Check marks and attendance.