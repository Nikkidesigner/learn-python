# Python Data Types

Python is a dynamically typed language, meaning you don’t need to declare a variable’s type explicitly. The type is determined at runtime. This document provides a detailed explanation of Python's built-in data types, including examples.

## 1. Numeric Data Types
Python supports the following numeric types:

- **Integer (`int`)**: Whole numbers (e.g., `1`, `42`, `-999`).
- **Floating Point (`float`)**: Numbers with decimals (e.g., `3.14`, `-0.01`).
- **Complex (`complex`)**: Numbers with a real and imaginary part (e.g., `5+6j`).

### Examples:
```python
x = 10       # int
y = 20.5     # float
z = 3 + 4j   # complex
print(type(x), type(y), type(z))
```

## 2. Boolean Data Type (`bool`)
Booleans represent truth values: `True` and `False`.

### Example:
```python
is_python_fun = True
print(type(is_python_fun))
```

## 3. String Data Type (`str`)
Strings are sequences of characters enclosed in quotes.

### Example:
```python
s = "Hello, Python!"
print(s[0])      # H
print(s[1:5])    # ello
print(s * 2)     # Hello, Python!Hello, Python!
print(s + " Rocks!")
```

## 4. Sequence Data Types
### 4.1 List (`list`)
Lists are mutable, ordered collections of elements.

### Example:
```python
my_list = [1, "Python", 3.14]
print(my_list[0])   # 1
my_list.append("New")
print(my_list)
```

### 4.2 Tuple (`tuple`)
Tuples are immutable, ordered collections.

### Example:
```python
my_tuple = (10, "Hello", 5.5)
print(my_tuple[1])  # Hello
```

### 4.3 Range (`range`)
Used for generating sequences of numbers.

### Example:
```python
for i in range(1, 5):
    print(i)
```

## 5. Binary Data Types
### 5.1 Bytes (`bytes`)
Immutable sequences of bytes.
```python
b = bytes([65, 66, 67])
print(b)  # b'ABC'
```

### 5.2 Bytearray (`bytearray`)
Mutable sequence of bytes.
```python
ba = bytearray([65, 66, 67])
ba[0] = 68
print(ba)  # bytearray(b'DBC')
```

### 5.3 Memoryview (`memoryview`)
Used to view the memory of byte objects.
```python
d = bytearray("hello", 'utf-8')
view = memoryview(d)
print(view)
```

## 6. Dictionary Data Type (`dict`)
Dictionaries store key-value pairs.
```python
my_dict = {"name": "John", "age": 30}
print(my_dict["name"])  # John
```

## 7. Set Data Types
### 7.1 Set (`set`)
Unordered, unique collection of elements.
```python
my_set = {1, 2, 3, 4}
print(my_set)
```

### 7.2 Frozen Set (`frozenset`)
Immutable version of a set.
```python
f_set = frozenset([1, 2, 3])
print(f_set)
```

## 8. None Type (`NoneType`)
Represents a null value or absence of value.
```python
x = None
print(type(x))  # <class 'NoneType'>
```

## 9. Type Conversion
Python provides built-in functions for type conversion.

```python
x = int("10")      # Converts string to int
y = float(5)       # Converts int to float
z = str(100)       # Converts int to string
print(type(x), type(y), type(z))
```

## 10. F-Strings in Python
F-strings (formatted string literals) provide a concise and readable way to embed expressions and variables inside strings.

### Example:
```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

### Benefits of F-Strings:
- **Readability & Simplicity**: More concise compared to `.format()` and `%` formatting.
- **Performance**: Faster execution.
- **Supports Inline Expressions**: You can evaluate expressions inside `{}`.
- **Handles Quotes Easily**.
- **Used in Date Formatting**:

```python
import datetime
today = datetime.datetime.today()
print(f"Today's date is {today:%B %d, %Y}.")
```

- **Access Dictionary Values**:
```python
user = {'name': 'Bob', 'age': 25}
print(f"User {user['name']} is {user['age']} years old.")  
```

### Printing Braces in F-Strings:
```python
print(f"{{Hello, Geek}}")  # Output: {Hello, Geek}
```

## Conclusion
Python offers a rich set of built-in data types and formatting tools, like f-strings, that enhance code readability and efficiency.

---

Feel free to contribute or add more examples!

