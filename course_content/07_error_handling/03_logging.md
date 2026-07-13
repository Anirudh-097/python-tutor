---
title: Logging
level: beginner
order: 3
---

# Logging

The `logging` module records information about a program while it runs.

Unlike `print()`, logging provides different levels of messages and can write to files.

## Basic Logging

```python
import logging

logging.warning("This is a warning.")
```

## Logging Levels

```python
import logging

logging.debug("Debug")
logging.info("Information")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")
```

Levels from lowest to highest:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

## Configure Logging

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application started.")
```

## Log to a File

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Program started.")
logging.error("Something went wrong.")
```

## Custom Log Format

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logging.warning("Disk space is low.")
```

Example output

```text
WARNING - Disk space is low.
```

## Include Timestamp

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Application started.")
```

## Logging Exceptions

```python
import logging

try:
    print(10 / 0)

except ZeroDivisionError:
    logging.exception("An error occurred.")
```

`logging.exception()` automatically includes the stack trace.

## Logger Object

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Application started.")
logger.warning("Low memory.")
```

## When to Use Logging

Use `print()` for quick debugging while learning.

Use `logging` in real applications because it:

- Supports log levels
- Can write to files
- Can include timestamps
- Can record stack traces
- Can be configured for production

## Practice

1. Log messages using every log level.
2. Save logs to a file.
3. Create a custom log format.
4. Log an exception using `logging.exception()`.