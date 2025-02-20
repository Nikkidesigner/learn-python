
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


# **Concept of Local and Global Variables in Python**
In Python, **variables** can be classified into two main types based on their **scope**:

1. **Global Variables**:  
   - Declared outside a function or block.
   - Can be accessed inside and outside functions.
   - Can be modified inside functions using the `global` keyword.

2. **Local Variables**:  
   - Declared inside a function.
   - Only accessible within that function.
   - Created when the function is called and destroyed when the function ends.

---

## **Access Rules for Local and Global Variables**
1. **A local variable is only accessible inside the function where it is defined.**
2. **A global variable is accessible anywhere in the program unless shadowed by a local variable.**
3. **A function can modify a global variable using the `global` keyword.**
4. **A function can access (but not modify) a global variable without using `global`.**
5. **Using the same name for a local and a global variable creates two separate variables (variable shadowing).**
6. **Nested functions can access variables from their enclosing functions using `nonlocal`.**

---

## **10 Examples to Understand Local and Global Variables**

### **1. Simple Example of a Global Variable**
```python
x = 10  # Global variable

def display():
    print(x)  # Accessing global variable

display()  # Output: 10
print(x)   # Output: 10
```

---

### **2. Simple Example of a Local Variable**
```python
def example():
    y = 20  # Local variable
    print(y)  # Accessible inside function

example()  # Output: 20
# print(y)  # ❌ Error: NameError: 'y' is not defined (y is local)
```

---

### **3. Local and Global Variable with the Same Name (Variable Shadowing)**
```python
a = 50  # Global variable

def test():
    a = 100  # Local variable (shadows global 'a')
    print("Inside function:", a)

test()  # Output: Inside function: 100
print("Outside function:", a)  # Output: Outside function: 50
```

---

### **4. Modifying a Global Variable Inside a Function Using `global`**
```python
b = 30  # Global variable

def modify():
    global b  # Declaring that we are modifying the global variable
    b = 60
    print("Inside function:", b)

modify()  
print("Outside function:", b)  # Output: 60 (global variable changed)
```

---

### **5. Accessing a Global Variable Inside a Function Without `global`**
```python
c = 5  # Global variable

def display():
    print("Inside function:", c)  # Allowed (reading global variable)

display()  # Output: Inside function: 5
print("Outside function:", c)  # Output: Outside function: 5
```

---

### **6. Trying to Modify a Global Variable Without `global` (Will Cause an Error)**
```python
d = 15  # Global variable

def change():
    d = d + 5  # ❌ UnboundLocalError (Python treats 'd' as a local variable here)
    print(d)

# change()  # Uncommenting this line will cause an error
```
✅ **Fix:** Use `global d` inside the function before modifying `d`.

---

### **7. Using `nonlocal` to Modify a Variable in an Enclosing Function**
```python
def outer():
    e = 10  # Enclosing function variable
    
    def inner():
        nonlocal e  # Modify the 'e' from outer function
        e += 5
        print("Inside inner function:", e)

    inner()
    print("Inside outer function:", e)

outer()
# Output:
# Inside inner function: 15
# Inside outer function: 15
```

---

### **8. Global and Local Variables in Nested Functions**
```python
f = 100  # Global variable

def outer():
    f = 200  # Local variable in 'outer'
    
    def inner():
        f = 300  # Local variable in 'inner'
        print("Inner function:", f)  # 300

    inner()
    print("Outer function:", f)  # 200

outer()
print("Global scope:", f)  # 100
```

---

### **9. Using `global` Inside a Nested Function**
```python
g = "Hello"  # Global variable

def outer():
    global g  # Now we are modifying the global 'g'
    g = "Hi"

outer()
print(g)  # Output: Hi
```

---

### **10. Function Using Both Global and Local Variables**
```python
h = 500  # Global variable

def mixed():
    global h
    h = h + 100  # Modifying global variable
    local_var = 300  # Local variable
    print("Inside function:", h, local_var)

mixed()  # Output: Inside function: 600 300
print("Outside function:", h)  # Output: 600
# print(local_var)  # ❌ NameError: 'local_var' is not defined (it's local)
```

---

## **Summary**
| Concept | Description |
|---------|-------------|
| **Global Variable** | Declared outside functions, accessible everywhere. |
| **Local Variable** | Declared inside a function, only accessible within that function. |
| **Variable Shadowing** | A local variable with the same name as a global variable hides the global one. |
| **`global` Keyword** | Used inside a function to modify a global variable. |
| **`nonlocal` Keyword** | Used to modify a variable from an enclosing function. |
| **Access Rule 1** | Global variables can be accessed inside functions (unless shadowed). |
| **Access Rule 2** | Local variables cannot be accessed outside their function. |
| **Access Rule 3** | Modifying a global variable inside a function requires `global`. |
| **Access Rule 4** | `nonlocal` allows modifying variables in an outer function (not global). |



# What is the Unicode System?

In today's globalized world, software applications often need to display messages and outputs in a variety of languages, including but not limited to English, French, Japanese, Hebrew, and Hindi. To facilitate this, Python's string type utilizes the Unicode Standard for representing characters, enabling programs to work seamlessly with a diverse range of characters.

## Understanding Characters and Unicode

A character is defined as the smallest possible component of a text. For instance, 'A', 'B', 'C', and other symbols like 'È' and 'Í' are all distinct characters. Unicode is a universal character encoding standard that assigns a unique number, known as a code point, to each character. These code points range from 0 to 0x10FFFF (1,114,111 in decimal). 

A Unicode string is essentially a sequence of these code points. However, to store these code points in memory, they must be represented as a set of code units, which are then mapped to 8-bit bytes. This mapping is crucial for the efficient storage and retrieval of characters in various applications.

## Character Encoding

Character encoding refers to the rules and methods used to translate a Unicode string into a sequence of bytes. The most common types of encodings are:

- **UTF-8**: A variable-length encoding that can represent any character in the Unicode standard. It uses one to four bytes for each character.
- **UTF-16**: Uses one or two 16-bit code units to represent characters. It is more efficient for languages that use a lot of characters outside the ASCII range.
- **UTF-32**: Uses a fixed length of 4 bytes for each character, making it simple but less memory-efficient.

The "UTF" in these encodings stands for "Unicode Transformation Format."

## Python's Unicode Support

Starting from Python 3.0, there is built-in support for Unicode. The `str` type in Python contains Unicode characters, meaning that any string created using single, double, or triple-quoted string syntax is stored as Unicode. The default encoding for Python source code is UTF-8, which allows for a wide range of characters to be represented.

### Unicode Representation in Strings

In Python, you can represent Unicode characters in two ways:
1. Literal representation (e.g., "3/4")
2. Unicode value representation (e.g., "\u00BE")

### Example of Unicode Representation

```python
# Example of Unicode representation
var = "3/4"
print(var)  # Output: 3/4

var = "\u00BE"
print(var)  # Output: ¾
```

In the above example, the string '10' is stored using the Unicode values of '1' and '0', which are represented as `\u0031` and `\u0030`, respectively.

```python
# Example of Unicode values
var = "\u0031\u0030"
print(var)  # Output: 10
```

## Encoding and Decoding

Strings display text in a human-readable format, while bytes store characters as binary data. The process of converting data from a character string to a series of bytes is known as **encoding**. Conversely, **decoding** translates bytes back into human-readable characters and symbols. 

It is important to note that these two methods are distinct:
- `encode` is a method of the string object.
- `decode` is a method of the Python byte object.

### Example of Encoding and Decoding

In the following example, we have a string variable that consists of ASCII characters. ASCII is a subset of the Unicode character set. The `encode()` method is used to convert it into a bytes object.

```python
# Example of encoding and decoding
string = "Hello"
tobytes = string.encode('utf-8')  # Convert string to bytes
print(tobytes)  # Output: b'Hello'

string = tobytes.decode('utf-8')  # Convert bytes back to string
print(string)  # Output: Hello
```

### Example with Unicode Characters

In this example, we will store the Rupee symbol (₹) using its Unicode value, convert the string to bytes, and then back to a string.

```python
# Example with Unicode character
string = "\u20B9"  # Unicode for Rupee symbol
print(string)  # Output: ₹

tobytes = string.encode('utf-8')  # Convert to bytes
print(tobytes)  # Output: b'\xe2\x82\xb9'

string = tobytes.decode('utf-8')  # Convert back to string
print(string)  # Output: ₹
```

## Conclusion

The Unicode system is essential for modern software applications that need to handle multiple languages and character sets. Python's built-in support for Unicode allows developers to work with a wide range of characters seamlessly. Understanding how to encode and decode strings is crucial for ensuring that text is displayed correctly across different platforms and languages. By leveraging Unicode, Python enables developers to create applications that are truly global in nature.


# Python Operators

Python operators are special symbols used to perform specific operations on one or more operands. The operands can be variables, values, or expressions. This README provides a comprehensive overview of the various types of operators available in Python, including arithmetic, comparison, assignment, logical, bitwise, membership, and identity operators, along with their usage and examples.

## Key Terms Related to Python Operators

- **Unary Operators**: Operators that require a single operand to perform an operation.
- **Binary Operators**: Operators that require two operands to perform an operation.
- **Operands**: The variables, values, or expressions that are used with operators to perform operations.

## Types of Python Operators

Python operators can be categorized into the following types:

1. **Arithmetic Operators**
2. **Comparison (Relational) Operators**
3. **Assignment Operators**
4. **Logical Operators**
5. **Bitwise Operators**
6. **Membership Operators**
7. **Identity Operators**

---

## 1. Python Arithmetic Operators

Arithmetic operators are used to perform basic mathematical operations such as addition, subtraction, multiplication, and more. Below is a table summarizing the arithmetic operators:

| Operator | Name            | Example          |
|----------|-----------------|------------------|
| `+`      | Addition        | `a + b = 30`     |
| `-`      | Subtraction     | `a - b = -10`    |
| `*`      | Multiplication  | `a * b = 200`    |
| `/`      | Division        | `b / a = 2`      |
| `%`      | Modulus         | `b % a = 0`      |
| `**`     | Exponentiation   | `a ** b = 10**20`|
| `//`     | Floor Division   | `9 // 2 = 4`     |

### Example of Python Arithmetic Operators

```python
# Example of Arithmetic Operators
a = 21
b = 10
c = 0

c = a + b
print("a: {} b: {} a+b: {}".format(a, b, c))

c = a - b
print("a: {} b: {} a-b: {}".format(a, b, c))

c = a * b
print("a: {} b: {} a*b: {}".format(a, b, c))

c = a / b
print("a: {} b: {} a/b: {}".format(a, b, c))

c = a % b
print("a: {} b: {} a%b: {}".format(a, b, c))

a = 2
b = 3
c = a ** b
print("a: {} b: {} a**b: {}".format(a, b, c))

a = 10
b = 5
c = a // b
print("a: {} b: {} a//b: {}".format(a, b, c))
```

### Output

```
a: 21 b: 10 a+b: 31
a: 21 b: 10 a-b: 11
a: 21 b: 10 a*b: 210
a: 21 b: 10 a/b: 2.1
a: 21 b: 10 a%b: 1
a: 2 b: 3 a**b: 8
a: 10 b: 5 a//b: 2
```

---

## 2. Python Comparison Operators

Comparison operators compare the values on either side of them and determine the relationship among them. They are also called relational operators.

| Operator | Name                     | Example                |
|----------|--------------------------|------------------------|
| `==`     | Equal                    | `(a == b)` is false.   |
| `!=`     | Not equal                | `(a != b)` is true.    |
| `>`      | Greater than             | `(a > b)` is false.    |
| `<`      | Less than                | `(a < b)` is true.     |
| `>=`     | Greater than or equal to  | `(a >= b)` is false.   |
| `<=`     | Less than or equal to     | `(a <= b)` is true.    |

### Example of Python Comparison Operators

```python
# Example of Comparison Operators
a = 21
b = 10

if (a == b):
    print("Line 1 - a is equal to b")
else:
    print("Line 1 - a is not equal to b")

if (a != b):
    print("Line 2 - a is not equal to b")
else:
    print("Line 2 - a is equal to b")

if (a < b):
    print("Line 3 - a is less than b")
else:
    print("Line 3 - a is not less than b")

if (a > b):
    print("Line 4 - a is greater than b")
else:
    print("Line 4 - a is not greater than b")

# Swap values
a, b = b, a

if (a <= b):
    print("Line 5 - a is either less than or equal to b")
else:
    print("Line 5 - a is neither less than nor equal to b")

if (b >= a):
    print("Line 6 - b is either greater than or equal to b")
else:
    print("Line 6 - b is neither greater than nor equal to b")
```

### Output

```
Line 1 - a is not equal to b
Line 2 - a is not equal to b
Line 3 - a is not less than b
Line 4 - a is greater than b
Line 5 - a is either less than or equal to b
Line 6 - b is either greater than or equal to b
```

---

## 3. Python Assignment Operators

Assignment operators are used to assign values to variables. Below is a table summarizing the assignment operators:

| Operator | Example     | Same As          |
|----------|-------------|------------------|
| `=`      | `a = 10`    | `a = 10`         |
| `+=`     | `a += 30`   | `a = a + 30`     |
| `-=`     | `a -= 15`   | `a = a - 15`     |
| `*=`     | `a *= 10`   | `a = a * 10`     |
| `/=`     | `a /= 5`    | `a = a / 5`      |
| `%=`     | `a %= 5`    | `a = a % 5`      |
| `**=`    | `a **= 4`   | `a = a ** 4`     |
| `//=`    | `a //= 5`   | `a = a // 5`     |
| `&=`     | `a &= 5`    | `a = a & 5`      |
| `|=`     | `a |= 5`    | `a = a | 5`      |
| `^=`     | `a ^= 5`    | `a = a ^ 5`      |
| `>>=`    | `a >>= 5`   | `a = a >> 5`     |
| `<<=`    | `a <<= 5`   | `a = a << 5`     |

### Example of Python Assignment Operators

```python
# Example of Assignment Operators
a = 21
b = 10
c = 0
print("a: {} b: {} c : {}".format(a, b, c))

c = a + b
print("a: {}  c = a + b: {}".format(a, c))

c += a
print("a: {} c += a: {}".format(a, c))

c *= a
print("a: {} c *= a: {}".format(a, c))

c /= a
print("a: {} c /= a : {}".format(a, c))

c = 2
print("a: {} b: {} c : {}".format(a, b, c))
c %= a
print("a: {} c %= a: {}".format(a, c))

c **= a
print("a: {} c **= a: {}".format(a, c))

c //= a
print("a: {} c //= a: {}".format(a, c))
```

### Output

```
a: 21 b: 10 c : 0
a: 21  c = a + b: 31
a: 21 c += a: 52
a: 21 c *= a: 1092
a: 21 c /= a : 52.0
a: 21 b: 10 c : 2
a: 21 c %= a: 2
a: 21 c **= a: 2097152
a: 21 c //= a: 99864
```

---

## 4. Python Bitwise Operators

Bitwise operators work on bits and perform bit-by-bit operations. These operators are used to compare binary numbers.

| Operator | Name                | Example       |
|----------|---------------------|---------------|
| `&`      | AND                 | `a & b`       |
| `|`      | OR                  | `a | b`       |
| `^`      | XOR                 | `a ^ b`       |
| `~`      | NOT                 | `~a`          |
| `<<`     | Zero fill left shift| `a << 3`      |
| `>>`     | Signed right shift  | `a >> 3`      |

### Example of Python Bitwise Operators

```python
# Example of Bitwise Operators
a = 20            
b = 10            

print('a=', a, ':', bin(a), 'b=', b, ':', bin(b))
c = 0

c = a & b        
print("result of AND is ", c, ':', bin(c))

c = a | b     
print("result of OR is ", c, ':', bin(c))

c = a ^ b        
print("result of EXOR is ", c, ':', bin(c))

c = ~a           
print("result of COMPLEMENT is ", c, ':', bin(c))

c = a << 2       
print("result of LEFT SHIFT is ", c, ':', bin(c))

c = a >> 2       
print("result of RIGHT SHIFT is ", c, ':', bin(c))
```

### Output

```
a= 20 : 0b10100 b= 10 : 0b1010
result of AND is  0 : 0b0
result of OR is  30 : 0b11110
result of EXOR is  30 : 0b11110
result of COMPLEMENT is  -21 : -0b10101
result of LEFT SHIFT is  80 : 0b1010000
result of RIGHT SHIFT is  5 : 0b101
```

---

## 5. Python Logical Operators

Logical operators are used to combine two or more conditions and check the final result. The following logical operators are supported by Python:

| Operator | Name | Example |
|----------|------|---------|
| `and`    | AND  | `a and b` |
| `or`     | OR   | `a or b` |
| `not`    | NOT  | `not(a)` |

### Example of Python Logical Operators

```python
# Example of Logical Operators
var = 5

print(var > 3 and var < 10)  # True, because 5 is greater than 3 and less than 10
print(var > 3 or var < 4)     # True, because 5 is greater than 3
print(not (var > 3 and var < 10))  # False, because the expression inside is True
```

### Output

```
True
True
False
```

---

## 6. Python Membership Operators

Membership operators test for membership in a sequence, such as strings, lists, or tuples. They are useful for checking whether a value exists within a collection.

| Operator | Description | Example |
|----------|-------------|---------|
| `in`     | Returns True if it finds a variable in the specified sequence; False otherwise. | `a in b` |
| `not in` | Returns True if it does not find a variable in the specified sequence; False otherwise. | `a not in b` |

### Example of Python Membership Operators

```python
# Example of Membership Operators
a = 10
b = 20
my_list = [1, 2, 3, 4, 5]

print("a:", a, "b:", b, "list:", my_list)

if (a in my_list):
    print("a is present in the given list")
else:
    print("a is not present in the given list")

if (b not in my_list):
    print("b is not present in the given list")
else:
    print("b is present in the given list")

c = b / a
print("c:", c, "list:", my_list)
if (c in my_list):
    print("c is available in the given list")
else:
    print("c is not available in the given list")
```

### Output

```
a: 10 b: 20 list: [1, 2, 3, 4, 5]
a is not present in the given list
b is not present in the given list
c: 2.0 list: [1, 2, 3, 4, 5]
c is available in the given list
```

---

## 7. Python Identity Operators

Identity operators compare the memory locations of two objects. They are useful for determining whether two variables point to the same object in memory.

| Operator | Description | Example |
|----------|-------------|---------|
| `is`     | Returns True if both variables are the same object; False otherwise. | `a is b` |
| `is not` | Returns True if both variables are not the same object; False otherwise. | `a is not b` |

### Example of Python Identity Operators

```python
# Example of Identity Operators
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

print(a is c)          # True, because c points to the same object as a
print(a is b)          # False, because a and b are different objects

print(a is not c)      # False, because c points to the same object as a
print(a is not b)      # True, because a and b are different objects
```

### Output

```
True
False
False
True
```

---

## Python Operators Precedence

Operator precedence determines the order in which operators are evaluated in an expression. Python operators have different levels of precedence, which affects how expressions are calculated. The following table lists operators from highest to lowest precedence:

| Sr.No. | Operator & Description |
|--------|------------------------|
| 1      | `**` Exponentiation (raise to the power) |
| 2      | `~ + -` Complement, unary plus and minus |
| 3      | `* / % //` Multiply, divide, modulo, and floor division |
| 4      | `+ -` Addition and subtraction |
| 5      | `>> <<` Right and left bitwise shift |
| 6      | `&` Bitwise 'AND' |
| 7      | `^ |` Bitwise exclusive `OR` and regular `OR` |
| 8      | `<= < > >=` Comparison operators |
| 9      | `<> == !=` Equality operators |
| 10     | `= %= /= //= -= += *= **=` Assignment operators |
| 11     | `is is not` Identity operators |
| 12     | `in not in` Membership operators |
| 13     | `not or and` Logical operators |

Understanding operator precedence is crucial for writing correct and efficient Python code, as it affects how expressions are evaluated and can lead to different results based on the order of operations.

---

## Conclusion

Python provides a rich set of operators that allow for various operations on data. Understanding logical, membership, and identity operators, along with operator precedence, is essential for effective programming in Python. By mastering these operators, you can create more complex and efficient code that handles a wide range of scenarios.



# Python Numeric and Math-Related Functions

Python provides a rich set of numeric and math-related functions that are essential for performing mathematical operations, statistical calculations, and random number generation. This README covers various categories of functions available in Python's `math` module, including theoretic and representation functions, power and logarithmic functions, trigonometric functions, angular conversion functions, mathematical constants, hyperbolic functions, special functions, random number functions, and built-in mathematical functions.

## 1. Theoretic and Representation Functions

The `math` module includes several theoretic and representation functions that perform various mathematical calculations. Below is a table summarizing these functions:

| Sr.No. | Function & Description |
|--------|------------------------|
| 1      | `math.ceil(x)` - The ceiling of x: the smallest integer not less than x. |
| 2      | `math.comb(n, k)` - Returns the number of ways to choose "k" items from "n" items without repetition and without order. |
| 3      | `math.copysign(x, y)` - Returns a float with the magnitude of x but the sign of y. |
| 4      | `math.cmp(x, y)` - Compares the values of two objects. **(Deprecated in Python 3)** |
| 5      | `math.fabs(x)` - Calculates the absolute value of a given number. |
| 6      | `math.factorial(n)` - Finds the factorial of a given integer. |
| 7      | `math.floor(x)` - Calculates the floor value of a given number. |
| 8      | `math.fmod(x, y)` - Returns the remainder of x with respect to y, providing more accurate results than the `%` operator. |
| 9      | `math.frexp(x)` - Calculates the mantissa and exponent of a given number. |
| 10     | `math.fsum(iterable)` - Returns the floating-point sum of all numeric items in an iterable (e.g., list, tuple). |
| 11     | `math.gcd(*integers)` - Calculates the greatest common divisor of all the given integers. |
| 12     | `math.isclose()` - Determines whether two numeric values are close to each other. |
| 13     | `math.isfinite(x)` - Determines whether the given number is finite. |
| 14     | `math.isinf(x)` - Determines whether the given value is infinity (positive or negative). |
| 15     | `math.isnan(x)` - Determines whether the given number is "NaN" (Not a Number). |
| 16     | `math.isqrt(n)` - Calculates the integer square root of the given non-negative integer. |
| 17     | `math.lcm(*integers)` - Calculates the least common multiple of the given integer arguments. |
| 18     | `math.ldexp(x, i)` - Returns the product of x and 2 raised to the power of i. |
| 19     | `math.modf(x)` - Returns the fractional and integer parts of x in a two-item tuple. |
| 20     | `math.nextafter(x, y)` - Returns the next floating-point value after x towards y. |
| 21     | `math.perm(n, k)` - Calculates the number of ways to choose k items from n items without repetition and with order. |
| 22     | `math.prod(iterable, *, start)` - Calculates the product of all numeric items in the iterable. |
| 23     | `math.remainder(x, y)` - Returns the remainder of x with respect to y. |
| 24     | `math.trunc(x)` - Returns the integral part of the number, removing the fractional part. |
| 25     | `math.ulp(x)` - Returns the value of the least significant bit of the float x. |

---

## 2. Power and Logarithmic Functions

The following functions are used for power and logarithmic calculations:

| Sr.No. | Function & Description |
|--------|------------------------|
| 1      | `math.cbrt(x)` - Calculates the cube root of a number. |
| 2      | `math.exp(x)` - Calculates the exponential of x: e^x. |
| 3      | `math.exp2(x)` - Returns 2 raised to the power of x. |
| 4      | `math.expm1(x)` - Returns e^x - 1. |
| 5      | `math.log(x)` - Calculates the natural logarithm of x (for x > 0). |
| 6      | `math.log1p(x)` - Returns the natural logarithm of 1 + x (base e). |
| 7      | `math.log2(x)` - Returns the base-2 logarithm of x. |
| 8      | `math.log10(x)` - Returns the base-10 logarithm of x (for x > 0). |
| 9      | `math.pow(x, y)` - Returns x raised to the power of y. |
| 10     | `math.sqrt(x)` - Returns the square root of x (for x > 0). |

---

## 3. Trigonometric Functions

Python includes several functions that perform trigonometric calculations:

| Sr.No. | Function & Description |
|--------|------------------------|
| 1      | `math.acos(x)` - Returns the arc cosine of x (in radians). |
| 2      | `math.asin(x)` - Returns the arc sine of x (in radians). |
| 3      | `math.atan(x)` - Returns the arc tangent of x (in radians). |
| 4      | `math.atan2(y, x)` - Returns atan(y / x) (in radians). |
| 5      | `math.cos(x)` - Returns the cosine of x (in radians). |
| 6      | `math.sin(x)` - Returns the sine of x (in radians). |
| 7      | `math.tan(x)` - Returns the tangent of x (in radians). |
| 8      | `math.hypot(x, y)` - Returns the Euclidean norm, sqrt(x*x + y*y). |

---

## 4. Angular Conversion Functions

The following functions are used for converting angles between radians and degrees:

| Sr.No. | Function & Description |
|--------|------------------------|
| 1      | `math.degrees(x)` - Converts the given angle from radians to degrees. |
| 2      | `math.radians(x)` - Converts the given angle from degrees to radians. |

---

## 5. Mathematical Constants

The Python `math` module defines several mathematical constants:

| Sr.No. | Constants & Description |
|--------|-------------------------|
| 1      | `math.pi` - Represents the mathematical constant pi (approximately 3.141592...). |
| 2      | `math.e` - Represents the mathematical constant e (approximately 2.718281...). |
| 3      | `math.tau` - Represents the mathematical constant Tau (τ), equivalent to 2π. |
| 4      | `math.inf` - Represents positive infinity. For negative infinity, use `-math.inf`. |
| 5      | `math.nan` - Represents a floating-point "not a number" (NaN) value. |

---

## 6. Hyperbolic Functions

Hyperbolic functions are analogs of trigonometric functions based on hyperbolas instead of circles. The following hyperbolic functions are available in the Python `math` module:

| Sr.No. | Function & Description |
|--------|------------------------|
| 1      | `math.acosh(x)` - Calculates the inverse hyperbolic cosine of the given value. |
| 2      | `math.asinh(x)` - Calculates the inverse hyperbolic sine of a given number. |
| 3      | `math.atanh(x)` - Calculates the inverse hyperbolic tangent of a number. |
| 4      | `math.cosh(x)` - Calculates the hyperbolic cosine of the given value. |
| 5      | `math.sinh(x)` - Calculates the hyperbolic sine of a given number. |
| 6      | `math.tanh(x)` - Calculates the hyperbolic tangent of a number. |

---

## 7. Special Functions

The following special functions are provided by the Python `math` module:

| Sr.No. | Function & Description |
|--------|------------------------|
| 1      | `math.erf(x)` - Returns the value of the Gauss error function for the given parameter. |
| 2      | `math.erfc(x)` - The complementary error function, equivalent to 1 - erf(x). |
| 3      | `math.gamma(x)` - Calculates the factorial of complex numbers, defined for all complex numbers except non-positive integers. |
| 4      | `math.lgamma(x)` - Calculates the natural logarithm of the absolute value of the Gamma function at x. |

---

## 8. Random Number Functions

Random numbers are used for games, simulations, testing, security, and privacy applications. The following functions are included in the random module:

| Sr.No. | Function & Description |
|--------|------------------------|
| 1      | `random.choice(seq)` - Returns a random item from a list, tuple, or string. |
| 2      | `random.randrange([start,] stop [,step])` - Returns a randomly selected element from range(start, stop, step). |
| 3      | `random.random()` - Returns a random float r, such that 0 <= r < 1. |
| 4      | `random.seed([x])` - Sets the integer starting value used in generating random numbers. |
| 5      | `random.shuffle(seq)` - Randomizes the items of the given sequence. |
| 6      | `random.uniform(a, b)` - Returns a random floating-point value r, such that a <= r < b. |

---

## 9. Built-in Mathematical Functions

Python includes several built-in mathematical functions that do not require importing from any module:

| Sr.No. | Function & Description |
|--------|------------------------|
| 1      | `abs(x)` - Returns the absolute value of x. |
| 2      | `max(*args)` - Returns the largest of its arguments or the largest number from an iterable. |
| 3      | `min(*args)` - Returns the smallest of its arguments or the smallest number from an iterable. |
| 4      | `pow(x, y)` - Returns x raised to the power of y (equivalent to x**y). |
| 5      | `round(x[, n])` - Returns x rounded to n digits from the decimal point. |
| 6      | `sum(iterable, /, start=0)` - Returns the sum of all numeric items in an iterable. |

---

## Conclusion

Python's `math` module and built-in functions provide a comprehensive set of tools for performing a wide range of mathematical operations, from basic arithmetic to complex calculations involving trigonometry and random number generation. Understanding these functions is essential for effective programming in Python, especially in fields that require mathematical computations, such as data analysis, scientific computing, and machine learning.

# Flow Control in Python

## Introduction

In Python, flow control statements determine the order in which individual instructions are executed. Instead of executing each line sequentially, programs can make decisions, repeat instructions, or jump to specific parts of the code. This makes programming powerful and flexible.

Flow control is broadly classified into:

1. **Decision Making Statements** (e.g., `if`, `elif`, `else`, `match`)
2. **Loops (Iteration Statements)** (e.g., `for`, `while`)
3. **Jump Statements** (e.g., `break`, `continue`, `pass`)
4. **Truthy and Falsey Values**

---

## 1. Decision Making Statements

### 1.1 The `if-elif-else` Statement

The `if` statement allows Python programs to execute different blocks of code based on conditions.

### **Example:**

```python
marks = 80
result = ""

if marks < 30:
    result = "Failed"
elif marks > 75:
    result = "Passed with distinction"
else:
    result = "Passed"

print(result)
```

**Output:**

```
Passed with distinction
```
Flowchart of if-else Statement


This flowchart shows how if-else statement is used −

![image](https://github.com/user-attachments/assets/b7eb565d-1a5f-4b93-8098-05a64a96ff09)

### 1.2 The `match-case` Statement

A Python match-case statement takes an expression and compares its value to successive patterns given as one or more case blocks. Only the first pattern that matches gets executed. It is also possible to extract components (sequence elements or object attributes) from the value into variables.



With the release of Python 3.10, a pattern matching technique called match-case has been introduced, which is similar to the switch-case construct available in C/C++/Java etc. Its basic use is to compare a variable against one or more values. It is more similar to pattern matching in languages like Rust or Haskell than a switch statement in C or C++..

### **Example:**

```python
def check_vowel(n):
    match n:
        case 'a' | 'e' | 'i' | 'o' | 'u':
            return "Vowel alphabet"
        case _:
            return "Simple alphabet"

print(check_vowel('a'))
print(check_vowel('m'))
print(check_vowel('o'))
```

**Output:**

```
Vowel alphabet
Simple alphabet
Vowel alphabet
```

---

## 2. Loops (Iteration Statements)

Loops allow repeated execution of a block of code until a condition is met.

### 2.1 `for` Loop

The `for` loop iterates over sequences like lists, tuples, and strings.

### **Example:**

```python
words = ["one", "two", "three"]
for x in words:
    print(x)
```

**Output:**

```
one
two
three
```

### 2.2 `while` Loop

The `while` loop executes as long as a condition is `True`.

### **Example:**

```python
i = 1
while i < 6:
    print(i)
    i += 1
```

**Output:**

```
1
2
3
4
5
```

---

## 3. Jump Statements

Jump statements are used to control the flow of loops.

### 3.1 The `break` Statement

The `break` statement stops the loop prematurely.

### **Example:**

```python
x = 0
while x < 10:
    print("x:", x)
    if x == 5:
        print("Breaking...")
        break
    x += 1

print("End")
```

**Output:**

```
x: 0
x: 1
x: 2
x: 3
x: 4
x: 5
Breaking...
End
```

### 3.2 The `continue` Statement

The `continue` statement skips the current iteration and moves to the next one.

### **Example:**

```python
for letter in "Python":
    if letter == "h":
        continue
    print("Current Letter:", letter)
```

**Output:**

```
Current Letter: P
Current Letter: y
Current Letter: t
Current Letter: o
Current Letter: n
```

### 3.3 The `pass` Statement

The `pass` statement is used as a placeholder for future code. It allows you to define empty loops, functions, or conditionals without throwing an error.

### **Example:**

```python
for i in range(5):
    if i == 3:
        pass  # Placeholder for future implementation
    else:
        print(i)
```

**Output:**
```
0
1
2
4
```

---

## 4. Truthy and Falsey Values

Python considers certain values as `True` or `False` when evaluated in conditions.

### **Falsey Values:**
- `0`, `0.0`, `''` (empty string), `None`, `[]` (empty list), `{}` (empty dictionary), `set()` (empty set), `False`

### **Truthy Values:**
- Any non-empty string, non-zero number, non-empty list/dictionary/set, `True`

### **Example:**
```python
name = ''
while not name:
    print('Enter your name:')
    name = input()

print('How many guests will you have?')
num_of_guests = int(input())

if num_of_guests:
    print('Be sure to have enough room for all your guests.')

print('Done')
```

### **Explanation:**
- If `name` is empty (`''`), the `while` loop continues asking for input.
- If `num_of_guests` is not `0`, the `if` statement executes and prints a message.

This approach makes the code cleaner compared to explicitly checking `name != ''` or `num_of_guests != 0`.

---

## Summary

- **Decision-making statements (`if-elif-else`, `match-case`)** help programs execute different code paths.
- **Loops (`for`, `while`)** allow repeated execution of statements.
- **Jump statements (`break`, `continue`, `pass`)** control loop execution flow.
- **Truthy and Falsey values** help in simplifying conditions in Python.

Mastering flow control is essential for writing efficient and logical Python programs!

---

Feel free to practice these examples and experiment with different conditions! 🚀

# **Advanced python concepts** 


# **Reading Files in Python – Understanding File Handling**  

In this lesson, we will explore how to **read files in Python** using the `open()` function. By the end, you will understand:  
✅ How to open and read files in Python.  
✅ The difference between **hard-coding** and dynamic file selection.  
✅ Why `argv` is useful when working with files.  
✅ How to properly close files.  

---

## **🚀 Understanding the `ex15.py` Script**  

### **📌 Code Breakdown**
Here’s the given script `ex15.py` with a **line-by-line explanation**:

```python
from sys import argv  # 1️⃣ Import argv from sys module.

script, filename = argv  # 2️⃣ Unpack command-line arguments.

txt = open(filename)  # 3️⃣ Open the file and store its reference in 'txt'.

print(f"Here's your file {filename}:")  # 4️⃣ Print message with file name.
print(txt.read())  # 5️⃣ Read and print the file’s contents.

print("Type the filename again:")  # 6️⃣ Ask the user to input the filename again.
file_again = input("> ")  # 7️⃣ Take filename input from the user.

txt_again = open(file_again)  # 8️⃣ Open the new file entered by the user.
print(txt_again.read())  # 9️⃣ Read and print the file's contents.
```

---

## **🔍 Line-by-Line Explanation**
| **Line** | **Explanation** |
|----------|----------------|
| **1** | `from sys import argv` – We import `argv`, which allows command-line arguments. |
| **2** | `script, filename = argv` – The script expects two inputs: the script name (`script`) and a filename (`filename`). |
| **3** | `txt = open(filename)` – The `open(filename)` command opens the file in **read mode** (default). It returns a file object, which we store in the `txt` variable. |
| **4** | `print(f"Here's your file {filename}:")` – Displays a message showing which file is being opened. |
| **5** | `print(txt.read())` – Calls the `.read()` method on the file object to read and print the entire file contents. |
| **6** | `print("Type the filename again:")` – Asks the user to manually enter the filename again. |
| **7** | `file_again = input("> ")` – Uses `input()` to take user input for another filename. |
| **8** | `txt_again = open(file_again)` – Opens the file specified by the user. |
| **9** | `print(txt_again.read())` – Reads and prints the file's contents. |

---

## **🛠 How to Run the Script?**
Since we use `argv`, this script should be run from the **terminal** or **command prompt** with an extra argument.  
Example:

```sh
python ex15.py ex15_sample.txt
```
### **📌 Output (If `ex15_sample.txt` contains these lines)**  
```
Here's your file ex15_sample.txt:
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

Type the filename again:
> ex15_sample.txt
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
```
---

## **💡 Important File Handling Concepts**
### **1️⃣ What is `open()` Doing?**
The `open()` function **returns a file object**, which allows us to perform operations like **reading, writing, or appending**.

Syntax:
```python
file = open("filename.txt", "mode")
```
📌 The **default mode** is `"r"` (**read mode**). Other modes:
| Mode | Meaning |
|------|---------|
| `"r"` | Read-only mode (default) |
| `"w"` | Write mode (overwrites file) |
| `"a"` | Append mode (adds to file) |
| `"x"` | Create mode (fails if file exists) |






---

### **2️⃣ Why Not "Hard-Code" the Filename?**
#### ❌ **Bad Practice (Hard-Coding)**
```python
txt = open("ex15_sample.txt")
```
- This forces the program to always open **only** `ex15_sample.txt`.  
- It **cannot work** for other files without modifying the script.

#### ✅ **Better Approach (Using `argv` or `input`)**
```python
filename = input("Enter the file name: ")
txt = open(filename)
```
- This allows users to enter **any file name**, making the program more flexible.

---

### **3️⃣ Why Do We Need `.read()`?**
The `.read()` method **reads the file contents** and returns it as a string.

Example:
```python
file = open("sample.txt")  
print(file.read())  # Prints all contents of the file
```

**Other File Methods:**
| Method | Function |
|--------|----------|
| `.read()` | Reads the entire file |
| `.readline()` | Reads one line at a time |
| `.readlines()` | Reads all lines into a list |

---

### **4️⃣ Closing Files - The Right Way**
After opening a file, **you must close it** to free system resources.

#### ✅ **Good Practice (Closing the File)**
```python
file = open("sample.txt")
print(file.read())
file.close()  # Close the file to free memory
```

#### ✅ **Better Practice (Using `with` Statement)**
```python
with open("sample.txt") as file:
    print(file.read())  # No need to manually close!
```
- **Automatic file closing!**
- Prevents accidental memory leaks.

---

## **🔥 Study Drills – Try These Exercises!**
1️⃣ **Rewrite each line in plain English to explain what it does.**  
2️⃣ **Modify the script to handle missing or incorrect filenames.**  
3️⃣ **Use `.readline()` instead of `.read()` to print one line at a time.**  
4️⃣ **Make the script ask for multiple filenames in a loop.**  

Would you like an advanced version that handles file errors? 🚀

Absolutely! Let’s dive deeper into **file handling in Python** and explore how to handle errors, improve the script, and make it more robust. By the end of this explanation, you’ll have a solid understanding of reading files, handling exceptions, and writing clean, efficient code.

---

## **🚀 Advanced File Handling with Error Handling**

When working with files, it’s crucial to handle potential errors gracefully. For example:
- What if the file doesn’t exist?
- What if the user provides an invalid filename?
- What if the file is corrupted or inaccessible?

Python provides a mechanism called **exception handling** to deal with such scenarios. Let’s enhance the `ex15.py` script to handle these cases.

---

### **📌 Updated Script with Error Handling**

Here’s the improved version of `ex15.py`:

```python
from sys import argv  # Import argv from sys module.

# Check if the correct number of arguments is provided.
if len(argv) != 2:
    print("Usage: python ex15.py <filename>")
    exit(1)

script, filename = argv  # Unpack command-line arguments.

try:
    # Open the file and read its contents.
    with open(filename, "r") as txt:
        print(f"Here's your file {filename}:")
        print(txt.read())  # Read and print the file’s contents.
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: Could not read the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Ask the user to input the filename again.
print("Type the filename again:")
file_again = input("> ")

try:
    # Open the new file entered by the user.
    with open(file_again, "r") as txt_again:
        print(txt_again.read())  # Read and print the file's contents.
except FileNotFoundError:
    print(f"Error: The file '{file_again}' does not exist.")
except IOError:
    print(f"Error: Could not read the file '{file_again}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

---

## **🔍 Explanation of the Updated Script**

### **1️⃣ Checking Command-Line Arguments**
```python
if len(argv) != 2:
    print("Usage: python ex15.py <filename>")
    exit(1)
```
- This ensures the user provides exactly one filename as an argument.
- If not, it prints a usage message and exits the script with an error code (`1`).

---

### **2️⃣ Using `try` and `except` for Error Handling**
The `try` block attempts to execute the code, and the `except` block catches any errors that occur.

#### **FileNotFoundError**
- This exception is raised if the file does not exist.
```python
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
```

#### **IOError**
- This exception is raised if the file cannot be read (e.g., due to permission issues).
```python
except IOError:
    print(f"Error: Could not read the file '{filename}'.")
```

#### **General Exception**
- This catches any other unexpected errors.
```python
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

---

### **3️⃣ Using `with` for Automatic File Closing**
```python
with open(filename, "r") as txt:
    print(txt.read())
```
- The `with` statement ensures the file is automatically closed after the block is executed, even if an error occurs.
- This eliminates the need to manually call `.close()`.

---

### **4️⃣ Handling User Input for Filenames**
The script asks the user to input the filename again and handles errors similarly:
```python
print("Type the filename again:")
file_again = input("> ")

try:
    with open(file_again, "r") as txt_again:
        print(txt_again.read())
except FileNotFoundError:
    print(f"Error: The file '{file_again}' does not exist.")
except IOError:
    print(f"Error: Could not read the file '{file_again}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

---

## **💡 Key Takeaways**

### **1️⃣ Why Use Error Handling?**
- Prevents the program from crashing due to unexpected issues.
- Provides meaningful feedback to the user.
- Makes the script more robust and user-friendly.

### **2️⃣ Why Use `with`?**
- Ensures files are properly closed, even if an error occurs.
- Reduces the risk of memory leaks.
- Makes the code cleaner and more readable.

### **3️⃣ Why Use `argv` and `input`?**
- `argv` allows dynamic file selection via command-line arguments.
- `input` allows the user to specify filenames interactively.
- Both approaches make the script more flexible and reusable.

---

## **🔥 Advanced Study Drills**

1️⃣ **Add a Loop for Multiple Files**
   - Modify the script to ask the user for multiple filenames in a loop until they type "quit".

2️⃣ **Implement File Writing**
   - Add functionality to write to a file. Use modes like `"w"` (write) or `"a"` (append).

3️⃣ **Create a File Explorer**
   - Build a script that lists all files in a directory and lets the user choose one to open.

4️⃣ **Handle Large Files**
   - Modify the script to read large files line by line using `.readline()` or iterate over the file object.

---

## **Example: Reading Large Files Line by Line**

Here’s how you can read a large file efficiently without loading the entire file into memory:

```python
filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        for line in file:  # Iterate over each line in the file.
            print(line, end="")  # Print the line (end="" prevents double-spacing).
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: Could not read the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

---



# **Writing to Files in Python**

## **Introduction**
Writing to a file in Python involves opening the file in a specific mode, writing data to it, and then closing the file to ensure that all data is saved and system resources are released. Python provides various file modes to handle different writing scenarios.

---

## **Opening a File for Writing**
The `open()` function is used to open a file and specify the mode in which the file should be accessed.

### **File Modes for Writing**
| Mode | Description |
|------|-------------|
| `"w"` | Write mode - Creates a new file or truncates an existing file before writing. |
| `"a"` | Append mode - Writes data at the end of the file without altering its existing content. |
| `"x"` | Exclusive creation mode - Fails if the file already exists. |
| `"wb"` | Binary write mode - Used for writing binary data. |
| `"w+"` | Read and write mode - Truncates the file before writing. |
| `"a+"` | Read and append mode - Preserves existing content and allows writing at the end. |

---

## **Writing to a File Using `write()`**
The `write()` method writes a string to the file.

### **Example: Writing to a New File**
```python
file = open("example.txt", "w")
file.write("Hello, World!\n")
file.write("This is a new line.\n")
file.close()
print("File written successfully!")
```
**Output in `example.txt`:**
```
Hello, World!
This is a new line.
```

### **Example: Appending to an Existing File**
```python
file = open("example.txt", "a")
file.write("Appending this line.\n")
file.close()
print("Data appended successfully!")
```
**Output in `example.txt` after execution:**
```
Hello, World!
This is a new line.
Appending this line.
```

---

## **File Handling in Python: Read, Write, Append, and Truncate**

This Python script demonstrates how to perform basic file operations, including **reading**, **writing**, **appending**, and **truncating** files. It also highlights best practices for file handling, such as using the `with` statement and handling file modes correctly.

---
```
#writing into a file 
from sys import argv
script , filename  = argv

with  open(filename,"w") as file_txt: 
    content = input(f"Enter the content to write in {filename} : \n")
    file_txt.write(content)
    file_txt.write("\n")
    print("File written successfully !")



  # truncating the file : goodbye 
print("Truncating the file ..........")
with open(filename,"w") as file_txt:
     file_txt.truncate()



#appending to an existing file :
with open(filename, "w") as file_txt:
    content = input(f"Enter the content to write in {filename}: \n")
    file_txt.write(content)
    file_txt.write("\n")  # Add a newline
    print("File written successfully!")



```
## **Script Overview**

The script performs the following tasks:
1. **Writes content to a file** (overwriting or creating a new file).
2. **Truncates the file** (clears its contents).
3. **Appends additional content** to the file.
4. **Closes the file** properly after each operation.

---

## **How It Works**

### **1. Writing to a File**
The script opens the file in **write mode (`"w"`)**. If the file already exists, it is overwritten. If it doesn’t exist, a new file is created. The user is prompted to enter content, which is then written to the file.

```python
with open(filename, "w") as file_txt:
    content = input(f"Enter the content to write in {filename}: \n")
    file_txt.write(content)
    file_txt.write("\n")  # Add a newline
    print("File written successfully!")
```

- **Key Points:**
  - The `"w"` mode automatically truncates the file (clears its contents) when opened.
  - The `.write()` method writes the user's input to the file.
  - A newline (`\n`) is added to ensure the content is properly formatted.

---

### **2. Truncating the File**
The script reopens the file in **write mode (`"w"`)** to truncate it. Truncating removes all content from the file, effectively clearing it.

```python
print("Truncating the file...")
with open(filename, "w") as file_txt:
    file_txt.truncate()  # Clear the file
```

- **Key Points:**
  - The `"w"` mode automatically truncates the file, so calling `.truncate()` is optional in this case.
  - Truncating is useful if you want to explicitly clear the file at a specific point.

---

### **3. Appending to the File**
The script opens the file in **append mode (`"a"`)**. In this mode, new content is added to the end of the file without affecting existing content. The user is prompted to enter additional content, which is appended to the file.

```python
with open(filename, "a") as file_txt:
    content = input(f"Enter the content to append in {filename}: \n")
    file_txt.write(content)
    file_txt.write("\n")  # Add a newline
    print("File appended successfully!")
```

- **Key Points:**
  - The `"a"` mode ensures that new content is added to the end of the file.
  - The file pointer is positioned at the end of the file, so `.write()` appends the content.

---

### **4. Closing the File**
The script uses the `with` statement to open files, which ensures that the file is **automatically closed** after the block of code is executed. This is a best practice to prevent memory leaks and ensure data integrity.

```python
with open(filename, "w") as file_txt:
    # Perform file operations
    ...
# File is automatically closed here
```

- **Key Points:**
  - The `with` statement is the recommended way to handle files in Python.
  - It eliminates the need to manually call `.close()`.

---

## **File Modes Explained**

| Mode | Description                                                                 |
|------|-----------------------------------------------------------------------------|
| `"r"` | **Read mode**: Opens the file for reading (default).                        |
| `"w"` | **Write mode**: Opens the file for writing. Overwrites the file if it exists or creates a new file if it doesn’t. |
| `"a"` | **Append mode**: Opens the file for appending. Adds content to the end of the file. |
| `"r+"`| **Read and write mode**: Opens the file for both reading and writing.       |
| `"w+"`| **Write and read mode**: Opens the file for writing and reading. Overwrites the file if it exists or creates a new file if it doesn’t. |
| `"a+"`| **Append and read mode**: Opens the file for appending and reading.         |

---

## **How to Run the Script**

1. Save the script as `file_handling.py`.
2. Open a terminal or command prompt.
3. Run the script with a filename as an argument:
   ```bash
   python file_handling.py example.txt
   ```
4. Follow the prompts to write, truncate, and append content to the file.

---

## **Example Output**

If the user provides the filename `example.txt` and inputs the following:

1. **Write Content:** `Hello, World!`
2. **Append Content:** `This is a new line.`

The file `example.txt` will contain:

```
This is a new line.
```

---

## **Best Practices**

1. **Use the `with` statement:**
   - Ensures files are properly closed, even if an error occurs.
   - Eliminates the need to manually call `.close()`.

2. **Choose the correct file mode:**
   - Use `"w"` for writing, `"a"` for appending, and `"r"` for reading.

3. **Handle errors gracefully:**
   - Use `try` and `except` blocks to handle file-related errors, such as `FileNotFoundError` or `IOError`.

4. **Avoid hardcoding filenames:**
   - Use command-line arguments (`argv`) or user input to make the script more flexible.

---

## **Study Drills**

1. **Add Error Handling:**
   - Modify the script to handle errors, such as missing files or invalid filenames.

2. **Read and Display File Content:**
   - Add functionality to read and display the file's content after writing or appending.

3. **Loop for Multiple Files:**
   - Allow the user to perform operations on multiple files in a loop.

4. **Experiment with Other Modes:**
   - Try using `"r+"`, `"w+"`, or `"a+"` modes to explore their behavior.



---

## **Writing Multiple Lines Using `writelines()`**
The `writelines()` method writes a list of strings to a file.

### **Example: Writing Multiple Lines**
```python
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)
print("Multiple lines written successfully!")
```

**Output in `example.txt`:**
```
First line
Second line
Third line
```

---

## **Writing Binary Data to a File**
To write binary data, use the `"wb"` mode.

### **Example: Writing Binary Data**
```python
with open('binary_file.bin', 'wb') as file:
    data = b"BinaryDataExample"
    file.write(data)
print("Binary data written successfully!")
```

### **Converting Text Strings to Binary Data**
```python
with open('binary_text.bin', 'wb') as file:
    data = "Hello World".encode('utf-8')
    file.write(data)
print("Text converted to binary and written successfully!")
```

---

## **Writing to a File in Read-Write Mode (`w+`)**
Using `w+` mode allows both reading and writing.

## Writing to a File in Reading and Writing Modes

When a file is opened for writing using 'w' or 'a', it is not possible to perform write operations at any earlier byte position in the file. The 'w+' mode, however, allows both reading and writing operations without closing the file. The `seek()` function is used to move the read/write pointer to any desired byte position within the file.

### Using the seek() Method
The `seek()` method is used to set the position of the read/write pointer within the file. The syntax for the `seek()` method is as follows:

```python
fileObject.seek(offset[, whence])
```

Where:

- **offset** − This is the position of the read/write pointer within the file.
- **whence** − This is optional and defaults to 0, which means absolute file positioning. Other values include:
  - **1** − Seek relative to the current position.
  - **2** − Seek relative to the file's end.

### Example 1: Modifying Part of a File
The following program demonstrates how to open a file in read-write mode ('w+'), write some data, seek a specific position, and then overwrite part of the file's content:

```python
# Open a file in read-write mode
fo = open("foo.txt", "w+")

# Write initial data to the file
fo.write("This is a rat race")

# Move the read/write pointer to the 10th byte
fo.seek(10, 0)

# Read 3 bytes from the current position
data = fo.read(3)
print("Read Data:", data)  # Output: "rat"

# Move the read/write pointer back to the 10th byte
fo.seek(10, 0)

# Overwrite the existing content with new text
fo.write('cat')

# Close the file
fo.close()
```

If we open the file in read mode (or seek to the starting position while in 'w+' mode) and read the contents, it will show the following:

```
This is a cat race
```

### Example 2: Appending Data and Using seek()
The 'a+' mode allows appending and reading data. However, it does not allow overwriting content unless `seek()` is used.

```python
# Open file in append and read mode
o_file = open("example.txt", "a+")

# Write initial content
o_file.write("Hello, world!\n")

# Move pointer to the beginning of the file
o_file.seek(0)

# Read content from the file
print("File Content:")
print(o_file.read())

# Move pointer to the beginning and write new content
o_file.seek(0)
o_file.write("Updated: ")

# Close file
o_file.close()
```

### Example 3: Reading and Writing a File Without Losing Data
Using 'r+' mode allows reading and writing without truncating the file.

```python
# Create and write to a file
with open("test.txt", "w") as file:
    file.write("Python file handling example\n")

# Open in read-write mode
with open("test.txt", "r+") as file:
    content = file.read()
    print("Before modification:")
    print(content)
    
    # Move pointer and modify content
    file.seek(7)
    file.write("file operations ")
    
    # Move pointer back to start and read again
    file.seek(0)
    print("After modification:")
    print(file.read())
```

**Output:**
```
Before modification:
Python file handling example
After modification:
Python file operations example
```

### Summary
- **`seek(offset, whence)`** adjusts the position of the file pointer.
- **Modes like `w+`, `a+`, and `r+`** allow different types of reading and writing.
- **Using `seek()` properly ensures you modify specific parts of a file without truncating it.**

These examples provide a deeper understanding of writing to a file while controlling the file pointer using `seek()`.

---

## **Handling File Writing Errors**
It is good practice to handle errors when working with files.

### **Example: Handling File Errors**
```python
try:
    with open("non_existent_folder/example.txt", "w") as file:
        file.write("Hello, World!")
except FileNotFoundError:
    print("Error: Directory does not exist.")
except PermissionError:
    print("Error: You do not have permission to write to this file.")
```

---

## **Summary**
✅ Use `open("filename", "w")` to write to a file (overwrites existing content).  
✅ Use `open("filename", "a")` to append data to a file.  
✅ Use `writelines()` to write multiple lines at once.  
✅ Use `wb` mode for writing binary data.  
✅ Use `seek()` to modify specific parts of a file.  
✅ Always handle file errors using `try-except`.  

---

## **Practice Exercises**
1️⃣ Write a Python program that creates a file and writes user input into it.  
2️⃣ Modify a text file by replacing a specific word using `seek()`.  
3️⃣ Create a binary file and write a list of numbers as binary data.  



# **Python Functions: A Comprehensive Guide**

## **Table of Contents**

1. [Introduction to Functions](#introduction-to-functions)
2. [Defining a Function](#defining-a-function)
3. [Calling a Function](#calling-a-function)
4. [Function Arguments](#function-arguments)
   - [Positional Arguments](#positional-arguments)
   - [Keyword Arguments](#keyword-arguments)
   - [Default Arguments](#default-arguments)
   - [Variable-length Arguments](#variable-length-arguments)
5. [Return Values](#return-values)
6. [Lambda Functions](#lambda-functions)
7. [Scope of Variables](#scope-of-variables)
8. [Practice Problems](#practice-problems)
9. [Real-world Use Cases](#real-world-use-cases)

---

## **1. Introduction to Functions**

A **function** in Python is a block of reusable code that performs a specific task. Functions help in organizing code, improving readability, and promoting code reuse. 

A Python function may be invoked from any other function by passing required data (called parameters or arguments). The called function returns its result back to the calling environment.

![image](https://github.com/user-attachments/assets/42ff5582-279e-480d-bd65-f87fe65110cf)


Python supports three types of functions:

1. **Built-in Functions**: Predefined functions like `print()`, `len()`, and `sum()`.
2. **Functions from Modules**: Functions defined in Python modules (e.g., `math.sqrt()`).
3. **User-defined Functions**: Functions created by the user to perform specific tasks.

---

## **2. Defining a Function**

To define a function in Python, use the `def` keyword followed by the function name and parentheses `()`. The function body is indented and can include a **docstring** (optional) to describe the function.

### **Syntax**
```python
def function_name(parameters):
    """Docstring (optional)"""
    # Function body
    return [expression]
```

### **Example**
```python
def greet():
    """This function greets the user."""
    print("Hello, World!")
```

---

## **3. Calling a Function**

Once a function is defined, you can call it using its name followed by parentheses. If the function requires arguments, pass them inside the parentheses.

### **Example**
```python
greet()  # Output: Hello, World!
```

---

## **4. Function Arguments**

Functions can accept arguments to make them more flexible. Python supports several types of arguments:

### **4.1 Positional Arguments**
Arguments passed in the order they are defined.

```python
def add(x, y):
    return x + y

result = add(10, 20)  # Output: 30
```

### **4.2 Keyword Arguments**
Arguments passed with a keyword. The order doesn’t matter.

```python
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

print_info(age=25, name="Alice")  # Output: Name: Alice, Age: 25
```

### **4.3 Default Arguments**
Arguments with default values. If no value is provided, the default is used.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, Guest!
greet("Bob")  # Output: Hello, Bob!
```

### **4.4 Variable-length Arguments**
Functions can accept a variable number of arguments using `*args` (non-keyword) and `**kwargs` (keyword).

```python
def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3)  # Output: 1 2 3

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)  # Output: name: Alice, age: 25
```

---

## **5. Return Values**

Functions can return values using the `return` statement. If no `return` statement is provided, the function returns `None`.

### **Example**
```python
def square(x):
    return x * x

result = square(5)  # Output: 25
```

---

## **6. Lambda Functions**

Lambda functions are small, anonymous functions defined using the `lambda` keyword. They can take any number of arguments but return only one expression.

### **Syntax**
```python
lambda arguments: expression
```

### **Example**
```python
add = lambda x, y: x + y
print(add(10, 20))  # Output: 30
```

---

## **7. Scope of Variables**

Variables in Python have two scopes:
- **Local Scope**: Variables defined inside a function.
- **Global Scope**: Variables defined outside a function.

### **Example**
```python
x = 10  # Global variable

def my_function():
    y = 20  # Local variable
    print(x + y)

my_function()  # Output: 30
print(y)  # Error: y is not defined
```

---

## **8. Practice Problems**

1. **Write a function** to calculate the factorial of a number.
2. **Create a function** that takes a list of numbers and returns the maximum value.
3. **Write a lambda function** to multiply two numbers.
4. **Create a function** that accepts a variable number of arguments and returns their sum.
5. **Write a function** to check if a string is a palindrome.

---

## **9. Real-world Use Cases**

1. **Data Processing**: Functions can be used to clean and process large datasets.
2. **Web Development**: Functions are used to handle HTTP requests and responses in frameworks like Flask and Django.
3. **Automation**: Functions can automate repetitive tasks like file handling or sending emails.
4. **Machine Learning**: Functions are used to define models, preprocess data, and evaluate performance.

---

## **Additional Resources**

- [Python Documentation on Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python: Functions](https://realpython.com/defining-your-own-python-function/)
- [W3Schools: Python Functions](https://www.w3schools.com/python/python_functions.asp)

---

## **Conclusion**

Functions are a fundamental concept in Python programming. By mastering functions, you can write modular, reusable, and efficient code. Practice the examples and problems provided in this README to strengthen your understanding of Python functions.

Happy coding! 🚀





