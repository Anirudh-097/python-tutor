---
title: Variables
level: beginner
order: 1
---

# Variables

A variable is a name (identifier) that refers to a value stored in memory. Variables allow you to store data and reuse it throughout your program.

Variables are created when you assign a value using the `=` operator.

## Example

```python
x = 5
print(x)
```

Output

```text
5
```

## Creating Variables

```python
name = "Alice"
age = 25
height = 5.6
is_student = True
```

## Reassigning Variables

```python
count = 10
print(count)

count = 20
print(count)
```

## Multiple Assignment

```python
x, y, z = 1, 2, 3

print(x)
print(y)
print(z)
```

Assign the same value:

```python
a = b = c = 100

print(a)
print(b)
print(c)
```

## Dynamic Typing

Variables can refer to different types.

```python
value = 100
print(type(value))

value = "Hello"
print(type(value))
```

## Naming Rules

Valid

```python
student_name = "John"
_age = 20
price2 = 50
```

Invalid

```python
2name = "John"
student-name = "John"
first name = "John"
```

## Best Practices

Good

```python
student_age = 18
total_marks = 450
```

Avoid

```python
x = 18
a = 450
```

## Practice

1. Create variables for your name, age, and city.
2. Print all variables.
3. Change the value of one variable and print it again.
4. Assign three variables in one line.