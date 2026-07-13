---
title: String Slicing
level: beginner
order: 6
---

# String Slicing

Strings are sequences of characters. You can access individual characters or slices using indexes.

```python
text = "Python"
```

## Indexing

```python
print(text[0])
```

```python
print(text[-1])
```

## Slicing

```python
print(text[0:2])
```

```python
print(text[2:])
```

```python
print(text[:4])
```

```python
print(text[:])
```

## Step

```python
print(text[::2])
```

```python
print(text[::-1])
```

## Examples

```python
word = "Programming"

print(word[:6])
print(word[3:8])
print(word[-4:])
```

## Practice

1. Print the first character.
2. Print the last character.
3. Reverse a string.
4. Print every second character.