---
title: String Methods
level: beginner
order: 7
---

# String Methods

Python provides many built-in methods for working with strings.

```python
text = "hello world"
```

## Uppercase

```python
print(text.upper())
```

## Lowercase

```python
print(text.lower())
```

## Title

```python
print(text.title())
```

## Capitalize

```python
print(text.capitalize())
```

## Replace

```python
print(text.replace("world", "Python"))
```

## Split

```python
print(text.split())
```

## Join

```python
words = ["Learn", "Python"]

print(" ".join(words))
```

## Strip

```python
text = "  hello  "

print(text.strip())
```

## Startswith

```python
print(text.startswith("he"))
```

## Endswith

```python
print(text.endswith("lo"))
```

## Find

```python
print(text.find("ll"))
```

## Count

```python
print(text.count("l"))
```

## Practice

1. Convert a sentence to uppercase.
2. Replace one word with another.
3. Count the occurrences of a character.
4. Split a sentence into words.