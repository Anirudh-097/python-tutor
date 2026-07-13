---
title: If Else
level: beginner
order: 1
---

# If Else

The `if` statement executes code only when a condition is `True`.

## if

```python
age = 20

if age >= 18:
    print("Adult")
```

## if else

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## if elif else

```python
score = 75

if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 50:
    print("C")
else:
    print("Fail")
```

## Multiple Conditions

```python
age = 22

if age >= 18 and age <= 30:
    print("Eligible")
```

## Truthy Values

```python
if "Python":
    print("Executed")

if []:
    print("Won't execute")
```

## Practice

1. Check whether a number is positive or negative.
2. Find the largest of two numbers.
3. Print grades based on marks.