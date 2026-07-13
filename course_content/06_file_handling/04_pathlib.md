---
title: Working with pathlib
level: intermediate
order: 4
---

# pathlib

The `pathlib` module provides an object-oriented way to work with files and directories.

It is recommended over using string paths.

## Creating a Path

```python
from pathlib import Path

path = Path("notes.txt")

print(path)
```

## Current Directory

```python
from pathlib import Path

print(Path.cwd())
```

## Home Directory

```python
from pathlib import Path

print(Path.home())
```

## Check if File Exists

```python
from pathlib import Path

path = Path("notes.txt")

print(path.exists())
```

## Check File Type

```python
from pathlib import Path

path = Path("notes.txt")

print(path.is_file())
print(path.is_dir())
```

## File Name

```python
from pathlib import Path

path = Path("documents/report.pdf")

print(path.name)
print(path.stem)
print(path.suffix)
```

Output

```text
report.pdf
report
.pdf
```

## Join Paths

```python
from pathlib import Path

path = Path("documents") / "images" / "photo.png"

print(path)
```

## Create Directory

```python
from pathlib import Path

Path("output").mkdir(exist_ok=True)
```

## Iterate Files

```python
from pathlib import Path

for file in Path(".").iterdir():
    print(file)
```

## Find Python Files

```python
from pathlib import Path

for file in Path(".").glob("*.py"):
    print(file)
```

## Read File

```python
from pathlib import Path

text = Path("notes.txt").read_text()

print(text)
```

## Write File

```python
from pathlib import Path

Path("hello.txt").write_text("Hello Python")
```

## Practice

1. Print the current working directory.
2. Create a folder named `data`.
3. List all `.py` files in a directory.
4. Read a file using `Path.read_text()`.
5. Write a text file using `Path.write_text()`.