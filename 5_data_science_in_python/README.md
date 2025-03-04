This topic introduces **data munging**, a crucial skill in software development where we clean and transform raw data into a usable format. It also explains a structured **process for problem-solving** in programming, particularly for **extracting data from PDFs**.  

---

# **Understanding Data Munging**
### **What is Data Munging?**
**Data munging** (also called **data wrangling**) refers to cleaning, restructuring, and enriching raw data to make it suitable for analysis or processing. It’s a fundamental step in **data science, automation, and backend development.**  

<p align="center"> 
<img  src="https://github.com/user-attachments/assets/1b10c06c-c033-4009-9772-66d0ae10619d" alt="Material Bread logo">
</p>

### **Why is Data Munging Important?**
- **Real-world data is messy.** It comes in inconsistent formats, often with missing values.
- **It’s required in many fields** like machine learning, analytics, automation, and data visualization.
- **Improperly cleaned data leads to errors** in applications and analysis.
- **It automates tedious tasks**, making processes more efficient.

---

# **Example Project: Extracting Data from PDFs**
### **The Problem Statement**
Your manager asks you to **find the amount of beer manufactured in the US every month**. However:
- The data is available only in a **PDF format** from the **ATF (Alcohol, Tobacco, and Firearms Department)**.
- Your task is to **extract specific statistics from the PDF**.

### **Required Data**
We need to extract:
1. **Reporting Period**  
2. **Report Date**  
3. **Production Data** (for the current month, prior year, and cumulative to date)  
4. **Stock on Hand Data** (for the current month and prior year)  
5. **Calculate Sales** = **Production** - **Stock on Hand**  

### **Solution Overview**
Since the data is locked inside a **PDF file**, we’ll use **pdftotext** to extract and process the content.

---

# **Step-by-Step Guide to Data Munging**
### **1️⃣ Install Required Libraries**
We need `pdftotext` to extract text from PDFs.

#### **Installation using Conda**
```bash
conda activate lpythw
conda install pdftotext
```

#### **Installation using pip (if Conda is not available)**
```bash
pip install pdftotext
```

---

### **2️⃣ Extract Text from the PDF**
```python
import pdftotext

# Open the PDF file
with open("beer_statistics.pdf", "rb") as file:
    pdf = pdftotext.PDF(file)

# Convert PDF pages into a single text string
pdf_text = "\n".join(pdf)

# Print extracted text
print(pdf_text)
```
🔹 **Explanation:**
- We open the **PDF file** in **binary mode** (`rb`).
- `pdftotext.PDF(file)` extracts text from the PDF.
- `"\n".join(pdf)` merges all pages into a **single text string**.
- Finally, we print the **raw extracted text** to analyze its structure.

---

### **3️⃣ Identify and Extract Relevant Information**
After printing the extracted text, we need to locate key information (dates, production, stock levels, etc.).

```python
import re

# Extract reporting period using regex
reporting_period = re.search(r"Reporting Period:\s*(.*)", pdf_text)
report_date = re.search(r"Report Date:\s*(.*)", pdf_text)

# Extract production and stock values
production_current_month = re.search(r"Production for Current Month:\s*([\d,]+)", pdf_text)
stock_current_month = re.search(r"Stocks on Hand End of Month:\s*([\d,]+)", pdf_text)

# Convert extracted values to usable format
reporting_period = reporting_period.group(1) if reporting_period else "Not found"
report_date = report_date.group(1) if report_date else "Not found"
production_current_month = int(production_current_month.group(1).replace(",", "")) if production_current_month else 0
stock_current_month = int(stock_current_month.group(1).replace(",", "")) if stock_current_month else 0

# Calculate sales
sales = production_current_month - stock_current_month

# Print extracted data
print(f"Reporting Period: {reporting_period}")
print(f"Report Date: {report_date}")
print(f"Production (Current Month): {production_current_month}")
print(f"Stock (End of Month): {stock_current_month}")
print(f"Sales: {sales}")
```
🔹 **Explanation:**
- We use **regular expressions (regex)** to find specific patterns in the extracted text.
- `.group(1)` extracts the **first matching group** (actual value).
- `.replace(",", "")` removes commas from numbers.
- `int()` converts values into integers for calculations.
- We **calculate sales** as `Production - Stock on Hand`.

---

# **Step-by-Step Approach to Solving Any Problem**
This process ensures **structured thinking** while solving problems.

### **1️⃣ Create a File or Project**
Start by creating a Python file (`extract_beer_stats.py`) instead of **staring at the screen**.

```bash
touch extract_beer_stats.py
```

---

### **2️⃣ Describe the Problem Inside the File**
Before coding, write a **clear description** in comments.

```python
# This script extracts beer production statistics from a PDF file.
# It retrieves:
# - Reporting period
# - Report date
# - Production and stock levels
# - Sales data
```

---

### **3️⃣ Convert Description into Comments for Each Step**
Break down the **high-level problem** into smaller **steps**.

```python
# Step 1: Install and import necessary libraries
# Step 2: Open and read the PDF file
# Step 3: Extract text content
# Step 4: Identify relevant data using regex
# Step 5: Convert extracted data into numerical format
# Step 6: Calculate sales as Production - Stock on Hand
# Step 7: Print the results
```

---

### **4️⃣ Write Pseudo-Code (Rough Sketch of Logic)**
Before writing actual code, **write it in plain English**.

```python
# Open PDF file
# Extract text using pdftotext
# Search for key terms: "Reporting Period", "Report Date", etc.
# Convert extracted values into numbers
# Compute the sales: Production - Stock
# Print the final report
```

---

### **5️⃣ Convert Pseudo-Code into Python**
Write and test the actual implementation **step by step** (as shown in the example above).

---

### **6️⃣ Run the Code and Debug Issues**
Run your script frequently to catch **early errors**.

```bash
python extract_beer_stats.py
```

---

### **7️⃣ Clean and Optimize the Code**
Once working:
- **Remove unnecessary print statements.**
- **Optimize regex patterns.**
- **Structure code using functions.**

---

### **8️⃣ Repeat the Process (Refine & Improve)**
After getting a working solution, **rewrite it** without looking at the original code to strengthen understanding.

---

Here’s a well-structured **documentation** for your **PDF data extraction program**. This documentation includes an explanation of the **Python scripts**, **execution commands**, and **expected outputs** for both **single PDF processing** and **multiple PDF processing**.

---

# **📌 PDF Data Extraction & Reporting Using Python**

## **1️⃣ Overview**
This script extracts specific data from **beer statistics reports (PDF files)** using `pdftotext`. The extracted data includes:
- **Reporting Period**
- **Report Date**
- **Production for Current Month**
- **Stocks on Hand End of Month**
- **Sales Calculation (Production - Stocks)**

---

## **2️⃣ Prerequisites**
Before running the script, ensure you have installed the required dependencies:

### **🔹 Install `pdftotext`**
```bash
pip install pdftotext
```
OR, if using **Conda**:
```bash
conda install -c conda-forge pdftotext
```

### **🔹 Check if Installed**
To verify that `pdftotext` is installed, run:
```bash
python -c "import pdftotext; print('pdftotext is installed!')"
```
If you see `pdftotext is installed!`, you're ready to proceed.

---

## **3️⃣ Extracting Data from a Single PDF**
The script processes a **single PDF file** and extracts the required information.

### **📌 Python Code (`extract_single_pdf.py`)**
```python
import pdftotext
import sys
import re  # Import regex module

# Ensure a file argument is provided
if len(sys.argv) < 2:
    print("Usage: python extract_single_pdf.py <pdf_file>")
    sys.exit(1)

pdf_file = sys.argv[1]

try:
    print(f"\n🔹 Processing: {pdf_file} 🔹\n")  # Print which file is being processed

    # Open the PDF
    with open(pdf_file, "rb") as infile:
        pdf = pdftotext.PDF(infile)

    # Convert PDF pages into text
    text = "\n".join(pdf)  # Combine all text into a single string

    # Extract reporting period and report date
    reporting_period = re.search(r"Reporting Period:\s*([A-Za-z]+\s\d{4})", text)
    report_date = re.search(r"Report Date:\s*([\dA-Z]+)", text)

    # Extract production and stock values
    production_current_month = re.search(r"Production[\s\S]*?\n([\d,]+)", text)
    stock_current_month = re.search(r"Stocks On Hand End-of-Month\s*\n([\d,]+)", text)

    # Convert extracted values to usable format
    reporting_period = reporting_period.group(1).strip() if reporting_period else "Not found"
    report_date = report_date.group(1).strip() if report_date else "Not found"
    production_current_month = int(production_current_month.group(1).replace(",", "")) if production_current_month else 0
    stock_current_month = int(stock_current_month.group(1).replace(",", "")) if stock_current_month else 0

    # Calculate sales
    sales = production_current_month - stock_current_month

    # Display extracted values
    print(f"📅 Reporting Period: {reporting_period}")
    print(f"📅 Reporting Date: {report_date}")
    print(f"🏭 Production (Current Month): {production_current_month}")
    print(f"📦 Stocks on Hand End of Month: {stock_current_month}")
    print(f"📊 Sales (Production - Stocks): {sales}")

except FileNotFoundError:
    print(f"❌ Error: The file '{pdf_file}' was not found.")
except pdftotext.Error as e:
    print(f"❌ Error processing PDF '{pdf_file}': {e}")
except Exception as e:
    print(f"❌ Unexpected error with '{pdf_file}': {e}")
```

---

### **📌 Running the Script for a Single PDF**
To extract data from **one PDF**, run:
```bash
python extract_single_pdf.py beer_november.pdf
```

### **📌 Expected Output**
```
🔹 Processing: beer_november.pdf 🔹

📅 Reporting Period: November 2021
📅 Reporting Date: 09MAR2022
🏭 Production (Current Month): 13094569
📦 Stocks on Hand End of Month: 10607001
📊 Sales (Production - Stocks): 2487568
```

---

## **4️⃣ Extracting Data from Multiple PDFs**
The script now supports **multiple PDFs**, processing each one separately and displaying results.

### **📌 Python Code (`extract_multiple_pdfs.py`)**
```python
import pdftotext
import sys
import re  # Import regex module

# Ensure at least one file argument is provided
if len(sys.argv) < 2:
    print("Usage: python extract_multiple_pdfs.py <pdf_file1> <pdf_file2> ...")
    sys.exit(1)

pdf_files = sys.argv[1:]  # Get all PDF filenames passed as arguments

for pdf_file in pdf_files:
    try:
        print(f"\n🔹 Processing: {pdf_file} 🔹\n")  # Print which file is being processed

        # Open the PDF
        with open(pdf_file, "rb") as infile:
            pdf = pdftotext.PDF(infile)

        # Convert PDF pages into text
        text = "\n".join(pdf)  # Combine all text into a single string

        # Extract reporting period and report date
        reporting_period = re.search(r"Reporting Period:\s*([A-Za-z]+\s\d{4})", text)
        report_date = re.search(r"Report Date:\s*([\dA-Z]+)", text)

        # Extract production and stock values
        production_current_month = re.search(r"Production[\s\S]*?\n([\d,]+)", text)
        stock_current_month = re.search(r"Stocks On Hand End-of-Month\s*\n([\d,]+)", text)

        # Convert extracted values to usable format
        reporting_period = reporting_period.group(1).strip() if reporting_period else "Not found"
        report_date = report_date.group(1).strip() if report_date else "Not found"
        production_current_month = int(production_current_month.group(1).replace(",", "")) if production_current_month else 0
        stock_current_month = int(stock_current_month.group(1).replace(",", "")) if stock_current_month else 0

        # Calculate sales
        sales = production_current_month - stock_current_month

        # Display extracted values for this PDF
        print(f"📅 Reporting Period: {reporting_period}")
        print(f"📅 Reporting Date: {report_date}")
        print(f"🏭 Production (Current Month): {production_current_month}")
        print(f"📦 Stocks on Hand End of Month: {stock_current_month}")
        print(f"📊 Sales (Production - Stocks): {sales}")
        print("-" * 50)  # Separator for better readability

    except FileNotFoundError:
        print(f"❌ Error: The file '{pdf_file}' was not found.")
    except pdftotext.Error as e:
        print(f"❌ Error processing PDF '{pdf_file}': {e}")
    except Exception as e:
        print(f"❌ Unexpected error with '{pdf_file}': {e}")
```

---

### **📌 Running the Script for Multiple PDFs**
To process **multiple PDFs**, run:
```bash
python extract_multiple_pdfs.py beer_november.pdf beer_october.pdf beer_september.pdf
```

### **📌 Expected Output**
```
🔹 Processing: beer_november.pdf 🔹
📅 Reporting Period: November 2021
📅 Reporting Date: 09MAR2022
🏭 Production (Current Month): 13094569
📦 Stocks on Hand End of Month: 10607001
📊 Sales (Production - Stocks): 2487568
--------------------------------------------------

🔹 Processing: beer_october.pdf 🔹
📅 Reporting Period: October 2021
📅 Reporting Date: 12JAN2022
🏭 Production (Current Month): 12084500
📦 Stocks on Hand End of Month: 9805000
📊 Sales (Production - Stocks): 2280000
--------------------------------------------------
```

---

### **📌 Exploring More Features in the `pdftotext` Library**
The `pdftotext` library is a **lightweight** and **efficient** Python wrapper for extracting text from PDF files.  
It provides several features to **control how text is extracted and processed**.

---

## **🔹 1. Basic PDF Text Extraction**
### ✅ **Extracting Text from a PDF**
```python
import pdftotext

# Open the PDF file in binary mode
with open("sample.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)  # Load the PDF

# Convert the entire PDF into a single text string
text = "\n".join(pdf)  # Joins all pages into one text block
print(text)  # Prints the extracted text
```
✔️ **Default behavior**: Extracts text from all pages and joins them with `\n`.

---

## **🔹 2. Extracting Text Page by Page**
By default, `pdf` behaves **like a list**, where each **element represents one page**.

### ✅ **Extracting Text from a Specific Page**
```python
# Extract text from the first page (index 0)
print(pdf[0])
```

### ✅ **Looping Through All Pages**
```python
for page_number, page in enumerate(pdf):
    print(f"Page {page_number + 1}:")
    print(page)
    print("-" * 50)  # Page separator
```
✔️ **Useful when analyzing PDFs where different pages have different formats**.

---

## **🔹 3. Extracting Text with Layout Preservation**
Some PDFs contain **formatted text (columns, tables, etc.)**, and extracting plain text **may distort their structure**.  
`pdftotext` allows preserving layout using the `layout=True` option.

### ✅ **Preserving the Original Layout**
```python
with open("formatted.pdf", "rb") as f:
    pdf = pdftotext.PDF(f, layout=True)  # Preserve original text formatting

print("\n".join(pdf))  # Display formatted text
```
✔️ **This is useful for documents with tables, columns, or structured text.**

---

## **🔹 4. Extracting Text from Encrypted PDFs**
If a **PDF is password-protected**, `pdftotext` allows you to **unlock** it before extracting text.

### ✅ **Handling Password-Protected PDFs**
```python
with open("protected.pdf", "rb") as f:
    pdf = pdftotext.PDF(f, password="mypassword")  # Provide the password

print("\n".join(pdf))  # Extract text
```
✔️ If the password is incorrect, it will raise a `RuntimeError`.

---

## **🔹 5. Checking Number of Pages in a PDF**
### ✅ **Getting the Total Page Count**
```python
print(f"Total pages in PDF: {len(pdf)}")
```
✔️ **Useful for handling multi-page PDFs dynamically**.

---

## **🔹 6. Saving Extracted Text to a File**
Instead of printing the text, we can **save it to a `.txt` file**.

### ✅ **Writing Extracted Text to a File**
```python
with open("output.txt", "w", encoding="utf-8") as out_file:
    out_file.write("\n".join(pdf))
```
✔️ This is **useful for data storage, further processing, or manual analysis**.

---

## **🔹 7. Extracting Text from PDFs in a Folder**
If you have **multiple PDFs**, you can process them in a loop.

### ✅ **Batch Processing Multiple PDFs**
```python
import os

folder = "pdf_reports/"
for filename in os.listdir(folder):
    if filename.endswith(".pdf"):
        with open(os.path.join(folder, filename), "rb") as f:
            pdf = pdftotext.PDF(f)
            print(f"\n🔹 Extracting text from: {filename}")
            print("\n".join(pdf))
            print("-" * 80)
```
✔️ **This is useful for processing multiple reports automatically.**

---

## **🔹 8. Error Handling in `pdftotext`**
### ✅ **Catching PDF Processing Errors**
```python
try:
    with open("sample.pdf", "rb") as f:
        pdf = pdftotext.PDF(f)
    print("\n".join(pdf))

except FileNotFoundError:
    print("❌ Error: The PDF file was not found.")
except pdftotext.Error as e:
    print(f"❌ PDF Processing Error: {e}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
```
✔️ **Prevents script crashes when dealing with missing files or unreadable PDFs.**

---

## **🔹 Summary of Key Features**
| Feature | Usage |
|---------|-------|
| **Basic Extraction** | `pdf = pdftotext.PDF(f)` |
| **Extract a Specific Page** | `pdf[0]` |
| **Extract All Pages** | `"\n".join(pdf)` |
| **Preserve Layout** | `pdf = pdftotext.PDF(f, layout=True)` |
| **Process Encrypted PDFs** | `pdf = pdftotext.PDF(f, password="mypassword")` |
| **Get Page Count** | `len(pdf)` |
| **Save Text to File** | `out_file.write("\n".join(pdf))` |
| **Process Multiple PDFs** | Loop through `os.listdir(folder)` |
| **Error Handling** | Use `try-except` blocks |

---


# **📌 Complete Guide to `re` (Regular Expressions) in Python**

The `re` module in Python is used for **pattern matching and text processing** using **regular expressions (regex)**.  
It helps in searching, extracting, and manipulating text efficiently.

---

## **🔹 1. Importing the `re` Module**
```python
import re  # Required for using regular expressions
```
Once imported, you can use various **functions and methods** provided by `re`.

---

# **📌 Key Functions in `re`**
Python's `re` module provides several functions to work with **regular expressions**.

| **Function** | **Description** |
|-------------|----------------|
| `re.match()` | Checks for a match at the **beginning** of a string |
| `re.search()` | Searches **anywhere** in the string for a match |
| `re.findall()` | Returns **all matches** in a list |
| `re.finditer()` | Returns an **iterator of match objects** |
| `re.split()` | Splits a string based on a pattern |
| `re.sub()` | Replaces occurrences of a pattern with another string |
| `re.compile()` | Compiles a regular expression pattern for reuse |

---

# **📌 2. `re.match()` - Match at the Beginning of a String**
The `match()` function checks if the pattern **matches from the start** of the string.

### ✅ **Example: Matching a Word at the Start**
```python
import re

text = "Hello, welcome to Python!"
pattern = r"Hello"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())  # Output: Match found: Hello
else:
    print("No match found")
```
✔️ **Returns `None`** if the pattern is **not at the beginning**.

---

# **📌 3. `re.search()` - Find First Match Anywhere**
The `search()` function **searches the entire string** for the pattern.

### ✅ **Example: Searching for a Word**
```python
text = "The price is 100 dollars"
pattern = r"\d+"  # Matches numbers

match = re.search(pattern, text)
if match:
    print("Match found:", match.group())  # Output: Match found: 100
```
✔️ **Finds the first occurrence** of the pattern.

---

# **📌 4. `re.findall()` - Find All Matches**
The `findall()` function returns **all occurrences** of a pattern in a list.

### ✅ **Example: Finding All Numbers**
```python
text = "Order 5 apples, 3 bananas, and 10 oranges."
pattern = r"\d+"  # Match all numbers

matches = re.findall(pattern, text)
print("Matches:", matches)  # Output: Matches: ['5', '3', '10']
```
✔️ **Returns a list of matches** instead of a match object.

---

# **📌 5. `re.finditer()` - Get Match Objects**
The `finditer()` function returns an **iterator of match objects**.

### ✅ **Example: Finding All Numbers with Positions**
```python
text = "Order 5 apples, 3 bananas, and 10 oranges."
pattern = r"\d+"  # Match numbers

matches = re.finditer(pattern, text)
for match in matches:
    print(f"Found {match.group()} at position {match.start()}-{match.end()}")
```
✔️ Provides **more details** about each match.

---

# **📌 6. `re.split()` - Splitting a String**
The `split()` function **splits a string** at each match.

### ✅ **Example: Splitting on Spaces**
```python
text = "Python is an amazing language"
pattern = r"\s+"  # Matches spaces

words = re.split(pattern, text)
print(words)  # Output: ['Python', 'is', 'an', 'amazing', 'language']
```
✔️ **Useful for tokenizing text**.

---

# **📌 7. `re.sub()` - Replacing Text**
The `sub()` function **replaces occurrences** of a pattern.

### ✅ **Example: Replacing Numbers with `XXX`**
```python
text = "My number is 9876543210"
pattern = r"\d+"

new_text = re.sub(pattern, "XXX", text)
print(new_text)  # Output: My number is XXX
```
✔️ **Used for data cleaning or formatting**.

---

# **📌 8. `re.compile()` - Precompiling a Pattern**
The `compile()` function **precompiles** a regex pattern for multiple uses.

### ✅ **Example: Using `compile()` for Repeated Searches**
```python
pattern = re.compile(r"\d+")  # Precompile pattern

text1 = "Order 5 apples, 3 bananas"
text2 = "Stock: 50 units, Price: 100"

print(pattern.findall(text1))  # Output: ['5', '3']
print(pattern.findall(text2))  # Output: ['50', '100']
```
✔️ **Improves performance** for multiple searches.

---

# **📌 Special Regex Symbols and Meta-Characters**
| **Symbol** | **Meaning** | **Example** | **Matches** |
|------------|------------|-------------|-------------|
| `.` | Any character except newline | `r"a.c"` | `"abc"`, `"a1c"` |
| `^` | Start of string | `r"^hello"` | `"hello world"` |
| `$` | End of string | `r"world$"` | `"hello world"` |
| `\d` | Digit (0-9) | `r"\d+"` | `"123"`, `"456"` |
| `\D` | Non-digit | `r"\D+"` | `"abc"`, `"xyz"` |
| `\s` | Whitespace | `r"\s+"` | `" "` (space), `"\t"` (tab) |
| `\S` | Non-whitespace | `r"\S+"` | `"Hello"`, `"Python3"` |
| `\w` | Word character (a-z, A-Z, 0-9, _) | `r"\w+"` | `"hello"`, `"python_3"` |
| `\W` | Non-word character | `r"\W+"` | `"@"`, `"!"` |
| `\b` | Word boundary | `r"\bword\b"` | `" word "` |
| `+` | One or more repetitions | `r"\d+"` | `"123"`, `"9"` |
| `*` | Zero or more repetitions | `r"ab*"` | `"a"`, `"abb"` |
| `?` | Zero or one repetition | `r"colou?r"` | `"color"`, `"colour"` |
| `{m,n}` | Between `m` and `n` repetitions | `r"\d{2,4}"` | `"12"`, `"1234"` |
| `( )` | Capturing group | `r"(ab)+"` | `"abab"` |
| `|` | OR (matches either pattern) | `r"cat|dog"` | `"cat"`, `"dog"` |

---

# **📌 Summary of `re` Functions**
| **Function** | **Purpose** | **Returns** |
|-------------|------------|-------------|
| `re.match()` | Match at the beginning of a string | `Match object` or `None` |
| `re.search()` | Find first occurrence anywhere | `Match object` or `None` |
| `re.findall()` | Find all occurrences | `List of matches` |
| `re.finditer()` | Find all occurrences with details | `Iterator of Match objects` |
| `re.split()` | Split string at pattern | `List of substrings` |
| `re.sub()` | Replace occurrences | `New string` |
| `re.compile()` | Precompile pattern for reuse | `Compiled pattern object` |

---

# **🚀 Final Thoughts**
✅ The `re` module provides **powerful** text searching and manipulation tools.  
✅ Understanding **regular expressions** makes **text extraction, validation, and formatting easy**.  
✅ Using `re.compile()` improves performance **for repeated searches**.  


### **🚀 Summary**
- ✅ **`extract_single_pdf.py`** → Processes **one PDF at a time**.
- ✅ **`extract_multiple_pdfs.py`** → Processes **multiple PDFs in one run**.
- ✅ **Regex-based extraction** ensures accurate data retrieval.

Let me know if you need any refinements! 🚀😊

# **Key Takeaways**
✅ **Data munging** is essential for cleaning and structuring data for analysis.  
✅ **Python’s pdftotext** allows text extraction from PDFs.  
✅ **Regular expressions (regex)** help extract structured data from unstructured text.  
✅ **A systematic problem-solving approach** helps in writing cleaner, maintainable code.  
✅ **Break down the problem** into steps, write pseudo-code, and refine the solution iteratively.

---

# **Next Steps**
🔹 Improve the script by **handling multiple PDF files** at once.  
🔹 Save extracted data in **CSV or JSON format** for further analysis.  
🔹 Implement **error handling** for missing or malformed data.  
🔹 Automate the process by **scheduling the script** to run periodically.

---

This exercise **bridges the gap between learning Python and using it for real-world tasks**. By following this structured approach, you’ll gain **confidence in applying Python to real projects**. 🚀
