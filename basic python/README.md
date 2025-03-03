
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

Functions are a fundamental concept in Python programming. By mastering functions, you can write modular, reusable, and efficient code. 





# **Encoding and Decoding Text in Python**

How we **encode** and **decode** text using different character encodings ? The script reads a file containing a list of human languages, encodes each line into bytes, and then decodes it back into a string. It also explains key concepts like `encode()`, `decode()`, `sys.argv`, and `strip()`.

To do this exercise you’ll need to download a text file that I’ve written named languages.txt. 


### Download the file : <a href = "https://learnpythonthehardway.org/python3/languages.txt">languages.txt </a>


This file was created with a list of human languages to demonstrate a few interesting concepts:
- How modern computers store human languages for display and processing and how Python3 calls these strings
- How you must “encode” and “decode” Python’s strings into a type called bytes
- How to handle errors in your string and byte handling
- How to read code and find out what it means even if you’ve never seen it before

---

## **Table of Contents**

1. [Key Concepts](#key-concepts)
   - [Encoding and Decoding](#encoding-and-decoding)
   - [Command-Line Arguments (`sys.argv`)](#command-line-arguments-sysargv)
   - [The `strip()` Function](#the-strip-function)
2. [Script Explanation](#script-explanation)
   - [Importing `sys`](#1-importing-sys)
   - [Unpacking Command-Line Arguments](#2-unpacking-command-line-arguments)
   - [The `main` Function](#3-the-main-function)
   - [The `print_line` Function](#4-the-print_line-function)
   - [Opening the File](#5-opening-the-file)
   - [Calling the `main` Function](#6-calling-the-main-function)
3. [Example Input and Output](#example-input-and-output)
4. [Real-world Use Cases](#real-world-use-cases)
5. [Practice Problems](#practice-problems)

---

## **1. Key Concepts**

### **Encoding and Decoding**

- **Encoding**:
  - Converts a string (human-readable text) into a sequence of bytes (binary data).
  - Example: `"Hello".encode("utf-8")` produces `b'Hello'`.
  - Common encodings: `utf-8`, `ascii`, `latin-1`.

- **Decoding**:
  - Converts bytes back into a string.
  - Example: `b'Hello'.decode("utf-8")` produces `"Hello"`.
  ### Working of the Python Decode() Method 
- The following flowchart shows the working of Python decoding:
<img src="https://github.com/user-attachments/assets/9e328e8a-ae87-4914-becd-8becdeb5afdc" height = "400" width="400" />


- **Why Encoding/Decoding is Important**:
  - Computers store and transmit data as bytes.
  - Different systems use different encodings, so proper encoding/decoding ensures text is displayed correctly.

---

### **Command-Line Arguments (`sys.argv`)**

- `sys.argv` is a list in Python that contains the command-line arguments passed to the script.
- The first element (`sys.argv[0]`) is the script name.
- Subsequent elements are the arguments provided by the user.
- Example:
  ```bash
  python script.py utf-8 strict
  ```
  - `sys.argv[0]`: `script.py`
  - `sys.argv[1]`: `utf-8`
  - `sys.argv[2]`: `strict`

---

### **The `strip()` Function**

- Removes leading and trailing whitespace (spaces, tabs, newlines) from a string.
- Example:
  ```python
  text = "  Hello, World!  \n"
  stripped_text = text.strip()  # "Hello, World!"
  ```

---

## **2. Script Explanation**

### **1. Importing `sys`**
```python
import sys
```
- Imports the `sys` module to access command-line arguments.

---

### **2. Unpacking Command-Line Arguments**
```python
script, input_encoding, error = sys.argv
```
- Unpacks the command-line arguments into three variables:
  - `script`: The name of the script.
  - `input_encoding`: The encoding scheme (e.g., `utf-8`).
  - `error`: The error handling scheme (e.g., `strict`, `ignore`, `replace`).

---

### **3. The `main` Function**
```python
def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
```
- **Purpose**: Reads the file line by line and processes each line.
- **Parameters**:
  - `language_file`: The file object containing the list of languages.
  - `encoding`: The encoding scheme to use.
  - `errors`: The error handling scheme.
- **Workflow**:
  1. Reads a line from the file using `readline()`.
  2. If the line is not empty, calls `print_line()` to process it.
  3. Recursively calls itself to process the next line.

---

### **4. The `print_line` Function**
```python
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)
```
- **Purpose**: Processes a single line from the file.
- **Parameters**:
  - `line`: The line of text to process.
  - `encoding`: The encoding scheme to use.
  - `errors`: The error handling scheme.
- **Workflow**:
  1. Removes whitespace from the line using `strip()`.
  2. Encodes the string into bytes using `encode()`.
  3. Decodes the bytes back into a string using `decode()`.
  4. Prints the raw bytes and the decoded string for comparison.

---

### **5. Opening the File**
```python
languages = open("languages.txt", encoding="utf-8")
```
- Opens the file `languages.txt` in read mode with `utf-8` encoding.
- The file contains a list of human languages, one per line.

---

### **6. Calling the `main` Function**
```python
main(languages, input_encoding, error)
```
- Calls the `main` function with the file object, encoding, and error handling scheme as arguments.
- Starts the process of reading and processing the file.

---

## **3. Example Input and Output**

### **Input File (`languages.txt`)**
```
English
Français
Español
日本語
```

### **Command to Run the Script**
```bash
python script.py utf-8 strict
```

### **Output**
```
b'English' <===> English
b'Fran\xc3\xa7ais' <===> Français
b'Espa\xc3\xb1ol' <===> Español
b'\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e' <===> 日本語
```

---

## **4. Real-world Use Cases**

1. **Text Processing**:
   - Encoding and decoding are essential when working with text files, databases, or APIs that use different character encodings.

2. **Data Transmission**:
   - Bytes are used for transmitting data over networks (e.g., HTTP requests, emails).

3. **Localization**:
   - Handling multiple languages and character sets in applications.

---

## **5. Practice Problems**

1. Modify the script to handle a different encoding (e.g., `ascii`) and observe the output.
2. Change the error handling scheme to `ignore` or `replace` and see how it affects the output.
3. Add a counter to display the line number along with the encoded and decoded text.
4. Write a script that writes encoded bytes to a file and then reads and decodes them.

---

## **Conclusion**

This script demonstrates how Python handles text encoding and decoding, which is crucial for working with multilingual data. By understanding these concepts, you can build applications that process and display text correctly across different systems and languages.

For further reading, refer to the [Python Documentation on Encodings](https://docs.python.org/3/library/codecs.html).


# Python Lists

## Introduction
A **list** in Python is a built-in data structure that stores an ordered collection of items. It is similar to an array in C, C++, or Java but with a major advantage—lists can hold elements of different data types.

Python’s simplest sequence data structure is the list, which is an ordered list of things. You can access
the elements of a list randomly, in order, extend it, shrink it, and do most anything else you could do
to a sequence of things in real life.


A Python list is mutable. Any item from the list can be accessed using its index, and can be modified. One or more objects from the list can be removed or added. A list may have same item at more than one index positions.



Lists are defined using **square brackets `[ ]`**, and items are separated by commas.

### **Examples of Lists**:
```python
list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = [25.50, True, -55, 1+2j]
```

## **Features of Lists**:
- Ordered collection of elements.
- Mutable (modifiable).
- Can contain mixed data types.
- Supports indexing and slicing.

---

## **Accessing Values in Lists**
You can access list elements using their index (starting from `0`).

### **Example:**
```python
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]:", list1[0])  # Accessing first element
print("list2[1:5]:", list2[1:5])  # Accessing elements from index 1 to 4
```

### **Output:**
```
list1[0]: physics
list2[1:5]: [2, 3, 4, 5]
```

---

## **Updating Lists**
Lists are mutable, meaning elements can be updated or modified.

### **Example:**
```python
list1 = ['physics', 'chemistry', 1997, 2000]
print("Value at index 2:", list1[2])

list1[2] = 2001  # Updating an element
print("Updated value at index 2:", list1[2])
```

### **Output:**
```
Value at index 2: 1997
Updated value at index 2: 2001
```

---

## **Deleting List Elements**
You can remove elements using the `del` statement or the `remove()` method.

### **Example:**
```python
list1 = ['physics', 'chemistry', 1997, 2000]
print("Before deletion:", list1)

del list1[2]  # Removing element at index 2
print("After deletion:", list1)
```

### **Output:**
```
Before deletion: ['physics', 'chemistry', 1997, 2000]
After deletion: ['physics', 'chemistry', 2000]
```

---

## **Python List Operations**
| Expression | Result | Description |
|------------|---------|-------------|
| `[1, 2, 3] + [4, 5, 6]` | `[1, 2, 3, 4, 5, 6]` | List concatenation |
| `['Hi!'] * 4` | `['Hi!', 'Hi!', 'Hi!', 'Hi!']` | List repetition |
| `3 in [1, 2, 3]` | `True` | Membership test |

---

## **Indexing, Slicing, and Matrices**
Lists support indexing and slicing like strings.

### **Example:**
```python
L = ['spam', 'Spam', 'SPAM!']
print(L[2])   # Accessing third element
print(L[-2])  # Accessing second last element
print(L[1:])  # Slicing from index 1 to end
```

### **Output:**
```
SPAM!
Spam
['Spam', 'SPAM!']
```

---

## **Python List Methods**
Python provides many built-in methods to manipulate lists.

| Method | Description |
|--------|-------------|
| `list.append(obj)` | Appends `obj` to the list. |
| `list.clear()` | Removes all elements from the list. |
| `list.copy()` | Returns a shallow copy of the list. |
| `list.count(obj)` | Counts occurrences of `obj` in the list. |
| `list.extend(seq)` | Extends list by appending elements from `seq`. |
| `list.index(obj)` | Returns the first index of `obj`. |
| `list.insert(index, obj)` | Inserts `obj` at the specified `index`. |
| `list.pop([index])` | Removes and returns item at `index`. Default is last item. |
| `list.remove(obj)` | Removes the first occurrence of `obj`. |
| `list.reverse()` | Reverses the list in place. |
| `list.sort()` | Sorts the list. |

### **Examples of List Methods:**
```python
numbers = [10, 20, 30, 40]
numbers.append(50)  # Adds 50 to the list
numbers.remove(20)  # Removes the first occurrence of 20
numbers.insert(1, 15)  # Inserts 15 at index 1
numbers.reverse()  # Reverses the list
print(numbers)
```

### **Output:**
```
[50, 40, 30, 15, 10]
```

---

## **Built-in Functions with Lists**
Python also provides built-in functions that can be used with lists.

| Function | Description |
|----------|-------------|
| `len(list)` | Returns the length of the list. |
| `max(list)` | Returns the maximum element. |
| `min(list)` | Returns the minimum element. |
| `list(seq)` | Converts a sequence to a list. |

### **Example:**
```python
num_list = [5, 10, 15, 20]
print("Length:", len(num_list))
print("Max value:", max(num_list))
print("Min value:", min(num_list))
```

### **Output:**
```
Length: 4
Max value: 20
Min value: 5
```

---

## **Conclusion**
- Lists are versatile and widely used in Python.
- They can store mixed data types.
- Lists are mutable and support many operations and methods.
- Understanding lists is essential for efficient Python programming.

---

Feel free to experiment with these examples to gain a deeper understanding! 🚀




# Python Dictionaries

## Introduction
A **dictionary** in Python is a built-in data structure that stores data in **key-value** pairs. It is an **unordered**, **mutable**, and **indexed** collection where each key is unique and maps to a specific value.

Dictionaries are commonly used when data needs to be stored in a structured format, allowing for quick lookups.

### **Example of Python Dictionaries:**
```python
capitals = {"Maharashtra": "Mumbai", "Gujarat": "Gandhinagar", "Telangana": "Hyderabad"}
numbers = {10: "Ten", 20: "Twenty", 30: "Thirty"}
marks = {"Savita": 67, "Imtiaz": 88, "Laxman": 91}
```

---

## **Key Features of Dictionaries**
- **Unordered** – Items have no specific order (in Python 3.7+, they maintain insertion order).
- **Mutable** – Can be modified after creation.
- **Indexed** – Access elements using keys instead of numerical indexes.
- **Unique Keys** – Keys must be unique; assigning a new value to an existing key replaces the old value.
- **Heterogeneous** – Keys and values can be of any data type.

---

## **Creating a Dictionary**
You can create a dictionary using **curly braces `{}`** or the `dict()` function.

### **Example:**
```python
# Using curly braces
sports_player = {"Name": "Sachin Tendulkar", "Age": 48, "Sport": "Cricket"}
print("Dictionary using curly braces:", sports_player)

# Using dict() function
student_info = dict(name="Alice", age=21, major="Computer Science")
print("Dictionary using dict():", student_info)
```

### **Output:**
```
Dictionary using curly braces: {'Name': 'Sachin Tendulkar', 'Age': 48, 'Sport': 'Cricket'}
Dictionary using dict(): {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}
```

---

## **Accessing Dictionary Items**
Use **square brackets `[ ]`** or the **`get()` method** to access values.

### **Example:**
```python
student_info = {"name": "Alice", "age": 21, "major": "Computer Science"}

# Accessing values using square brackets
name = student_info["name"]
print("Name:", name)

# Accessing values using get() method
age = student_info.get("age")
print("Age:", age)
```

### **Output:**
```
Name: Alice
Age: 21
```

---

## **Modifying Dictionary Items**
You can **update** values or **add** new key-value pairs.

### **Example:**
```python
student_info["age"] = 22  # Modifying an existing key-value pair
student_info["graduation_year"] = 2023  # Adding a new key-value pair
print("Modified dictionary:", student_info)
```

### **Output:**
```
Modified dictionary: {'name': 'Alice', 'age': 22, 'major': 'Computer Science', 'graduation_year': 2023}
```

---

## **Removing Dictionary Items**
Use the `del` statement, `pop()`, or `popitem()` to remove elements.

### **Example:**
```python
# Using del statement
del student_info["major"]

# Using pop()
graduation_year = student_info.pop("graduation_year")
print(student_info)
```

### **Output:**
```
{'name': 'Alice', 'age': 22}
```

---

## **Iterating Through a Dictionary**
You can loop through keys, values, or key-value pairs using loops.

### **Example:**
```python
student_info = {"name": "Alice", "age": 22, "major": "Computer Science"}

# Iterating through keys
for key in student_info:
    print("Key:", key, "Value:", student_info[key])

# Iterating through values
for value in student_info.values():
    print("Value:", value)

# Iterating through key-value pairs
for key, value in student_info.items():
    print("Key:Value:", key, value)
```

---

## **Dictionary Methods with Examples**
| Method | Description | Example |
|--------|-------------|---------|
| `dict.clear()` | Removes all elements | `student_info.clear()` |
| `dict.copy()` | Returns a shallow copy | `copy_dict = student_info.copy()` |
| `dict.fromkeys(seq, value)` | Creates dictionary with keys from `seq` | `new_dict = dict.fromkeys(["a", "b", "c"], 0)` |
| `dict.get(key, default)` | Returns value for key or default | `age = student_info.get("age", 0)` |
| `dict.items()` | Returns a view of key-value pairs | `print(student_info.items())` |
| `dict.keys()` | Returns a view of keys | `print(student_info.keys())` |
| `dict.pop(key)` | Removes and returns the value of key | `student_info.pop("age")` |
| `dict.update(dict2)` | Updates the dictionary with another dictionary | `student_info.update({"GPA": 3.8})` |
| `dict.values()` | Returns a view of values | `print(student_info.values())` |

### **Example Usage:**
```python
# Using some dictionary methods
student_info = {"name": "Alice", "age": 22, "major": "Computer Science"}
print(student_info.keys())  # Output: dict_keys(['name', 'age', 'major'])
print(student_info.values())  # Output: dict_values(['Alice', 22, 'Computer Science'])

# Using update method
student_info.update({"GPA": 3.8})
print(student_info)
```

### **Output:**
```
dict_keys(['name', 'age', 'major'])
dict_values(['Alice', 22, 'Computer Science'])
{'name': 'Alice', 'age': 22, 'major': 'Computer Science', 'GPA': 3.8}
```

---

## **Built-in Functions with Dictionaries**
| Function | Description | Example |
|----------|-------------|---------|
| `len(dict)` | Returns the number of items | `print(len(student_info))` |
| `str(dict)` | Returns a string representation | `print(str(student_info))` |
| `type(variable)` | Returns the type of variable | `print(type(student_info))` |

---

## **Conclusion**
- Dictionaries store key-value pairs for fast lookups.
- They are mutable, unordered, and flexible.
- Python provides many useful methods for working with dictionaries.
- Understanding dictionaries is essential for Python programming.

---

Start experimenting with dictionaries and explore their powerful capabilities! 🚀





#  Dictionaries and Modules

## Introduction
In this exercise, we will explore Python’s **`__dict__` attribute**, which is a special dictionary used to store all attributes of objects, including **modules, classes, and instances**. Understanding `__dict__` helps in:

  1. **Inspecting and manipulating objects dynamically.**
  2. **Understanding how Python stores attributes internally.**
  3. **Exploring module-level variables and metadata.**

---

## **Step 1: Reviewing `import` and Modules**
A module in Python is simply a file containing Python definitions and statements. When you import a module, Python loads its contents into memory and allows access to its attributes.

### **Example:** `ex26.py`
```python
name = "Zed"
height = 74
```

Now create another file and import `ex26.py`:

### **Example:** `ex26_code.py`
```python
import ex26

print("Name:", ex26.name)
print("Height:", ex26.height)
```

### **Output:**
```
Name: Zed
Height: 74
```

This demonstrates how importing a module makes its attributes accessible.

---

## **Step 2: Understanding `__dict__`**
Every Python module, class, or object has an internal dictionary (`__dict__`) that stores its attributes.

### **Example:**
```python
from pprint import pprint
pprint(ex26.__dict__)
```

### **Sample Output:**
```
{'__builtins__': <module 'builtins' ...>,
 '__cached__': None,
 '__doc__': None,
 '__file__': 'ex26.py',
 '__loader__': ...,
 '__name__': 'ex26',
 '__package__': None,
 '__spec__': None,
 'height': 74,
 'name': 'Zed'}
```

The `__dict__` attribute contains all module variables and built-in metadata.

---

## **Step 3: Accessing Variables Using `__dict__`**
Since modules use `__dict__` internally, we can retrieve variables using dictionary syntax.

### **Example:**
```python
print("Height:", ex26.height)
print("Height via __dict__:", ex26.__dict__['height'])
```

### **Output:**
```
Height: 74
Height via __dict__: 74
```

Both methods return the same result.

---

## **Step 4: Modifying `__dict__`**
Since `__dict__` acts as a dictionary, modifying it updates the module’s attributes dynamically.

### **Example:**
```python
print(f"Initially: {ex26.height} inches tall.")

ex26.__dict__['height'] = 1000
print(f"Updated: {ex26.height} inches tall.")

ex26.height = 12
print(f"Modified again: {ex26.__dict__['height']} inches tall.")
```

### **Output:**
```
Initially: 74 inches tall.
Updated: 1000 inches tall.
Modified again: 12 inches tall.
```

This proves that updating `__dict__` directly affects module variables.

---

## **Step 5: Exploring `__dict__` in Other Objects**
The `__dict__` attribute is **not just for modules**—it also exists for classes and instances.

### **Example (Using Classes):**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
print(person1.__dict__)  # Inspecting the instance dictionary
```

### **Output:**
```
{'name': 'Alice', 'age': 25}
```

This shows that instance variables are stored in `__dict__`.

---

## **Step 6: Exploring Other Dunder Variables**
Python provides many other special (dunder) variables. You can explore them using `help()` and `__doc__`.

### **Example:**
```python
from pprint import pprint

print(pprint.__doc__)  # Prints the documentation for pprint
help(pprint)  # Displays detailed help information
```

### **Output:**
```
pprint(object, *args, sort_dicts=True, **kwargs)
    Pretty-print a Python object to a stream [...]
```

Try accessing `__doc__`, `__name__`, `__file__`, and `__package__` in different objects.

---

## **Why Use `__dict__`?**
- **Introspection:** Helps debug and inspect objects dynamically.
- **Dynamic Attribute Assignment:** Modify objects on the fly.
- **Serialization:** Convert objects into JSON-friendly dictionaries.
- **Meta-programming:** Used in frameworks and advanced Python techniques.

### **Example (Dynamic Attributes):**
```python
class Car:
    pass

car1 = Car()
car1.__dict__["color"] = "red"
print(car1.color)  # Accessing dynamically assigned attribute
```

### **Output:**
```
red
```

---

## **Summary**
- `__dict__` is a built-in dictionary storing object attributes.
- Modules, classes, and instances use `__dict__` for storing variables dynamically.
- You can manipulate `__dict__` to modify objects at runtime.
- Other dunder variables (`__doc__`, `__name__`, `__file__`) provide metadata about objects.

---

### **Next Steps**
- Experiment with modifying `__dict__` in different modules and classes.
- Explore additional dunder variables using `dir()`.
- Try building a dynamic object system using `__dict__`.

Happy Coding! 🚀

# The Five Simple Rules to the Game of Code

## Introduction
Programming, like games such as Chess or Go, follows a set of simple rules that enable complex interactions. These rules are fundamental to understanding how code works at a deeper level. While you may not use these rules directly in daily coding, knowing them will help you debug, optimize, and truly understand the inner workings of your programs.

---

## **Rule 1: Everything Is a Sequence of Instructions**
All programs consist of a sequence of instructions that tell the computer what to do. Python executes statements in order, converting them into low-level bytecode instructions.

### **Example:**
```python
x = 10
y = 20
z = x + y
```

Internally, Python translates this into bytecode:
```plaintext
LOAD_CONST 0 (10)  # Load 10
STORE_NAME 0 (x)   # Store in x
LOAD_CONST 1 (20)  # Load 20
STORE_NAME 1 (y)   # Store in y
LOAD_NAME 0 (x)    # Load x (10)
LOAD_NAME 1 (y)    # Load y (20)
BINARY_ADD         # Add x and y
STORE_NAME 2 (z)   # Store result in z
```
Each Python instruction is broken down into basic operations that the computer executes sequentially.

---

## **How to View Bytecode**
You can view the bytecode of any Python script using the `dis` module.

### **Example:**
```python
from dis import dis

dis('''
x = 10
y = 20
z = x + y
''')
```
This will output a bytecode representation of the given Python code.

---

## **Rule 2: Jumps Make the Sequence Non-Linear**
In addition to executing instructions sequentially, programs can **jump** to different parts of the code, making execution non-linear. The `while` loop is an example of this:

### **Example:**
```python
while True:
    x = 10
```
Disassembling this code reveals a jump instruction:
```plaintext
LOAD_CONST 1 (10)
STORE_NAME 0 (x)
JUMP_ABSOLUTE 0  # Jump back to instruction at index 0
```
The `JUMP_ABSOLUTE` instruction tells Python to return to the beginning of the loop, creating an infinite cycle.

---

## **Rule 3: Conditions Control the Jumps**
Programs make decisions using conditions (`if` statements, `while` loops). These conditions are translated into **jump instructions** that determine execution flow.

### **Example:**
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

Disassembling this:
```plaintext
LOAD_NAME 0 (x)
LOAD_CONST 1 (5)
COMPARE_OP 4 (> 5)
POP_JUMP_IF_FALSE 10  # Skip print if condition is False
LOAD_GLOBAL 0 (print)
CALL_FUNCTION 1
```
The instruction `POP_JUMP_IF_FALSE` ensures the `print` function only executes if `x > 5`.

---

## **Rule 4: Functions Allow Code Reuse**
Functions encapsulate code and create **reusable** sequences of instructions.

### **Example:**
```python
def add(a, b):
    return a + b

result = add(5, 10)
```

Bytecode reveals function calls involve `CALL_FUNCTION` and `RETURN_VALUE` instructions:
```plaintext
LOAD_NAME 0 (add)
LOAD_CONST 1 (5)
LOAD_CONST 2 (10)
CALL_FUNCTION 2  # Call add with two arguments
STORE_NAME 1 (result)
```
Functions allow efficient code organization and modular programming.

---

## **Rule 5: Everything Reduces to Data Manipulation**
Ultimately, programming boils down to **loading, storing, modifying, and moving data**. Whether using variables, loops, or functions, every program is a series of operations on data.

### **Example:**
```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
```
Bytecode shows the underlying operations:
```plaintext
LOAD_NAME 0 (numbers)
LOAD_METHOD 1 (append)
LOAD_CONST 2 (4)
CALL_METHOD 1
```
Here, Python loads the list, fetches the `append` method, calls it, and modifies the list.

---

## **Where Bytecode is Stored**
Python compiles scripts into **.pyc files** inside the `__pycache__` directory. These files store precompiled bytecode, allowing faster execution.

To see compiled bytecode:
1. Create a Python script (e.g., `ex27.py`).
2. Run it using `python ex27.py`.
3. Check the `__pycache__` directory for the compiled `.pyc` file.

---

## **Summary**
- **All code is translated into a sequence of bytecode instructions.**
- **Jumps allow non-linear execution (loops, conditionals).**
- **Conditionals control jumps, making decisions in code.**
- **Functions enable code reuse and organization.**
- **All programming reduces to data manipulation.**

---

## **Next Steps**
- Experiment with `dis()` to analyze different Python structures.
- Explore the `__pycache__` directory to see compiled bytecode.
- Use `help()` and `dir()` to explore Python’s internals.

Understanding these fundamentals will help you become a better programmer! 🚀


#Understanding If, Else, and Elif Statements

## Introduction
In this exercise, we will explore **conditional statements** in Python, specifically `if`, `else`, and `elif`. These statements allow programs to make decisions and execute different blocks of code based on conditions.

Conditional statements are the foundation of control flow in Python. Understanding them is crucial for writing dynamic and responsive programs.

---

## **The If Statement**
An `if` statement evaluates a condition (a Boolean expression). If the condition is `True`, the code block under the `if` executes. If the condition is `False`, the block is skipped.

### **Example:** `ex30.py`
```python
people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5  # Increments dogs by 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
```

### **Expected Output:**
```
Too many cats! The world is doomed!
The world is dry!
People are greater than or equal to dogs.
People are less than or equal to dogs.
People are dogs.
```

### **Explanation:**
1. If `people < cats` is `True`, it prints `Too many cats! The world is doomed!`.
2. If `people > cats` is `True`, it prints `Not many cats! The world is saved!`.
3. The program continues checking each `if` statement and executing the corresponding block if the condition is `True`.

---

## **Indentation in If Statements**
Python uses indentation to define blocks of code. The standard indentation is **four spaces**.

```python
if condition:
    # This line is part of the if block
    print("Condition met!")
```

If you forget to indent, Python will raise an error:
```python
if True:
print("This will cause an IndentationError!")
```

---

## **Using `dis()` to Inspect Bytecode**
We can use the `dis` module to see how Python translates `if` statements into bytecode.

```python
from dis import dis

dis('''
if people < cats:
    print("Too many cats! The world is doomed!")
''')
```

The output shows the **jump instructions** Python uses to execute conditional statements efficiently.

---

## **The If-Else Statement**
Sometimes, we want to execute **one block of code if a condition is true** and **another block if it is false**. This is done using `else`.

### **Example:**
```python
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
```

### **Output:**
```
x is greater than 5
```

---

## **The If-Elif-Else Statement**
The `elif` (short for "else if") statement allows checking multiple conditions sequentially. The first condition that evaluates to `True` executes, and the rest are ignored.

### **Example:** `ex31.py`
```python
people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
```

### **Expected Output:**
```
We should take the cars.
Maybe we could take the trucks.
Alright, let's just take the trucks.
```

### **Explanation:**
1. The first `if` checks if `cars > people`. Since `40 > 30`, it prints "We should take the cars." The `elif` and `else` blocks are skipped.
2. The second `if` checks if `trucks > cars`. Since `15 < 40`, it moves to the `elif` and prints "Maybe we could take the trucks."
3. The third `if` checks if `people > trucks`. Since `30 > 15`, it prints "Alright, let's just take the trucks."

---

## **Study Drills & Experiments**
1. **Try changing the values of `people`, `cars`, and `trucks`** and predict what will print.
2. **Use Boolean expressions** (`and`, `or`, `not`) inside `if` statements:
   ```python
   if cars > people and trucks < cars:
       print("This condition is True!")
   ```
3. **Use dis() to inspect if-elif-else bytecode** to understand how Python handles conditionals internally.

---

## **Common Questions**
### **1. What does `+=` mean?**
`x += 1` is shorthand for `x = x + 1`. It increments `x` by 1.

### **2. What happens if I forget to indent an if statement?**
Python raises an `IndentationError`. Proper indentation is required for blocks.

### **3. Can I put multiple conditions inside an `if` statement?**
Yes! You can use `and`, `or`, and `not`:
```python
if x > 5 and x < 10:
    print("x is between 5 and 10")
```

### **4. What happens if none of the conditions in an if-elif chain are true?**
If there is an `else`, its block executes. If there is no `else`, nothing happens.

---

## **Summary**
- **`if` executes a block if a condition is true.**
- **`else` provides an alternative block when the condition is false.**
- **`elif` allows checking multiple conditions sequentially.**
- **Indentation is crucial for defining blocks.**
- **Using `dis()` helps inspect how Python executes conditionals.**

---

### **Next Steps**
- Experiment with different conditions and values.
- Try writing a simple program that takes user input and makes decisions using `if-elif-else`.
- Keep practicing! 🚀






#  Advanced Developer Tools

## Introduction

As a Python developer, managing dependencies and working in isolated environments is crucial for avoiding conflicts between different projects. This exercise covers **Conda environments**, **pip**, **.condarc configuration**, and **editor setup tips** to help you work efficiently and avoid common pitfalls.

---

## **1. Understanding Conda Environments**

Conda environments allow you to install software packages specific to a project in an isolated workspace. This prevents conflicts between different Python projects that may require different package versions.

### **Creating a New Conda Environment**
To create and activate a new environment named `lpythw`, run the following commands:
```bash
conda create --name lpythw
conda activate lpythw
```

You will see your shell prompt change to include `(lpythw)`, indicating that you are inside the environment.

### **Deactivating an Environment**
To exit the environment, run:
```bash
conda deactivate
```

### **Listing Available Environments**
To see a list of all environments on your system, use:
```bash
conda info --envs
```

### **Checking Installed Packages**
To see what packages are installed in an environment, run:
```bash
conda list
```

---

## **2. Using Conda-Forge for More Packages**

Sometimes, the default Conda repository does not have the package you need. The `conda-forge` repository provides additional community-maintained packages.

### **Adding Conda-Forge**
```bash
# Verify Conda version >= 4.9
conda --version

# Ensure you are in the base environment
conda deactivate

# Install a faster dependency solver
conda install -n base conda-libmamba-solver
conda config --set solver libmamba

# Update Conda (this may take a while)
conda update -n base conda

# Add the conda-forge channel
conda config --append channels conda-forge
conda config --set channel_priority strict
```

After these steps, Conda will have access to many more packages while prioritizing stability.

---

## **3. Using pip for Package Management**

While Conda is powerful, some Python libraries are only available via `pip`, the standard Python package manager.

### **Installing pip in a Conda Environment**
```bash
conda install pip
```

### **Using pip Safely Inside a Conda Environment**
Using pip alongside Conda can cause conflicts. The best practice is to install packages in this order:
```bash
# 1. Create a new environment
conda create --name new-condapip

# 2. Activate the environment
conda activate new-condapip

# 3. Install Conda packages first
conda install numpy pandas

# 4. Then use pip for unavailable packages
pip install some-package
```

### **Creating a pip-only Environment**
If you don’t need Conda, create a pip-only environment:
```bash
conda create --name pip-only-env
conda activate pip-only-env
pip install requests
```

---

## **4. Managing Conda Configuration with .condarc**

Conda settings are stored in a file called `.condarc`, usually found in your home directory.

### **Example `.condarc` File:**
```yaml
channels:
  - conda-forge
  - defaults
channel_priority: strict
```

To modify `.condarc`, use:
```bash
conda config --append channels conda-forge
conda config --set channel_priority strict
```

---

## **5. Best Practices for Editing and Development**

### **Avoid Using Tab Characters**
- Use spaces instead of tabs to prevent indentation errors.
- Most editors allow you to configure spaces instead of tabs.

### **Show White Spaces in Your Editor**
- In **VS Code**, enable `Render Whitespace` in settings.
- In **Geany**, go to `View -> Show White Space`.

### **Save Frequently**
Use `Ctrl+S` often to save your work.

### **Experiment with Different Editors**
- **VS Code**: Popular with extensive plugin support.
- **PyCharm**: Powerful IDE for professional Python development.
- **Geany**: Lightweight but feature-rich.

### **Use the Right IDE for the Right Task**
- **Android Development** → Use **Android Studio**.
- **iOS Development** → Use **Xcode**.
- **General Python Development** → Use **VS Code or PyCharm**.

---

## **6. Going Further**

- **Customize your editor** to fit your workflow (fonts, colors, keybindings).
- **Experiment with Conda and pip environments** to see how they work.
- **Read official Conda documentation** to explore more advanced options.

By following these best practices, you’ll avoid many common pitfalls and work more efficiently as a Python developer. 🚀



#  A Project Skeleton

## Introduction
In this exercise, we will learn how to create a **Python project skeleton**, package it using **Conda**, and install it locally for use in other projects. This is useful when developing reusable modules or applications.

This guide will cover:
- **Why we use project skeletons**
- **Understanding each command**
- **Using `cookiecutter` to generate a structured project**
- **Building and installing a Conda package**

---

## **1. Why Use a Project Skeleton?**
A **project skeleton** provides a standardized structure for organizing code, making it easier to:
- Maintain consistency across projects.
- Reuse code efficiently in different environments.
- Share your project with others.
- Install and use your project across multiple projects.

---

## **2. Setting Up a Conda Environment**
Before creating a project, we need to **activate an isolated Conda environment** to keep dependencies separate.

### **Command:**
```bash
conda activate lpythw
```
- This ensures that our package is installed in a controlled environment, avoiding conflicts.
- If `lpythw` doesn’t exist, create it using:
```bash
conda create --name lpythw
conda activate lpythw
```

---

## **3. Using `cookiecutter` to Generate a Project**
`cookiecutter` is a tool that **automatically generates project files and directories** based on templates.

### **Install `cookiecutter`**
```bash
conda install cookiecutter
```
- Installs `cookiecutter`, which helps create structured projects quickly.

### **Generate a Project Skeleton**
```bash
cookiecutter https://github.com/conda/cookiecutter-conda-python.git
```
This command:
- Downloads the **Conda Python project template**.
- Asks for user details (name, email, GitHub username, etc.).
- Creates a structured project with the necessary files.

### **Example Input:**
```
full_name [Full Name]: John Doe
email [Email Address]: johndoe@example.com
github_username [Destination github org or username]: johndoe
repo_name [repository-name]: my_project
package_name [my_project]: my_project
project_short_description [Short description]: A sample Conda project.
noarch_python [y]: y
include_cli [y]: y
Choose a license [1-6]: 1
```
- The project is now created inside the `my_project` directory.

---

## **4. Exploring the Project Structure**
Once created, navigate into the project directory:
```bash
cd my_project
ls  # List the project files
```
### **Key Files and Directories:**
- **`my_project/`** – The main project directory.
- **`conda.recipe/`** – Contains instructions for building the package.
- **`my_project/testing.py`** – A sample Python module.
- **`LICENSE`** – Defines the project’s licensing.
- **`README.md`** – Project documentation.

---

## **5. Writing a Simple Python Function**
Inside `my_project/testing.py`, add the following code:
```python
def hello():
    print("Hello!")
```
This function will be used to test our package installation.

---

## **6. Building the Project with Conda**
Now, we will **convert our project into a Conda package** so it can be installed.

### **Command:**
```bash
conda build conda.recipe
```
#### **Explanation:**
- `conda build` compiles the project into an **installable package**.
- `conda.recipe/` contains **metadata** (`meta.yaml`) that describes the package.
- The build output is stored inside Conda’s build directory.

### **Sample Output:**
```
TEST END: /Users/USER/anaconda3/conda-bld/noarch/my_project-0+unknown-py_0.tar.bz2
```
This file is our **installable package**.

---

## **7. Installing the Project Locally**
Once the package is built, install it in our environment.

### **Command:**
```bash
conda install /Users/USER/anaconda3/conda-bld/noarch/my_project-0+unknown-py_0.tar.bz2
```
#### **Explanation:**
- Installs the package in the **`lpythw`** environment.
- Adds `my_project` to the Conda package list.

### **Verify Installation:**
```bash
conda list my_project
```
Sample output:
```
# Name Version Build Channel
my_project 0+unknown py_0 local
```
---

## **8. Testing the Installed Package**
To confirm that `my_project` works, create a new Python file **outside** the project folder.

### **Example (`test_install.py`):**
```python
from my_project import testing

testing.hello()
```
### **Run the Script:**
```bash
python test_install.py
```
### **Expected Output:**
```
Hello!
```
If this works, your package is successfully installed!

---

## **9. Removing the Package**
If you want to **remove the package**, use:
```bash
conda remove my_project
```
This will clean up the installation and remove the package from your environment.

---

## **10. Troubleshooting Common Errors**
### **Error 1: `metadata-generation-failed`**
**Issue:** If you named the project with a hyphen (`my-project` instead of `my_project`), it may cause an error.
**Solution:** Use underscores (`_`) instead of hyphens (`-`).

### **Error 2: `ValueError: License file missing`**
**Issue:** If you didn’t create a `LICENSE` file, the build might fail.
**Solution:** Add an empty `LICENSE` file in the project directory.

---

## **11. Study Drills**
1. **Try creating another package** with your own Python code.
2. **Install and use the package in Jupyter Lab** to test its usability.
3. **Read the documentation for `conda build`** to understand more options.
4. **Research how to publish projects to PyPI and Anaconda.**
5. **Explore other templates in `cookiecutter`** for different project structures.

---

## **Summary**
- `cookiecutter` helps create a structured Python project quickly.
- `conda build` packages the project into an installable format.
- `conda install` allows local installation and usage.
- Errors can often be fixed by carefully reviewing file names and metadata.

By following this process, you can create reusable and shareable Python projects! 🚀


#  Understanding Closures in Python

## Introduction
A **closure** is a function that is **defined inside another function** and **remembers** the variables from its parent function, even after the parent function has finished executing. Closures allow functions to have **persistent state** without using global variables.

This concept is important in Python because it enables **encapsulation**, **state retention**, and **functional programming** patterns.

---

## **1. Example of a Closure**

### **Code:**
```python
# This function creates and returns another function

def constructor(color, size):
    print(">>> constructor color:", color, "size:", size)
    
    # Nested function (closure)
    def repeater():
        print("### repeater color:", color, "size:", size)
    
    print("<<< exit constructor")
    return repeater  # Returns the nested function

# Creating functions using the constructor
blue_xl = constructor("blue", "xl")
green_sm = constructor("green", "sm")

# Calling the returned functions multiple times
for i in range(4):
    blue_xl()
    green_sm()
```

### **Expected Output:**
```
>>> constructor color: blue size: xl
<<< exit constructor
>>> constructor color: green size: sm
<<< exit constructor
### repeater color: blue size: xl
### repeater color: green size: sm
### repeater color: blue size: xl
### repeater color: green size: sm
### repeater color: blue size: xl
### repeater color: green size: sm
### repeater color: blue size: xl
### repeater color: green size: sm
```

---

## **2. Breaking Down the Code**

### **Step 1: Defining the Outer Function (`constructor`)**
```python
def constructor(color, size):
```
- This function **takes `color` and `size` as parameters** and creates an **inner function**.
- `color` and `size` exist **only inside this function**, meaning they are local variables.

### **Step 2: Defining the Inner Function (`repeater`)**
```python
def repeater():
    print("### repeater color:", color, "size:", size)
```
- `repeater` is **nested inside** `constructor`.
- It **uses** the `color` and `size` variables **from the parent function**.

### **Step 3: Returning the Inner Function**
```python
return repeater
```
- The function `repeater` is **returned** instead of being executed.
- Since `constructor` finishes execution, its local variables **should** be destroyed, but **Python keeps them alive** inside the closure.

### **Step 4: Using the Closure**
```python
blue_xl = constructor("blue", "xl")
green_sm = constructor("green", "sm")
```
- Calling `constructor("blue", "xl")` **creates a closure** where `color = "blue"` and `size = "xl"`.
- `blue_xl` now **stores** the `repeater` function with its specific data.
- Same for `green_sm`, but with `color = "green"` and `size = "sm"`.

### **Step 5: Calling the Closures in a Loop**
```python
for i in range(4):
    blue_xl()
    green_sm()
```
- Each call to `blue_xl()` prints `color: blue size: xl`.
- Each call to `green_sm()` prints `color: green size: sm`.
- The values of `color` and `size` are **remembered** even after `constructor` has finished.

---

## **3. How Closures Work Internally**

When Python detects that a function **inside another function** is using variables from its parent, it creates a **closure**. The function keeps a reference to the parent’s local variables, even after the parent function exits.

To confirm that `repeater` is a closure, use:
```python
print(blue_xl.__closure__)
print(green_sm.__closure__)
```
**Output:**
```
(<cell at 0x7f8b4c8d9d60: str object at 0x7f8b4c6a23f0>, <cell at 0x7f8b4c8d9c80: str object at 0x7f8b4c6a2450>)
(<cell at 0x7f8b4c8d9d60: str object at 0x7f8b4c6a2490>, <cell at 0x7f8b4c8d9c80: str object at 0x7f8b4c6a24f0>)
```
Each closure stores **references** to `color` and `size` inside **cell objects**, which retain values even after `constructor` has exited.

---

## **4. Why Are Closures Useful?**
Closures are useful when you need functions that:
- **Remember state** (e.g., configurations, user preferences).
- **Avoid global variables** (keep data encapsulated).
- **Can be customized at runtime**.
- **Create function factories** (return different functions based on input).

---

## **5. Real-World Use Cases of Closures**

### **Example 1: Function Factory for Multiplication**
```python
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

# Create two different closures
double = multiplier(2)
triple = multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```
- `double` remembers `factor = 2`.
- `triple` remembers `factor = 3`.

### **Example 2: Logging with Configurable Prefix**
```python
def logger(prefix):
    def log_message(message):
        print(f"{prefix}: {message}")
    return log_message

error_logger = logger("ERROR")
info_logger = logger("INFO")

error_logger("Something went wrong!")  # ERROR: Something went wrong!
info_logger("System running smoothly.")  # INFO: System running smoothly.
```
- `error_logger` remembers `prefix = "ERROR"`.
- `info_logger` remembers `prefix = "INFO"`.

---

## **6. Summary**
- **Closures are functions inside functions that remember variables from their parent.**
- **They enable stateful functions without global variables.**
- **They are used in decorators, function factories, and event handlers.**
- **Python automatically detects and maintains closure variables.**

---

### **Next Steps**
- Try modifying `constructor()` to return different functions.
- Experiment with using closures in real projects (e.g., logging, web development).
- Learn about Python **decorators**, which use closures extensively.

Closures are a powerful concept—master them, and you’ll write more flexible Python code! 🚀





# Object-Oriented Programming (OOP) in Python

## **Introduction**
Object-Oriented Programming (OOP) is a programming paradigm that uses **objects** to represent real-world entities. Python fully supports OOP, making it easy to create and manage **classes, objects, inheritance, and polymorphism**.

This chapter covers:
- **Procedural vs. Object-Oriented Programming**
- **Core principles of OOP: Classes, Objects, Encapsulation, Inheritance, and Polymorphism**
- **Method Overloading and Operator Overloading**

---

## **1. Procedural vs. Object-Oriented Programming**
### **Procedural Approach:**
- Code is organized into **functions**.
- Focuses on **procedures** (step-by-step execution).
- Uses **global variables**, which can lead to maintenance issues.
- Example:
```python
def add_numbers(a, b):
    return a + b
print(add_numbers(5, 10))  # Output: 15
```

### **Object-Oriented Approach:**
- Code is organized into **classes and objects**.
- Focuses on **data and behaviors** together.
- Reduces redundancy using **inheritance**.
- Example:
```python
class Calculator:
    def add(self, a, b):
        return a + b
calc = Calculator()
print(calc.add(5, 10))  # Output: 15
```

---

## **2. Classes and Objects in Python**
A **class** is a blueprint for creating objects. An **object** is an instance of a class with its own attributes and behaviors.

### **Example: Creating a Class and Object**
```python
class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    def description(self):  # Method
        return f"{self.brand} {self.model} supports Android."

# Creating an object of the class
phone = Smartphone("Samsung", "Galaxy S21")
print(phone.description())  # Output: Samsung Galaxy S21 supports Android.
```

### **Breakdown:**
- `__init__`: A special method (constructor) that initializes attributes.
- `self`: Refers to the current object instance.
- `brand` and `model`: Instance variables that store object data.
- `description()`: A method that defines object behavior.

---


.

---

## **What is `self` in Python Classes?**
- `self` is a **reference to the current instance of the class**.
- It is used to **access instance variables and methods** inside the class.
- When an object is created, `self` allows that object to store and manipulate its own data.

---

## **How `self` Works Internally?**
Think of a class as a **blueprint**, and `self` as a way to keep track of each **individual object** created from that blueprint.

### **Example 1: Understanding `self` in Action**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Assigning instance variable using self
        self.model = model

    def show_details(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

# Creating two objects
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Calling the method
car1.show_details()  # Output: Car Brand: Toyota, Model: Camry
car2.show_details()  # Output: Car Brand: Honda, Model: Civic
```

### **How Does `self` Work Here?**
1. When `car1` is created, `self.brand = "Toyota"` and `self.model = "Camry"`.
2. When `car2` is created, `self.brand = "Honda"` and `self.model = "Civic"`.
3. When `car1.show_details()` is called:
   - `self.brand` refers to `"Toyota"`, and `self.model` refers to `"Camry"`.
4. When `car2.show_details()` is called:
   - `self.brand` refers to `"Honda"`, and `self.model` refers to `"Civic"`.

🔹 **Key takeaway:** `self` ensures that each object maintains its own unique data.

---

## **Example 2: What Happens if We Remove `self`?**
Let’s try removing `self` and see what happens:

```python
class Car:
    def __init__(brand, model):  # ❌ Wrong! Missing self
        brand.model = model  # ❌ Wrong! 'brand' is not a reference to the object

car1 = Car("Toyota", "Camry")  # ❌ Error!
```
❌ This will result in an **error**, because Python does not automatically pass the object reference without `self`.

✅ Corrected version:
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```
Now, `self` properly stores attributes in the object.

---

## **Example 3: Using `self` in Multiple Methods**
The `self` keyword is also used when calling other methods inside a class.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print(f"{self.name}'s salary is {self.salary}")

    def increase_salary(self, amount):
        self.salary += amount  # Updating instance variable
        print(f"Salary updated! New salary: {self.salary}")

# Creating an object
emp1 = Employee("Alice", 50000)

# Calling methods
emp1.display_salary()  # Output: Alice's salary is 50000
emp1.increase_salary(5000)  # Output: Salary updated! New salary: 55000
```

### **How `self` Works Here?**
1. `self.name` and `self.salary` are used to store data **inside** the object.
2. `self.salary += amount` modifies the **specific object's** salary.
3. `self.display_salary()` is called on `emp1`, so it prints **Alice’s salary**.
4. `self.increase_salary(5000)` updates Alice’s salary, but does **not** affect other objects.

---

## **Example 4: Using `self` to Differentiate Between Objects**
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def compare_marks(self, other_student):
        if self.marks > other_student.marks:
            print(f"{self.name} has higher marks than {other_student.name}.")
        elif self.marks < other_student.marks:
            print(f"{other_student.name} has higher marks than {self.name}.")
        else:
            print(f"Both {self.name} and {other_student.name} have equal marks.")

# Creating two student objects
student1 = Student("John", 85)
student2 = Student("Emma", 90)

# Comparing marks
student1.compare_marks(student2)  # Output: Emma has higher marks than John.
```

### **How `self` Works Here?**
- `self.marks` refers to the marks of **the object calling the method** (`student1`).
- `other_student.marks` refers to the marks of **the other object passed as an argument** (`student2`).

---

## **When is `self` Automatically Passed?**
### **Case 1: Inside a Class → `self` is Explicit**
```python
class Example:
    def show(self):
        print("Hello, self is required in class methods!")

obj = Example()
obj.show()  # ✅ Works, because we explicitly use self
```

### **Case 2: Outside the Class → `self` is Implicit**
```python
class Example:
    def show(self):
        print("Hello!")

obj = Example()
Example.show(obj)  # ✅ Equivalent to obj.show()
```
- `Example.show(obj)` is **manually passing** the object.
- `obj.show()` automatically passes `obj` as `self`.

---

## **Key Takeaways About `self`**
✅ `self` represents the **current object**.  
✅ It allows each object to **store its own data separately**.  
✅ It is used in **instance methods** to access attributes and other methods.  
✅ `self` **must be the first parameter** in any method (but can have a different name).  

---

## **Frequently Asked Questions**
### **Q1: Can I use a different name instead of `self`?**
Yes! Python allows any name for the first parameter, but using `self` is a convention.
```python
class Test:
    def show(myself):
        print("It works!")

obj = Test()
obj.show()  # Output: It works!
```
However, **always use `self`** to maintain readability.

---

### **Q2: Do static methods require `self`?**
No! Static methods don’t operate on the object, so they don’t use `self`.

```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

print(MathOperations.add(10, 20))  # Output: 30
```
Here, `add()` does **not** use `self` because it doesn't access instance variables.

---

## **Final Thoughts**
- `self` is a **reference to the object** inside class methods.
- It allows each instance to have **independent attributes**.
- Without `self`, methods wouldn't be able to access or modify object data.



## **3. Encapsulation**
Encapsulation restricts direct access to some object components and prevents accidental modification.

### **Example: Using Private Variables**
```python
class Desktop:
    def __init__(self):
        self.__max_price = 25000  # Private attribute
    
    def sell(self):
        return f"Selling Price: {self.__max_price}"
    
    def set_max_price(self, price):
        if price > self.__max_price:
            self.__max_price = price

# Creating an object
d = Desktop()
print(d.sell())  # Output: Selling Price: 25000

# Attempting to modify private variable directly (fails)
d.__max_price = 35000
print(d.sell())  # Output: Selling Price: 25000

# Modifying using setter method
d.set_max_price(35000)
print(d.sell())  # Output: Selling Price: 35000
```

### **Key Points:**
- `__max_price` is **private** and cannot be modified directly.
- Use **getter and setter methods** to access and modify private attributes.

---
## Why modifying `desktopObj.__max_price = 35000` doesn’t actually change the encapsulated variable and doesn’t throw an error ?   Let’s break it down step by step.

## **Understanding Encapsulation in Python**
Encapsulation is one of the fundamental principles of **Object-Oriented Programming (OOP)**. It helps restrict direct access to data members (attributes) and allows modification only through **methods** (like setters).  

### **Key Concept: Private Variables (`__max_price`)**
- In Python, we can define a **private variable** using **double underscores (`__`)** before the variable name.  
- This **does not truly make it private** but applies **name mangling**, which means:
  - The variable name is internally changed from `__max_price` to `_ClassName__max_price` (`_Desktop__max_price` in this case).
  - This prevents accidental modification but does **not** make it fully private.

---

## **Analyzing Your Code Step by Step**
```python
class Desktop:
   def __init__(self):
      self.__max_price = 25000  # Private variable (name mangling applies)

   def sell(self):
      return f"Selling Price: {self.__max_price}"  # Returns the actual value

   def set_max_price(self, price):
      if price > self.__max_price:
         self.__max_price = price  # Updates the value safely

# Creating object
desktopObj = Desktop()
print(desktopObj.sell())  # Output: Selling Price: 25000
```
✅ **At this point, `__max_price` is initialized as 25000.**

---

### **Step 1: Attempting to Modify `__max_price` Directly**
```python
desktopObj.__max_price = 35000
print(desktopObj.sell())  # Output: Selling Price: 25000
```
### **Why Doesn't the Value Change?**
- When you write `desktopObj.__max_price = 35000`, **Python does NOT modify the original `__max_price`.**
- Instead, Python **creates a new variable** in the object with the name `__max_price`, but **this is not the same as the original** one.
- The actual internal variable **is still named** `_Desktop__max_price` because of **name mangling**.

👉 **This means that `sell()` still prints the old value (25000) because it is reading `_Desktop__max_price`, not `__max_price`.**

---

### **Step 2: Modifying Using the Setter Method**
```python
desktopObj.set_max_price(35000)
print(desktopObj.sell())  # Output: Selling Price: 35000
```
✅ **Now, the value changes successfully because:**
- The method `set_max_price(35000)` modifies `self.__max_price` **inside the class scope**.
- Since `self.__max_price` (or internally `_Desktop__max_price`) is accessed correctly, the change **actually happens**.

---

## **How to Check Name Mangling?**
To confirm that the actual variable name is `_Desktop__max_price`, you can print `__dict__`:
```python
print(desktopObj.__dict__)  
```
💡 **Output:**
```python
{'_Desktop__max_price': 25000, '__max_price': 35000}
```
👉 You can see that:
- `_Desktop__max_price = 25000` (the actual private variable).
- `__max_price = 35000` (a new variable that we mistakenly created).

---

## **How to Properly Modify `__max_price`?**
There are **two correct ways** to modify `__max_price`:
1. **Using the Setter Method** (`set_max_price()`).
2. **Accessing the Mangled Name (`_Desktop__max_price`)** (Not Recommended but Possible).

### ✅ **Correct Way (Using Setter)**
```python
desktopObj.set_max_price(35000)
print(desktopObj.sell())  # Output: Selling Price: 35000
```
**Best practice** because it allows controlled modification.

### ❌ **Not Recommended but Possible (Accessing the Mangled Name)**
```python
desktopObj._Desktop__max_price = 40000
print(desktopObj.sell())  # Output: Selling Price: 40000
```
Although this works, **it breaks encapsulation** and should be avoided.

---

## **Final Summary**
| Action | Expected Outcome | Explanation |
|---------|----------------|-------------|
| `print(desktopObj.sell())` | 25000 | `__max_price` is initialized as 25000. |
| `desktopObj.__max_price = 35000` | No effect | A new variable is created instead of modifying the original one. |
| `print(desktopObj.sell())` | 25000 | `sell()` still refers to `_Desktop__max_price`, not the newly created `__max_price`. |
| `desktopObj.set_max_price(35000)` | Works correctly | The setter modifies `_Desktop__max_price` properly. |
| `print(desktopObj.sell())` | 35000 | The modification is now reflected correctly. |

---

## **Key Takeaways**
✅ **Name mangling (`_ClassName__variable`) prevents accidental modification of private variables.**  
✅ **Direct modification (`desktopObj.__max_price = 35000`) does not work because it creates a new variable instead.**  
✅ **Always use setter methods (`set_max_price()`) to modify private variables safely.**  
✅ **Accessing `_Desktop__max_price` directly works, but it breaks encapsulation and is discouraged.**



Great question! The `__init__` method in Python is called the **constructor**, and it is **automatically invoked when an object is created**.  

However, Python **does allow you to define other methods** that behave like a constructor, but they won't be **automatically called** when creating an object.

---

## **1️⃣ Can We Use a Different Name Instead of `__init__`?**
No, if you want a method to be called **automatically when an object is created**, you **must use `__init__`**.  

However, you **can define other methods** to act as **custom constructors**, but they have to be **explicitly called**.

### ❌ **Incorrect Example (Doesn't Work as an Automatic Constructor)**
```python
class Example:
    def my_constructor(self, name):
        self.name = name

# Creating an object
obj = Example("John")  # ❌ TypeError: Example() takes no arguments
```
🚨 **Error:** Python does not automatically call `my_constructor()` like `__init__()`. 

---

## **2️⃣ Using a Custom Method as a Constructor (But Calling it Manually)**
You **can define a separate method** to act as a constructor, but you have to **call it explicitly**.

### ✅ **Correct Example**
```python
class Example:
    def my_constructor(self, name):
        self.name = name

# Creating an object
obj = Example()  # No error
obj.my_constructor("John")  # Manually calling the constructor

print(obj.name)  # Output: John
```
🔹 **Key Difference:** `my_constructor()` is not called automatically. You must call it explicitly.

---

## **3️⃣ Alternative Constructors with `@classmethod`**
A better way to define **alternative constructors** is using a **class method (`@classmethod`)**.

### ✅ **Using `@classmethod` to Create an Alternative Constructor**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split('-')
        return cls(name, int(age))  # Creates an instance using the default constructor

# Using the normal constructor
p1 = Person("Alice", 30)

# Using an alternative constructor
p2 = Person.from_string("Bob-25")

print(p1.name, p1.age)  # Output: Alice 30
print(p2.name, p2.age)  # Output: Bob 25
```
✔ `from_string()` is a **custom constructor** that allows us to create a `Person` object from a string.

---

## **4️⃣ Using `__new__()` as a Constructor**
Python has another special method called `__new__()`, which is **called before `__init__()`**.  
You can override it to control object creation.

### ✅ **Using `__new__()`**
```python
class Example:
    def __new__(cls):
        print("Creating an instance...")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing the instance...")

obj = Example()
```
🛠 **Output:**
```
Creating an instance...
Initializing the instance...
```
✔ `__new__()` runs **before** `__init__()` and is mainly used for **custom object creation**.

---

## **Final Summary**
| Method | Automatically Called? | Purpose |
|--------|----------------|---------|
| `__init__()` | ✅ Yes | Default constructor (initializes object attributes). |
| Custom method (`my_constructor()`) | ❌ No | Can act like a constructor but must be called explicitly. |
| `@classmethod` alternative constructor | ✅ Yes (if used) | Creates an object in a different way. |
| `__new__()` | ✅ Yes (before `__init__()`) | Controls object creation before initialization. |

### **Conclusion**
- **`__init__` is the only automatic constructor.**  
- **Other methods** can be used as constructors but must be called **explicitly**.  
- **`@classmethod` is the best way** to create **alternative constructors**.  
- **`__new__()` is for low-level object creation** before initialization.

Let me know if you need more clarification! 🚀😊





## **4. Inheritance**
Inheritance allows a child class to reuse attributes and methods from a parent class.

### **Example: Single Inheritance**
```python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def child_greet(self):
        return "Hello from Child"

c = Child()
print(c.greet())  # Output: Hello from Parent
print(c.child_greet())  # Output: Hello from Child
```

### **Example: Multiple Inheritance**
```python
class A:
    def method_A(self):
        return "Method from A"

class B:
    def method_B(self):
        return "Method from B"

class C(A, B):  # Inheriting from A and B
    def method_C(self):
        return "Method from C"

obj = C()
print(obj.method_A())  # Output: Method from A
print(obj.method_B())  # Output: Method from B
```

---

## **5. Polymorphism**
Polymorphism allows different classes to define methods with the same name but different behavior.

### **Example: Method Overriding**
```python
class Parent:
    def show(self):
        return "Parent's method"

class Child(Parent):
    def show(self):
        return "Child's method"

c = Child()
print(c.show())  # Output: Child's method
```

### **Example: Function Polymorphism**
```python
def add(a, b, c=0):
    return a + b + c

print(add(10, 20))   # Output: 30
print(add(10, 20, 30))  # Output: 60
```

---

## **6. Operator Overloading**
Python allows us to define the behavior of operators (`+`, `-`, `*`, etc.) for custom objects.

### **Example: Overloading `+` for a Vector Class**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Calls __add__ method
print(v3)  # Output: Vector(6, 8)
```

### **Key Points:**
- `__add__` is a special method that defines behavior for `+`.
- `v1 + v2` triggers `v1.__add__(v2)`.

---

## **Summary**
- **Classes and Objects**: Objects are instances of classes with attributes and behaviors.
- **Encapsulation**: Restricts direct access to data using private variables.
- **Inheritance**: Allows a class to derive attributes and methods from another class.
- **Polymorphism**: Enables methods to have different behaviors in different classes.
- **Operator Overloading**: Customizes operator behavior for user-defined classes.

---

### **Next Steps**
- **Practice creating your own classes and objects.**
- **Experiment with encapsulation by using private variables.**
- **Try implementing different types of inheritance.**
- **Learn about `super()` to call parent class methods.**
- **Explore real-world use cases of OOP in Python.**

OOP is a powerful paradigm that makes code modular, reusable, and maintainable. Mastering these concepts will help you write efficient Python programs! 🚀



# Object-Oriented Analysis and Design (OOAD) in Python

## **Introduction**
Object-Oriented Analysis and Design (OOAD) is a systematic approach to designing and developing software using Object-Oriented Programming (OOP). This process ensures that **complex systems** can be broken down into manageable components, making code more reusable, maintainable, and scalable.

This chapter covers:
- **Understanding the OOAD process**
- **Breaking down a problem into objects and classes**
- **Creating a class hierarchy and relationships**
- **Implementing the design using Python**
- **Iterating through refinement and testing**

---

## **1. Understanding the OOAD Process**
The OOAD process follows these **five key steps**:

### **Step 1: Write or Draw About the Problem**
- Describe the problem in simple words or diagrams.
- Identify how different entities interact within the system.
- Example (Text-based adventure game):
  - **“Aliens have invaded a spaceship, and the hero must navigate through different rooms, defeat enemies, and escape.”**
  - The game involves **scenes (rooms)** and an **engine** that controls the game flow.

### **Step 2: Extract Key Concepts**
- Identify the **nouns (objects)** and **verbs (actions)** in the description.
- Example (Key nouns for the game):
  - Alien, Player, Ship, Maze, Room, Scene, Map, Engine, EscapePod.
- Example (Key verbs for the game):
  - Move, Attack, Escape, Enter, Play.

### **Step 3: Create a Class Hierarchy & Object Map**
- Group similar concepts together to form a **class hierarchy**.
- Identify **parent-child relationships** between objects.
- Example (Game class hierarchy):
  - `Scene` → Base class for different game scenes.
  - `Map` → Stores scenes and controls navigation.
  - `Engine` → Controls game execution.

### **Step 4: Code the Classes and Write Tests**
- Define **classes and methods** for each object.
- Implement **basic structure and relationships**.
- Write **unit tests** to validate the code.

### **Step 5: Repeat and Refine**
- Identify **weaknesses** in the design and **improve** them.
- Optimize the **class hierarchy and method structure**.
- Iterate over different steps when necessary.

---

## **2. Implementing the Game Structure**
Based on the analysis, the following class structure is designed:

### **Class Hierarchy for the Game**
```
* Map
    - next_scene()
    - opening_scene()
* Engine
    - play()
* Scene
    - enter()
* Death (inherits from Scene)
* Central Corridor (inherits from Scene)
* Laser Weapon Armory (inherits from Scene)
* The Bridge (inherits from Scene)
* Escape Pod (inherits from Scene)
```

### **Basic Class Implementation**
```python
class Scene:
    def enter(self):
        pass

class Engine:
    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):
    def enter(self):
        pass

class CentralCorridor(Scene):
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

class Map:
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

# Creating objects and running the game
if __name__ == "__main__":
    a_map = Map("central_corridor")
    a_game = Engine(a_map)
    a_game.play()
```

At this stage, we have **defined the basic structure**, but the methods need to be implemented.

---

## **3. Iterating and Refining the Design**
The **OOAD process is iterative**, meaning you **revisit previous steps** as needed. 
- **New insights** might emerge as we implement the game.
- **Refactoring** is an important part of making the code better.
- **Adding new features** will require modifying our class hierarchy.

For example, if we find that `Engine.play()` needs a game loop, we stop and redefine it:
```python
class Engine:
    def __init__(self, game_map):
        self.game_map = game_map

    def play(self):
        current_scene = self.game_map.opening_scene()
        while current_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.game_map.next_scene(next_scene_name)
```
This is a **top-down approach**—we start from the abstract idea and refine details as we go.

---

## **4. Top-Down vs. Bottom-Up Approaches**
OOAD typically follows a **top-down** approach, but you can also use a **bottom-up** method:

### **Top-Down Approach**
1. Define the problem.
2. Identify objects and their relationships.
3. Write high-level code first.
4. Implement the details later.
5. Iterate and refine.

### **Bottom-Up Approach**
1. Start with small code snippets.
2. Refine the code into classes and methods.
3. Identify key concepts after experimenting.
4. Write documentation after understanding the system.
5. Iterate and improve structure.

Example:
```python
# Bottom-up approach: first write small test code
class TestScene:
    def enter(self):
        print("Test Scene Entered")
        return "next_scene"

scene = TestScene()
scene.enter()
```
- Here, **we experiment first** before designing the full system.
- This works well when **we don’t know the complete structure yet**.

---

## **5. Key Takeaways from OOAD**
1. **OOAD simplifies complex problems**
   - Breaking a large problem into smaller components makes coding easier.

2. **Class Hierarchies improve structure**
   - Use **inheritance** to remove redundancy.
   - Make a **base class (`Scene`)** for shared functionality.

3. **Encapsulation ensures maintainability**
   - Store **game logic inside classes** (e.g., `Map`, `Engine`).
   - Use **methods** to keep data controlled.

4. **Iterative Refinement is key**
   - Start with a rough **skeleton** and refine it over time.
   - Write **unit tests** to validate your design.

---

## **Next Steps**
- **Enhance the game** by implementing user interactions.
- **Improve error handling** to manage invalid inputs.
- **Optimize the `Engine` class** to support dynamic game states.

By following **OOAD principles**, we can create **structured, scalable, and maintainable software**. Mastering this approach will improve your ability to design **complex systems efficiently! 🚀**





# Automated Testing in Python with PyTest

## **Introduction**
Automated testing is a crucial part of software development. It helps verify that code changes do not introduce new bugs and ensures the reliability of the software. **PyTest** is a powerful testing framework in Python that makes writing and running tests simple and efficient.

This chapter covers:
- **Why automated testing is important**
- **How to install and use PyTest**
- **Writing test cases using assertions**
- **Running tests and checking coverage**

---

## **1. Why Automated Testing?**
### **Key Benefits:**
1. **Prevents breaking old code** – Ensures new changes don’t introduce bugs in existing functionality.
2. **Saves time** – Automates repetitive testing tasks.
3. **Ensures consistency** – Eliminates human error in manual testing.
4. **Encourages better design** – Helps identify bad API design or logic flaws early.
5. **Allows safe refactoring** – With proper test coverage, you can modify old code without fear.

**Key Takeaway:** Automated testing **reduces risk and improves software quality**.

---

## **2. Installing PyTest**
To install PyTest and the coverage tool, use the following commands:

```bash
# Activate the correct environment
conda activate lpythw

# Install PyTest
conda install pytest

# Install coverage tool
conda install pytest-cov
```

The **coverage tool** helps ensure that your tests execute all parts of your code.

---

## **3. Writing a Simple Test with PyTest**
Let’s create a **Person** class that simulates a simple combat system.

### **Main Code (ex50.py)**
```python
class Person:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def hit(self, target):
        target.hp -= self.damage

    def alive(self):
        return self.hp > 0
```

### **Test Code (ex50_test.py)**
```python
from ex50 import Person

def test_combat():
    boxer = Person("Boxer", 100, 10)
    zombie = Person("Zed", 1000, 1000)

    # Assert initial health
    assert boxer.hp == 100, "Boxer should start with 100 HP."
    assert zombie.hp == 1000, "Zombie should start with 1000 HP."

    # Boxer attacks zombie
    boxer.hit(zombie)
    assert zombie.alive(), "Zombie should still be alive."

    # Zombie attacks boxer
    zombie.hit(boxer)
    assert not boxer.alive(), "Boxer should be dead."
```

### **Understanding Assertions:**
- `assert condition, "Error message if false"`
- If the condition is **False**, the test fails and prints the error message.

---

## **4. Running Tests with PyTest**
To run the tests, use:
```bash
pytest ex50_test.py
```

PyTest automatically detects and runs test files that **start with `test_` or end with `_test.py`**.

You can also run all tests in a directory with:
```bash
pytest
```

If a test fails, PyTest provides detailed output to help debug the issue.

---

## **5. Checking Test Coverage**
To check how much of your code is tested, use:
```bash
pytest --cov=ex50
```

This shows which lines of `ex50.py` were executed during testing and highlights untested areas.

---

## **6. Best Practices for Efficient Testing**
1. **Write tests from a user’s perspective** – Simulate real-world use cases.
2. **Test both valid and invalid inputs** – Ensure your program handles errors gracefully.
3. **Use coverage reports** – Identify untested parts of the code.
4. **Remove unnecessary code** – If a function isn’t being tested, ask if it’s needed.
5. **Monitor external services** – If your code depends on external APIs, write tests to confirm they work.

---

### **🔹 Understanding Terms Used in PyTest Testing Code**  

When writing tests in PyTest, we use various **keywords, decorators, assertions, fixtures, and configurations** to define and manage test cases effectively. Let's go over them **one by one with examples**.  

---

## **1️⃣ Test Functions & Naming Conventions**
PyTest **automatically detects test cases** based on naming patterns:  
- **Test files** must start with `test_` or end with `_test.py`.  
- **Test functions** must start with `test_`.  

✅ **Example:**  
```python
# test_example.py
def test_addition():
    assert 2 + 2 == 4  # Passes ✅
```
---

## **2️⃣ Assertions (`assert` Keyword)**
Assertions **check if a condition is True**. If False, the test **fails**.  

✅ **Examples:**  
```python
def test_numbers():
    assert 10 > 5  # ✅ Passes
    assert "hello".upper() == "HELLO"  # ✅ Passes
    assert len([1, 2, 3]) == 3  # ✅ Passes
```
💡 **If an assertion fails, PyTest shows the failure message.**  

---

## **3️⃣ Using `pytest` for Advanced Assertions**
PyTest provides **extra assertion features**, like checking exceptions and warnings.

✅ **Checking if an Exception is Raised**
```python
import pytest

def divide(x, y):
    return x / y

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)  # This should raise an error ✅
```
✔️ The test **expects** a `ZeroDivisionError`, so it **passes**.  

---

## **4️⃣ Parametrization (`@pytest.mark.parametrize`)**
Instead of writing multiple similar test cases, we can **run the same test with different values**.

✅ **Example:**
```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (5, 5, 10),
    (-1, 1, 0)
])
def test_add(a, b, expected):
    assert a + b == expected  # Runs the test with different values
```
✔️ PyTest **runs this test three times** with different values.

---

## **5️⃣ PyTest Fixtures (`@pytest.fixture`)**
Fixtures help **set up and tear down test environments** (like creating a database connection).  

✅ **Example:**
```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "John", "age": 30}

def test_sample_data(sample_data):
    assert sample_data["name"] == "John"
    assert sample_data["age"] == 30
```
✔️ The `sample_data` **fixture runs before the test starts**.

---

## **6️⃣ Skipping & Marking Tests (`@pytest.mark.skip`, `@pytest.mark.xfail`)**
Sometimes, we want to **skip** a test or mark it as **expected to fail**.

✅ **Skipping a Test**
```python
import pytest

@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    assert 2 + 2 == 5  # This test will be skipped 🚀
```

✅ **Expected Failure (`xfail`)**
```python
@pytest.mark.xfail
def test_known_bug():
    assert 10 / 0  # Expected to fail but won't break the test run
```
✔️ The test **fails but does not stop execution**.

---

## **7️⃣ Running Tests with PyTest CLI**
Some useful **pytest commands** to run tests:

| Command | Description |
|---------|-------------|
| `pytest` | Runs all tests in the current directory |
| `pytest -v` | Runs tests in **verbose mode** |
| `pytest -s` | Shows `print()` statements in test output |
| `pytest -k "test_name"` | Runs only tests matching `"test_name"` |
| `pytest --maxfail=2` | Stops after **2 failures** |
| `pytest --cov=my_project` | Runs **test coverage analysis** |

✅ **Example:**  
```bash
pytest -v test_example.py  # Runs test_example.py in verbose mode
```

---

## **8️⃣ Using PyTest Configurations (`pytest.ini`)**
Instead of writing `pytest` commands manually, we can configure **default behavior** using a `pytest.ini` file.

✅ **Example (`pytest.ini` file in project root):**
```ini
[pytest]
addopts = -v --tb=short
testpaths = tests  # Run tests only inside the 'tests/' folder
```
✔️ **Now, running `pytest` automatically uses these settings.**  

---

## **🔹 Summary of Important PyTest Terms**
| Term | Description |
|------|-------------|
| `assert` | Checks if a condition is True (test passes) or False (test fails) |
| `pytest.mark.parametrize` | Runs the same test multiple times with different values |
| `pytest.fixture` | Provides reusable setup data for tests |
| `pytest.raises` | Checks if an exception is raised |
| `pytest.mark.skip` | Skips a test |
| `pytest.mark.xfail` | Marks a test as "expected to fail" |
| `pytest.ini` | Configures pytest settings |
| `__pycache__` | Stores compiled test files for faster execution |

---


---

### **Want to learn more?**
Would you like:
- **Hands-on examples with real projects?**  
- **Exploring mocking/stubs for complex testing?**  
- **Integration with CI/CD tools like GitHub Actions?**  

Let me know how deep you want to go! 🚀🔥


## **7. Key Takeaways**
- Automated testing **saves time and improves code reliability**.
- PyTest makes writing tests simple with **assertions**.
- Running `pytest` executes all test files automatically.
- Use **coverage reports** to identify missing test cases.
- Following best testing practices ensures robust software.

By mastering PyTest, you can write **high-quality, bug-free Python programs** with confidence! 🚀





# Exception Handling in Python

## **Introduction**
Exception handling in Python is a mechanism that allows you to gracefully handle runtime errors in your program. Errors can arise due to various reasons such as incorrect user input, division by zero, file not found, or incorrect data types. Instead of terminating the program abruptly, Python provides a structured way to handle these errors using **try-except** blocks.

This chapter covers:
- **What are exceptions?**
- **Handling exceptions using `try-except` blocks**
- **Using `else` and `finally` with exceptions**
- **Raising exceptions manually using `raise`**
- **User-defined exceptions**
- **Assertions in Python**

---
## **1. What is an Exception?**
An exception is an **error that occurs during program execution** that disrupts the normal flow of instructions. Common causes include:
- Division by zero
- Accessing a file that doesn’t exist
- Using an incorrect data type for an operation
- Indexing an out-of-range element in a list

Python provides built-in exception classes to handle such cases.

**Example:**
```python
print(10 / 0)  # ZeroDivisionError
```
**Output:**
```
ZeroDivisionError: division by zero
```
---
## **2. Handling Exceptions with `try-except` Blocks**
Python uses `try-except` to catch exceptions and prevent the program from crashing.

### **Basic Syntax:**
```python
try:
    # Code that may cause an exception
except ExceptionType:
    # Code to handle the exception
```

### **Example:**
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")
```
**Input & Output:**
```
Enter a number: 0
Error: Cannot divide by zero!
```
---
## **3. Using `else` and `finally` in Exception Handling**
### **Using `else` Clause**
- The `else` block runs **only if no exception occurs** in the `try` block.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print("Result:", result)  # Executes only if no exception occurs
```

### **Using `finally` Clause**
- The `finally` block **always executes**, regardless of whether an exception occurred or not.

```python
try:
    file = open("testfile.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
finally:
    print("Closing the file...")
    file.close()  # Always executes
```

---
## **4. Raising Exceptions Using `raise`**
Sometimes, you might want to raise exceptions manually using the `raise` statement.

### **Example:**
```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older!")
    return "Access granted"

try:
    print(check_age(16))
except ValueError as e:
    print("Exception occurred:", e)
```
**Output:**
```
Exception occurred: Age must be 18 or older!
```

---
## **5. User-Defined Exceptions**
You can define your own exceptions by inheriting from the built-in `Exception` class.

### **Example:**
```python
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print("Caught an exception:", e)
```

**Output:**
```
Caught an exception: This is a custom error!
```
---
## **6. Assertions in Python**
Assertions are used to verify that a condition is true during development. If the condition is false, an `AssertionError` is raised.

### **Example:**
```python
def KelvinToFahrenheit(temp):
    assert temp >= 0, "Temperature below absolute zero!"
    return (temp - 273) * 1.8 + 32

print(KelvinToFahrenheit(300))  # Valid case
print(KelvinToFahrenheit(-10))  # Raises AssertionError
```
**Output:**
```
AssertionError: Temperature below absolute zero!
```

---
## **7. Common Built-in Exceptions in Python**
| Exception | Description |
|-----------|-------------|
| `ZeroDivisionError` | Raised when dividing by zero |
| `ValueError` | Raised when an operation receives an invalid argument |
| `TypeError` | Raised when an operation is performed on an incorrect data type |
| `IndexError` | Raised when accessing an invalid index in a list |
| `KeyError` | Raised when a key is not found in a dictionary |
| `FileNotFoundError` | Raised when a file does not exist |
| `AssertionError` | Raised when an assertion fails |
| `ImportError` | Raised when an import fails |

---
## **8. Best Practices for Exception Handling**
✅ **Use specific exception handling** instead of a generic `except:` clause.
```python
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
```

✅ **Use `finally` for resource cleanup** (e.g., closing files or database connections).
```python
try:
    file = open("data.txt", "r")
finally:
    file.close()
```

✅ **Avoid using bare `except:` as it catches all exceptions, including system-exiting exceptions.**
```python
try:
    risky_code()
except Exception as e:
    print("An error occurred:", e)
```

✅ **Use logging instead of print statements to track exceptions.**
```python
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR)
try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("Exception occurred", exc_info=True)
```

Here is a comprehensive explanation of **Standard Built-in Exceptions in Python**, along with detailed examples for each.  

---

# **Standard Built-in Exceptions in Python**
Python provides a rich set of **built-in exceptions** that help in handling errors efficiently. These exceptions are organized in a hierarchical structure, making debugging and error handling easier.  

---

## **Hierarchy of Built-in Exceptions**
Python exceptions are derived from the `BaseException` class, which is at the top of the hierarchy. Below is a simplified representation of the exception hierarchy:

```
BaseException
│
├── SystemExit
├── KeyboardInterrupt
├── Exception
│   ├── ArithmeticError
│   │   ├── FloatingPointError
│   │   ├── OverflowError
│   │   ├── ZeroDivisionError
│   ├── AssertionError
│   ├── AttributeError
│   ├── EOFError
│   ├── ImportError
│   │   ├── ModuleNotFoundError
│   ├── LookupError
│   │   ├── IndexError
│   │   ├── KeyError
│   ├── NameError
│   │   ├── UnboundLocalError
│   ├── OSError
│   │   ├── FileNotFoundError
│   ├── RuntimeError
│   │   ├── NotImplementedError
│   ├── SyntaxError
│   │   ├── IndentationError
│   ├── TypeError
│   ├── ValueError
```

---

## **List of Built-in Exceptions with Examples**

### **1. Exception**
**Base class for all exceptions.** It is not raised directly but is inherited by all other exceptions.  

Example:
```python
try:
    raise Exception("This is a custom exception.")
except Exception as e:
    print(f"Exception caught: {e}")
```
**Output:**
```
Exception caught: This is a custom exception.
```

---

### **2. StopIteration**
Raised when the `next()` method of an iterator reaches the end.  

Example:
```python
it = iter([1, 2, 3])
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # Raises StopIteration
```
**Output:**
```
1
2
3
Traceback (most recent call last):
    print(next(it))
StopIteration
```

---

### **3. SystemExit**
Raised when `sys.exit()` is called to terminate the program.  

Example:
```python
import sys
try:
    sys.exit("Exiting program")
except SystemExit as e:
    print(f"SystemExit: {e}")
```
**Output:**
```
SystemExit: Exiting program
```

---

### **4. ArithmeticError**
Base class for errors occurring in numeric calculations.  

Example:
```python
try:
    raise ArithmeticError("Arithmetic error occurred")
except ArithmeticError as e:
    print(e)
```
**Output:**
```
Arithmetic error occurred
```

---

### **5. OverflowError**
Raised when a mathematical calculation exceeds the limits of a numeric type.  

Example:
```python
import math
try:
    print(math.exp(1000))  # Exponential function
except OverflowError:
    print("OverflowError: Number too large!")
```
**Output:**
```
OverflowError: Number too large!
```

---

### **6. FloatingPointError**
Raised when a floating point operation fails (rarely occurs in Python).  

Example:
```python
import sys
sys.float_info.max  # Maximum float value
```

---

### **7. ZeroDivisionError**
Raised when dividing a number by zero.  

Example:
```python
try:
    x = 5 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
```
**Output:**
```
Error: division by zero
```

---

### **8. AssertionError**
Raised when an `assert` statement fails.  

Example:
```python
try:
    assert 2 + 2 == 5, "Math is broken!"
except AssertionError as e:
    print(e)
```
**Output:**
```
Math is broken!
```

---

### **9. AttributeError**
Raised when an invalid attribute is accessed on an object.  

Example:
```python
class Test:
    pass

obj = Test()
try:
    obj.value
except AttributeError as e:
    print(e)
```
**Output:**
```
'Test' object has no attribute 'value'
```

---

### **10. EOFError**
Raised when input() reaches end-of-file (EOF).  

Example:
```python
try:
    data = input()
except EOFError:
    print("EOFError: End of input reached")
```

---

### **11. ImportError**
Raised when an import fails.  

Example:
```python
try:
    import non_existent_module
except ImportError as e:
    print(f"ImportError: {e}")
```
**Output:**
```
ImportError: No module named 'non_existent_module'
```

---

### **12. KeyboardInterrupt**
Raised when a user interrupts execution (e.g., pressing `Ctrl + C`).  

Example:
```python
try:
    while True:
        pass  # Infinite loop
except KeyboardInterrupt:
    print("Execution interrupted by user!")
```

---

### **13. LookupError**
Base class for lookup errors (e.g., `IndexError`, `KeyError`).  

Example:
```python
try:
    raise LookupError("Generic lookup error")
except LookupError as e:
    print(e)
```

---

### **14. IndexError**
Raised when trying to access an index that is out of range.  

Example:
```python
numbers = [10, 20, 30]
try:
    print(numbers[5])
except IndexError as e:
    print(f"Error: {e}")
```
**Output:**
```
Error: list index out of range
```

---

### **15. KeyError**
Raised when trying to access a non-existent dictionary key.  

Example:
```python
d = {"name": "Alice"}
try:
    print(d["age"])
except KeyError as e:
    print(f"KeyError: {e}")
```
**Output:**
```
KeyError: 'age'
```

---

### **16. NameError**
Raised when a variable is not defined.  

Example:
```python
try:
    print(x)
except NameError as e:
    print(f"NameError: {e}")
```
**Output:**
```
NameError: name 'x' is not defined
```

---

### **17. UnboundLocalError**
Raised when a local variable is referenced before assignment.  

Example:
```python
def example():
    print(x)
    x = 10

try:
    example()
except UnboundLocalError as e:
    print(f"Error: {e}")
```
**Output:**
```
Error: local variable 'x' referenced before assignment
```

---

### **18. TypeError**
Raised when an operation is applied to an incorrect data type.  

Example:
```python
try:
    print("Hello" + 5)
except TypeError as e:
    print(f"TypeError: {e}")
```

---

### **19. ValueError**
Raised when a function receives an invalid argument.  

Example:
```python
try:
    num = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")
```

---

### **20. NotImplementedError**
Raised when an abstract method is not implemented in a subclass.  

Example:
```python
class Parent:
    def method(self):
        raise NotImplementedError("Subclasses must implement this!")

class Child(Parent):
    pass

c = Child()
c.method()
```

---


---
## **9. Summary**
- Exceptions allow graceful handling of runtime errors.
- `try-except` blocks catch exceptions and prevent crashes.
- `else` executes when no exception occurs; `finally` executes always.
- `raise` is used to manually trigger exceptions.
- Custom exceptions can be created by subclassing `Exception`.
- Assertions help with debugging by enforcing conditions.

By mastering exception handling, you ensure **robust, error-free, and maintainable** Python applications! 🚀



