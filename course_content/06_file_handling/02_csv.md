---
title: CSV Files
level: intermediate
order: 2
---

# CSV Files

CSV (Comma-Separated Values) files store tabular data.

Python provides the built-in `csv` module.

## Writing CSV

```python
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 20])
    writer.writerow(["Bob", 22])
```

## Reading CSV

```python
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

## Dictionary Writer

```python
import csv

with open("employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "salary"]
    )

    writer.writeheader()

    writer.writerow({
        "name": "Alice",
        "salary": 50000
    })

    writer.writerow({
        "name": "Bob",
        "salary": 60000
    })
```

## Dictionary Reader

```python
import csv

with open("employees.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["salary"])
```

## Custom Delimiter

```python
import csv

with open("data.csv") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        print(row)
```

## Practice

1. Create a CSV containing student details.
2. Read every row.
3. Use `DictWriter`.
4. Read data using `DictReader`.