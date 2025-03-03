This topic introduces **data munging**, a crucial skill in software development where we clean and transform raw data into a usable format. It also explains a structured **process for problem-solving** in programming, particularly for **extracting data from PDFs**.  

---

# **Understanding Data Munging**
### **What is Data Munging?**
**Data munging** (also called **data wrangling**) refers to cleaning, restructuring, and enriching raw data to make it suitable for analysis or processing. It’s a fundamental step in **data science, automation, and backend development.**  

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
