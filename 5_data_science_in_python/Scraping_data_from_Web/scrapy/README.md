This chapter introduces **web scraping** and **automated data extraction** using **Python and BeautifulSoup**. It builds on the previous **data munging** exercise by focusing on **downloading PDFs automatically** from a website instead of doing it manually. 

---

# **1️⃣ Understanding Web Scraping**
### **🔹 What is Web Scraping?**
Web scraping is **the process of extracting data from web pages automatically**. Web pages contain **structured data**, but it's often **designed for human reading rather than for computers**. By scraping the web, we can **extract, clean, and store useful data** for **data science, analysis, or automation**.

### **🔹 Why is Web Scraping Useful?**
✅ Automates repetitive tasks  
✅ Extracts structured data from unstructured web pages  
✅ Feeds data to data science and machine learning models  
✅ Saves time compared to manual data collection  

---

# **2️⃣ Web Scraping Basics**
To scrape a website, you need to:

1️⃣ **Download the HTML page**  
2️⃣ **Parse the HTML structure** to extract specific elements  
3️⃣ **Store the extracted data** for later use  


---

---

# **📌 Web Scraping and PDF Processing in Python**

## **1️⃣ Overview**
This script **scrapes a webpage**, extracts **PDF links**, **downloads PDFs**, extracts **text**, and extracts specific **statistical information** from them.

### **🚀 Key Functionalities**
✅ Scrapes a webpage for **PDF links**  
✅ **Downloads** the PDFs to your local system  
✅ **Extracts text** from each PDF  
✅ **Finds and prints** relevant statistics  

---

## **2️⃣ Required Libraries**
Before running the script, install the required Python libraries using:
```bash
pip install pdftotext beautifulsoup4 html5lib
```

---

## **3️⃣ Understanding the Code**
### **🔹 Importing Required Libraries**
```python
import os
import pdftotext
from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
```
| **Library** | **Purpose** |
|------------|------------|
| `os` | Handles file operations (checking existence, getting paths) |
| `pdftotext` | Extracts text from PDFs |
| `urllib.request` | Fetches content from URLs (downloads PDFs, web requests) |
| `BeautifulSoup` | Parses and extracts data from HTML (scraping) |
| `urljoin` | Converts **relative URLs** to **absolute URLs** |

---

### **🔹 Step 1: Scraping the Web Page**
```python
base_url = "https://learncodethehardway.com/setup/python/ttb/"
response = request.urlopen(base_url)
soup = BeautifulSoup(response, "html5lib")
```
✔️ **`base_url`** → The webpage to scrape PDFs from.  
✔️ **`request.urlopen(base_url)`** → Opens the URL and fetches the HTML content.  
✔️ **`BeautifulSoup(response, "html5lib")`** → Parses the HTML using `"html5lib"`.

---

### **🔹 Step 2: Extracting PDF Links**
```python
pdf_links = [urljoin(base_url, link["href"]) for link in soup.find_all("a", href=True) if link["href"].endswith(".pdf")]
```
✔️ **`soup.find_all("a", href=True)`** → Finds all `<a>` (anchor) tags containing `href`.  
✔️ **`if link["href"].endswith(".pdf")`** → Filters links that **end with `.pdf`**.  
✔️ **`urljoin(base_url, link["href"])`** → Converts **relative PDF URLs** to **absolute URLs**.

🔹 **Example:**  
```html
<a href="/setup/python/ttb/sample.pdf">Download</a>
```
Extracted URL:  
```
https://learncodethehardway.com/setup/python/ttb/sample.pdf
```

---

### **🔹 Step 3: Downloading the PDFs**
```python
for pdf_link in pdf_links[:5]:  # Limit to 5 PDFs
    pdf_name = pdf_link.split("/")[-1]
```
✔️ **`pdf_links[:5]`** → Processes **only the first 5 PDFs**.  
✔️ **`pdf_link.split("/")[-1]`** → Extracts **PDF filename** from the URL.  

🔹 **Example:**
```python
pdf_link = "https://example.com/files/report.pdf"
pdf_name = pdf_link.split("/")[-1]  # "report.pdf"
```

#### **✅ Checking and Downloading the PDF**
```python
if not os.path.exists(pdf_name):
    save_path = os.path.abspath(pdf_name)
    with request.urlopen(pdf_link) as response, open(pdf_name, "wb") as pdf_file:
        pdf_file.write(response.read())
    print(f"\n \n ✅ Downloaded: {pdf_name} at {save_path}")
```
✔️ **`os.path.exists(pdf_name)`** → Checks if the file **already exists**.  
✔️ **`os.path.abspath(pdf_name)`** → Gets the **full path** of the PDF.  
✔️ **`request.urlopen(pdf_link).read()`** → **Downloads the PDF**.  
✔️ **`open(pdf_name, "wb")`** → Saves the PDF in **binary mode (`wb`)**.  

🔹 **Example Output:**
```
✅ Downloaded: Statistical_Report_Beer_December_2021.pdf at E:\python\Scraping_data\Statistical_Report_Beer_December_2021.pdf
```

---

### **🔹 Step 4: Extracting Text from the PDF**
```python
with open(pdf_name, "rb") as f:
    pdf = pdftotext.PDF(f)
```
✔️ **Opens the downloaded PDF** in **binary mode (`"rb"`)**.  
✔️ **Converts the PDF into a `pdftotext.PDF` object**, making it readable as text.

---

### **🔹 Step 5: Extracting Statistics**
```python
for line in "".join(pdf).split("\n"):
    if line.startswith("Reporting Period"):
        print(f"📄 {pdf_name} - {line}")
```
✔️ **`"".join(pdf)`** → Converts **all pages** into a **single string**.  
✔️ **`.split("\n")`** → Splits the text **line by line**.  
✔️ **`if line.startswith("Reporting Period")`** → Filters lines that contain **relevant statistics**.

🔹 **Example PDF Text (Extracted Data)**:
```
Reporting Period: December 2021
Report Date: 10JAN2022
Production for Current Month: 100000
```
🔹 **Output:**
```
📄 Statistical_Report_Beer_December_2021.pdf - Reporting Period: December 2021
```



# **📌 Complete Code (Copy & Paste to Run)**
```python
import os
import pdftotext
from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # Convert relative URLs to absolute URLs

# Step 1: Scrape Web Page
base_url = "https://learncodethehardway.com/setup/python/ttb/"
response = request.urlopen(base_url)
soup = BeautifulSoup(response, "html5lib")

# Step 2: Extract PDF Links
pdf_links = [urljoin(base_url, link["href"]) for link in soup.find_all("a", href=True) if link["href"].endswith(".pdf")]

# Step 3: Create a Download Folder
download_folder = "downloaded_pdfs"
os.makedirs(download_folder, exist_ok=True)  # Creates the folder if it doesn't exist

# Step 4: Download and Process PDFs
for pdf_link in pdf_links[:5]:  # Limit to 5 PDFs
    pdf_name = pdf_link.split("/")[-1]  # Extract the filename
    pdf_path = os.path.join(download_folder, pdf_name)  # Full path where PDF will be saved

    # Download PDF if not already cached
    if not os.path.exists(pdf_path):
        with request.urlopen(pdf_link) as response, open(pdf_path, "wb") as pdf_file:
            pdf_file.write(response.read())
        print(f"\n✅ Downloaded: {pdf_name} at {os.path.abspath(pdf_path)}")

    # Step 5: Extract Text from PDF
    with open(pdf_path, "rb") as f:
        pdf = pdftotext.PDF(f)

    # Step 6: Extract Statistics
    for line in "".join(pdf).split("\n"):
        if line.startswith("Reporting Period"):
            print(f"📄 {pdf_name} - {line}")
```





---

## **4️⃣ How to Run the Script**
### ✅ **Run the Script in the Terminal**
```bash
python script_name.py
```
✔️ The script will:
1. Scrape PDF links from **the webpage**.
2. **Download up to 5 PDFs** if not already downloaded.
3. **Extract text** from the PDFs.
4. **Print extracted statistics**.

---

## **5️⃣ Example Output**
```
✅ Downloaded: Statistical_Report_Beer_December_2021.pdf at E:\python\Scraping_data\Statistical_Report_Beer_December_2021.pdf
📄 Statistical_Report_Beer_December_2021.pdf - Reporting Period: December 2021

✅ Downloaded: Statistical_Report_Beer_November_2021.pdf at E:\python\Scraping_data\Statistical_Report_Beer_November_2021.pdf
📄 Statistical_Report_Beer_November_2021.pdf - Reporting Period: November 2021
```

---

## **6️⃣ Summary of Key Concepts**
| **Concept** | **Usage in the Script** | **Explanation** |
|-------------|------------------------|----------------|
| **`BeautifulSoup`** | `soup.find_all("a", href=True)` | Extracts all links (`<a>` tags) from HTML |
| **`urljoin()`** | `urljoin(base_url, link["href"])` | Converts relative URLs to absolute URLs |
| **`os.path.exists()`** | `if not os.path.exists(pdf_name)` | Checks if a file already exists |
| **`request.urlopen()`** | `request.urlopen(pdf_link).read()` | Downloads the PDF file |
| **`pdftotext.PDF()`** | `pdf = pdftotext.PDF(f)` | Converts a PDF into **text format** |
| **`split("\n")`** | `for line in "".join(pdf).split("\n")` | Splits text into **lines** |
| **`startswith()`** | `if line.startswith("Reporting Period")` | Finds lines that start with a specific keyword |

---

## **🚀 Final Thoughts**
✅ **Efficiently scrapes, downloads, and processes PDFs.**  
✅ **Uses `BeautifulSoup` for web scraping and `pdftotext` for text extraction.**  
✅ **Can be extended to extract more statistics!**  

Would you like **to save extracted data to a CSV file**? Let me know! 🚀😊


# **Advanced Web Scraping Tools**
| **Tool** | **Description** |
|----------|----------------|
| **Requests** | Easier HTTP client than `urllib` |
| **Scrapy** | Powerful web scraping framework |
| **Playwright** | Runs a full browser for complex scraping |
| **Common Crawl** | Public dataset of crawled websites |

---

# **📌 Summary**
✅ **Scraped PDF links from a webpage**  
✅ **Downloaded PDFs automatically**  
✅ **Extracted structured data**  
✅ **Stored and processed data efficiently**  

---
### **🚀 Next Steps**
📌 **Improve error handling**  
📌 **Store extracted data in a database**  
📌 **Use Scrapy or Playwright for more advanced scraping**  

---
**Conclusion:**  
This **web scraping exercise** demonstrates **real-world automation** techniques. It teaches how to **download files, extract data, and automate repetitive tasks**. This knowledge is essential for **data science, web automation, and testing applications**. 🚀
