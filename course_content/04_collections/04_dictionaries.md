---
title: Dictionaries
level: intermediate
order: 4
---

# Dictionaries

A dictionary stores data as key-value pairs.

## Creating Dictionaries

```python
student = {
    "name": "Alice",
    "age": 20
}

print(student)
```

## Accessing Values

```python
print(student["name"])
```

```python
print(student.get("age"))
```

## Adding Items

```python
student["city"] = "London"

print(student)
```

## Updating Values

```python
student["age"] = 21

print(student)
```

## Removing Items

```python
student.pop("age")

print(student)
```

```python
del student["name"]
```

## Keys

```python
student = {
    "name": "Bob",
    "age": 25
}

print(student.keys())
```

## Values

```python
print(student.values())
```

## Items

```python
print(student.items())
```

## Iterating

```python
for key in student:
    print(key)
```

```python
for value in student.values():
    print(value)
```

```python
for key, value in student.items():
    print(key, value)
```

## Dictionary Comprehension

```python
squares = {
    x: x * x
    for x in range(5)
}

print(squares)
```

## Nested Dictionaries

```python
students = {
    "101": {
        "name": "Alice",
        "age": 20
    },
    "102": {
        "name": "Bob",
        "age": 22
    }
}

print(students["101"]["name"])
```

## Practice

1. Create a dictionary for a student.
2. Add a new key.
3. Update an existing value.
4. Iterate through all key-value pairs.
5. Create a dictionary of numbers and their squares.