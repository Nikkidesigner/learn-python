
# Learn Python with codewidnikki                                         


![image](https://github.com/user-attachments/assets/85402c30-bce6-4c5c-b75f-6778867ff61b)    

## What is Python ? 

Python refers to the Python programming language (with syntax rules for 
writing what is considered valid Python code) and the Python interpreter 
software that reads source code (written in the Python language) and performs its instructions. 

The Python interpreter is free to download from 
http://python.org/, and there are versions for Linux, OS X, and Windows. 


The name Python comes from the surreal British comedy group Monty 
Python, not from the snake. 

Python programmers are affectionately called 
Pythonistas, and both Monty Python and serpentine references usually prefer Python tutorials and documentation.


![image](https://github.com/user-attachments/assets/87806b4d-f9b7-4559-9e94-4db46ba9e753)   


Python was developed by Guido van Rossum (a Dutch programmer) in the late 1980s and early nineties at the National Research Institute for Mathematics and Computer Science in the Netherlands.


 ## Here’s a brief rundown of what you’ll find in each chapter:
**Part I: Python Programming Basics**


- Chapter 1: Python Basics Covers expressions, the most basic type of Python instruction, and how to use the Python interactive shell software to experiment with code.
- Chapter 2: Flow Control Explains how to make programs decide which instructions to execute so your code can intelligently respond to different conditions.
- Chapter 3: Functions Instructs you on how to define your own functions so that you can organize your code into more manageable chunks.
- Chapter 4: Lists Introduces the list data type and explains how to organize data.
- Chapter 5: Dictionaries and Structuring Data Introduces the dictionary data type and shows you more powerful ways to organize data.
- Chapter 6: Manipulating Strings Covers working with text data (called strings in Python).

# Applications : 

Python is a general-purpose programming language suitable for the development of a wide range of software applications. Over the last few years, Python has become the preferred language of choice for developers in various application areas, including:

- Data Science
- Machine Learning
- Web Development
- Computer Vision and Image Processing
- Embedded Systems and IoT
- Job Scheduling and Automation
- Desktop GUI Applications
- Console-based Applications
- CAD Applications
- Game Development
 

<img src="https://github.com/user-attachments/assets/7b755817-2cc3-44f1-834b-ef68076b7149" height = "200" width="200" />
<img src="https://github.com/user-attachments/assets/138f2902-e2e3-477e-b51f-6dba19a85840" height = "200" width="200" />
<img src="https://github.com/user-attachments/assets/afd21545-d1dd-4a13-bd56-f0ac07edb484" height = "200" width="200" />
<img src="https://github.com/user-attachments/assets/8ba41baf-7bb4-421f-b8b9-7055e230a0c3" height = "200" width="200" />





## Application Areas

### Data Science

- Python's rise in popularity is largely due to its data science libraries.
- Essential libraries include:
  - **NumPy**
  - **Pandas**
  - **Matplotlib**
- Distributions like **Anaconda** and **ActiveState** bundle essential libraries for data science.
- Python helps companies generate business insights from large datasets.

### Machine Learning

- Libraries such as **Scikit-learn** and **TensorFlow** are used for building predictive models.
- Applications include:
  - Medical diagnosis
  - Statistical arbitrage
  - Sales prediction
- Learn Python in-depth with real-world projects through certification courses.

### Web Development

- Popular frameworks include:
  - **Django**
  - **Pyramid**
  - **Flask**
- Supports asynchronous programming for high-performance web apps and APIs.

### Computer Vision and Image Processing

- **OpenCV** is widely used for image capturing and processing.
- Applications include:
  - Face detection
  - Pattern recognition
- Used in robotics, industrial surveillance, and biometrics.

### Embedded Systems and IoT

- **Micropython** is a lightweight version for microcontrollers like Arduino.
- Popular for automation products and robotics.
- **Raspberry Pi** is a low-cost single-board computer used for various applications.

### Job Scheduling and Automation

- Python automates CRON jobs for tasks like periodic data backups.
- Many software products, like **Maya**, embed Python APIs for automation scripts.

### Desktop GUI Applications

- Python is ideal for building user-friendly desktop applications.
- Popular GUI libraries include:
  - **Tkinter**
  - **wxPython**
  - **PyQt**
  - **PyGTK**
  - **PySimpleGUI**
  - **Jython**

### Console-based Applications

- Python is used to build CLI applications for tasks like database backups.
- Libraries for command-line argument parsing include:
  - **argparse**
  - **Click**
  - **Typer**
  - **Textual**

### CAD Applications

- Python automates repetitive tasks in CAD software.
- Notable software with Python APIs:
  - **Autodesk Fusion 360**
  - **SolidWorks**
  - **CATIA**

### Game Development

- Popular games built with Python include:
  - **BattleField2**
  - **The Sims 4**
  - **World of Tanks**
- Libraries for game development:
  - **Pygame**: Open-source library for multimedia applications.
  - **Kivy**: Supports multi-touch and runs on various platforms.
  - **PyKyra**: Fast game development framework supporting multiple multimedia formats.


## Conclusion

Python's versatility and extensive libraries make it a powerful choice for a wide range of applications, from data science to game development. Whether you're automating tasks, developing web applications, or creating games, Python provides the tools and frameworks necessary to succeed.



# Python Interpreter

Python is an interpreter-based language, which means that Python code is executed line by line. This document provides an overview of how the Python interpreter works in both interactive and scripted modes.

## Installation

- **Linux**: The Python executable is typically installed in the `/usr/bin/` directory.
- **Windows**: The executable (`python.exe`) is found in the installation folder (e.g., `C:\python311`).

## How Python Interpreter Works

![image](https://github.com/user-attachments/assets/20702ee2-7de5-47a0-b34c-69f54f239d67)

The Python interpreter consists of two main components:

1. **Translator**: Checks the syntax of the code. If the syntax is correct, it generates intermediate bytecode.
2. **Python Virtual Machine (PVM)**: Converts the bytecode into native binary and executes it.

### Diagram of Python Interpreter Mechanism

```
[Python Code] --> [Translator] --> [Bytecode] --> [PVM] --> [Native Binary Execution]
```

## Python Interpreter Modes

### Interactive Mode

When launched from a command line terminal without any additional options, the Python prompt (`>>>`) appears. The interpreter operates on the principle of REPL (Read, Evaluate, Print, Loop). Each command entered is read, translated, and executed.

**Example of an Interactive Session:**

```python
>>> price = 100
>>> qty = 5
>>> total = price * qty
>>> total
500
>>> print("Total =", total)
Total = 500
```

To exit the interactive session, you can:
- Enter the end-of-line character (`Ctrl+D` for Linux, `Ctrl+Z` for Windows).
- Type `quit()` and press Enter.

```python
>>> quit()
$
```

The standard interactive shell lacks features like line editing, history search, and auto-completion. For enhanced functionality, consider using advanced interactive interpreters like **IPython** or **bpython**.

### Scripting Mode

In scripting mode, you can save a set of instructions in a text file with a `.py` extension and execute it as a command line parameter.

**Example Script (`prog.py`):**

```python
print("My first program")
price = 100
qty = 5
total = price * qty
print("Total =", total)
```

**Execution on Windows:**

```bash
C:\Users\Acer>python prog.py
My first program
Total = 500
```

Python executes the script line by line, even though it appears to run the entire script at once. If an error occurs, the interpreter stops executing at that point.

**Example with Error:**

```python
print("My first program")
price = 100
qty = 5
total = prive * qty  # Error in this statement
print("Total =", total)
```

**Execution Result:**

```bash
C:\Users\Acer>python prog.py
My first program
Traceback (most recent call last):
  File "C:\Python311\prog.py", line 4, in <module>
    total = prive * qty
    ^^^^^
NameError: name 'prive' is not defined. Did you mean: 'price'?
```

### Using Shebang (#!)

You can make a Python script self-executable in Linux by adding a shebang line at the top of the script. This line indicates which executable should be used to interpret the script.

**Modified Script (`prog.py`):**

```python
#! /usr/bin/python3.11

print("My first program")
price = 100
qty = 5
total = price * qty
print("Total =", total)
```

To mark the script as self-executable, use the `chmod` command:

```bash
$ chmod +x prog.py
```

You can now execute the script directly:

```bash
$ ./prog.py
```

## Interactive Python - IPython

**IPython** is an enhanced interactive environment for Python, offering many features compared to the standard Python shell. It was developed by Fernando Perez in 2001.

### Key Features of IPython:

- **Object Introspection**: Check properties of an object during runtime.
- **Syntax Highlighting**: Helps identify language elements like keywords and variables.
- **History Management**: Stores interaction history for easy reproduction.
- **Tab Completion**: Autocompletes keywords, variables, and function names.
- **Magic Commands**: Control the Python environment and perform OS tasks.

### Installation

Install IPython using pip:

```bash
pip3 install ipython
```

### Launching IPython

To launch IPython from the command line:

```bash
C:\Users\Acer>ipython
```

You will see a prompt that looks like this:

```
Python 3.11.2 (tags/v3.11.2:878ead1, Feb 7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
IPython 8.4.0 -- An enhanced Interactive Python. Type '?' for help.
In [1]:
```

### IPython Prompts

- **In [n]**: Appears before any input expression.
- **Out [n]**: Appears before the output.

**Example Session in IPython:**

```python
In [1]: price = 100
In [2]: quantity = 5
In [3]: total = price * quantity
In [4]: total
Out[4]: 500
```

### Additional Features

- **Tab Completion**: Provides a list of methods when you press the tab key.
- **Introspection**: Use `?` to get information about an object.

**Example:**

```python
In [5]: var = "Hello World"
In [6]: var?
```

### Running OS Commands

You can run OS commands directly in IPython using the `!` prefix:

```python
In [8]: !dir *.exe
```

## Conclusion

The Python interpreter provides a flexible environment for executing Python code, whether interactively or through scripts. With tools like IPython, you can enhance your coding experience with additional features that improve productivity and ease of use.


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

# Python Format Specifiers

Python provides various format specifiers to format strings, numbers, dates, and other data types efficiently. These specifiers are commonly used in f-strings, `str.format()`, and the `printf`-style `%` formatting.

## 1. String Formatting Specifiers
| Specifier | Description | Example Output |
|-----------|-------------|----------------|
| `%s` | String format | `'Hello'` |
| `%c` | Single character | `'A'` |
| `%r` | String representation (uses `repr()`) | `"'Hello'"` |
| `%a` | ASCII representation | `'Hello'` |

### Example:
```python
name = "Alice"
print("Hello, %s!" % name)  # Output: Hello, Alice!
```

## 2. Integer Formatting Specifiers
| Specifier | Description | Example Output |
|-----------|-------------|----------------|
| `%d` | Decimal (Integer) | `42` |
| `%i` | Integer | `42` |
| `%o` | Octal number | `0o52` |
| `%x` | Hexadecimal (lowercase) | `0x2a` |
| `%X` | Hexadecimal (uppercase) | `0X2A` |

### Example:
```python
num = 42
print("Decimal: %d, Octal: %o, Hex: %x" % (num, num, num))
```

## 3. Floating-Point Formatting Specifiers
| Specifier | Description | Example Output |
|-----------|-------------|----------------|
| `%f` | Floating point (default 6 decimals) | `3.140000` |
| `%.nf` | Floating point (n decimal places) | `3.14` for `%.2f` |
| `%e` | Exponential notation (lowercase) | `3.14e+00` |
| `%E` | Exponential notation (uppercase) | `3.14E+00` |
| `%g` | Uses `%e` or `%f` (whichever is shorter) | `3.14` |
| `%G` | Uses `%E` or `%f` (whichever is shorter) | `3.14` |

### Example:
```python
pi = 3.14159
print("Pi: %.2f" % pi)  # Output: Pi: 3.14
```

## 4. Date and Time Formatting Specifiers
Python uses the `datetime` module for date formatting.

| Specifier | Description | Example Output |
|-----------|-------------|----------------|
| `%Y` | Year (4 digits) | `2025` |
| `%y` | Year (last 2 digits) | `25` |
| `%m` | Month (zero-padded) | `02` |
| `%B` | Full month name | `February` |
| `%b` | Abbreviated month name | `Feb` |
| `%d` | Day (zero-padded) | `08` |
| `%A` | Full weekday name | `Monday` |
| `%a` | Abbreviated weekday name | `Mon` |
| `%H` | Hour (24-hour) | `14` |
| `%I` | Hour (12-hour) | `02` |
| `%p` | AM/PM | `PM` |
| `%M` | Minutes | `30` |
| `%S` | Seconds | `45` |

### Example:
```python
import datetime
now = datetime.datetime.now()
print(f"Today's date: {now:%B %d, %Y}")  # Output: February 18, 2025
```

## 5. Miscellaneous Formatting Specifiers
| Specifier | Description | Example Output |
|-----------|-------------|----------------|
| `%u` | Unsigned integer | `42` |
| `%n` | Platform-specific newline | `\n` or `\r\n` |
| `%%` | Literal percent sign | `%` |

### Example:
```python
percentage = 85
print("Your score: %d%%" % percentage)  # Output: Your score: 85%
```

## Conclusion
Python format specifiers allow precise control over how values are displayed. Whether working with strings, numbers, or dates, mastering these specifiers helps in formatting output effectively.

---

# Python Type Casting

Type casting in Python refers to the process of converting an object of one data type into another. This is particularly useful when you have data of one type but need to use it in another form. Python supports two types of casting: **implicit** and **explicit**.

## Types of Type Casting

### 1. Implicit Casting

Implicit casting, also known as automatic casting, occurs when the Python interpreter automatically converts one data type to another without explicit instruction from the programmer. Python is a strongly typed language, meaning it does not allow automatic type conversion between unrelated data types. For example, a string cannot be converted to a number type automatically. However, an integer can be cast into a float.

#### Example of Implicit Casting

```python
a = 10        # int object
b = 10.5      # float object
c = a + b     # Implicitly converts 'a' to float
print(c)      # Output: 20.5
```

In this example, the integer `a` is implicitly converted to a float to perform the addition with `b`.

### 2. Explicit Casting

Explicit casting requires the programmer to specify the conversion using built-in functions. Python provides several functions for explicit type casting, including `int()`, `float()`, and `str()`.

#### Python `int()` Function

The `int()` function converts a value to an integer. It can convert a float to an integer, a string with a valid integer representation, or a boolean value.

```python
a = int(10.5)  # Converts float to int
print(a)       # Output: 10

b = int("100") # Converts string to int
print(b)       # Output: 100

c = int(True)  # Converts boolean to int
print(c)       # Output: 1
```

#### Python `float()` Function

The `float()` function converts a value to a float. It can convert an integer, a string with a valid floating-point representation, or a boolean value.

```python
a = float(10)      # Converts int to float
print(a)           # Output: 10.0

b = float("9.99")  # Converts string to float
print(b)           # Output: 9.99
```

#### Python `str()` Function

The `str()` function converts a value to a string. It can convert integers, floats, and other objects to their string representation.

```python
a = str(10)        # Converts int to string
print(a)           # Output: '10'

b = str(3.14)      # Converts float to string
print(b)           # Output: '3.14'
```

## Conversion of Sequence Types

Python's sequence types include lists, tuples, and strings. You can convert between these types using built-in functions.

### List to Tuple and String

```python
a = [1, 2, 3, 4, 5]  # List Object
b = tuple(a)         # Convert list to tuple
print(b)             # Output: (1, 2, 3, 4, 5)

c = "Hello"          # String Object
d = list(c)         # Convert string to list
print(d)             # Output: ['H', 'e', 'l', 'l', 'o']
```

### Tuple to List and String

```python
e = (1, 2, 3, 4, 5)  # Tuple Object
f = list(e)          # Convert tuple to list
print(f)             # Output: [1, 2, 3, 4, 5]

g = str(e)           # Convert tuple to string
print(g)             # Output: '(1, 2, 3, 4, 5)'
```

## Conclusion

Python's type casting feature allows for the conversion of one data type to another using built-in functions. Understanding how to use implicit and explicit casting effectively can enhance your programming skills and improve the flexibility of your code. Whether you're converting numbers, strings, or sequences, Python provides the tools necessary to handle data types efficiently.


