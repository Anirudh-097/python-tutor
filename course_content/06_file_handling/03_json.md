---
title: JSON Files
level: intermediate
order: 3
---

# JSON Files

JSON (JavaScript Object Notation) is commonly used to exchange data between applications.

Python provides the built-in `json` module.

## Python Dictionary

```python
student = {
    "name": "Alice",
    "age": 20,
    "marks": [90, 85, 95]
}
```

## Convert to JSON String

```python
import json

text = json.dumps(student)

print(text)
```

## Pretty Printing

```python
import json

print(json.dumps(student, indent=4))
```

## Convert JSON to Dictionary

```python
import json

text = '{"name":"Alice","age":20}'

data = json.loads(text)

print(data["name"])
```

## Write JSON File

```python
import json

student = {
    "name": "Alice",
    "age": 20
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

## Read JSON File

```python
import json

with open("student.json") as file:
    data = json.load(file)

print(data)
```

## Nested JSON

```python
employee = {
    "name": "Bob",
    "address": {
        "city": "London",
        "zip": 10001
    }
}

print(employee["address"]["city"])
```

## Practice

1. Create a dictionary.
2. Save it as JSON.
3. Read the JSON file.
4. Convert a JSON string into a dictionary.