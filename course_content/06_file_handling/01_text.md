---
title: Text Files
level: intermediate
order: 1
---

# Text Files

Python provides the built-in `open()` function to read from and write to text files.

## Opening a File

```python
file = open("notes.txt", "r")
```

## Reading an Entire File

```python
file = open("notes.txt", "r")

content = file.read()

print(content)

file.close()
```

## Reading Line by Line

```python
file = open("notes.txt", "r")

for line in file:
    print(line.strip())

file.close()
```

## Reading All Lines

```python
file = open("notes.txt", "r")

lines = file.readlines()

print(lines)

file.close()
```

## Writing a File

```python
file = open("notes.txt", "w")

file.write("Hello Python")

file.close()
```

> Opening a file with `"w"` overwrites its existing contents.

## Appending to a File

```python
file = open("notes.txt", "a")

file.write("\nLearning file handling.")

file.close()
```

## Using `with`

Using `with` automatically closes the file.

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

## Writing Multiple Lines

```python
lines = [
    "Python\n",
    "Java\n",
    "Go\n"
]

with open("languages.txt", "w") as file:
    file.writelines(lines)
```

## File Modes

| Mode | Description |
|------|-------------|
| `r` | Read |
| `w` | Write (overwrite) |
| `a` | Append |
| `x` | Create new file |
| `r+` | Read and write |

## Practice

1. Create a text file.
2. Write your name into it.
3. Append another line.
4. Read and print the contents.
5. Print the file line by line.