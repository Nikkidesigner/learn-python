# **Scrapy Tutorial: Web Scraping with Scrapy**

## **Introduction to Scrapy**
Scrapy is a powerful and widely-used Python framework for web scraping. It allows developers to efficiently extract data from websites, follow links, and store scraped data in various formats. This tutorial will walk you through the entire process of using Scrapy to scrape data from `quotes.toscrape.com`.

### **Prerequisites**
Before starting, ensure Scrapy is installed on your system. If not, install it using:
```sh
pip install scrapy
```

## **1. Creating a Scrapy Project**
To begin scraping, set up a new Scrapy project. Open a terminal and run:
```sh
scrapy startproject tutorial
```
This creates the following directory structure:
```
tutorial/
    scrapy.cfg            # Configuration file
    tutorial/             # Project's Python module
        __init__.py
        items.py          # Defines data structures
        middlewares.py    # Custom middleware for Scrapy
        pipelines.py      # Data processing pipeline
        settings.py       # Configuration settings
        spiders/          # Stores spider scripts
            __init__.py
```

# **📌 Scrapy Project Folder Structure Breakdown**
When you create a Scrapy project using:
```bash
scrapy startproject tutorial
```
It generates the following structure:

```
tutorial/
    scrapy.cfg            # Configuration file
    tutorial/             # Project's Python module
        __init__.py
        items.py          # Defines data structures
        middlewares.py    # Custom middleware for Scrapy
        pipelines.py      # Data processing pipeline
        settings.py       # Configuration settings
        spiders/          # Stores spider scripts
            __init__.py
```

---

## **📌 Purpose of Each File**
### **🔹 1. `scrapy.cfg` (Project Configuration File)**
📌 **Purpose:**
- Global **configuration file** for the Scrapy project.
- Defines settings like **log levels, feed exports, and custom paths**.

📌 **Example Content:**
```ini
[settings]
default = tutorial.settings
```
✔️ Specifies that the **default settings file** is `tutorial/settings.py`.

---

### **🔹 2. `tutorial/` (Main Project Module)**
📌 **Purpose:**
- Contains all the **Scrapy components** (spiders, settings, pipelines, etc.).
- Serves as a **Python package** (`__init__.py` makes it importable).

---

### **🔹 3. `__init__.py` (Package Initialization)**
📌 **Purpose:**
- Marks `tutorial/` and `spiders/` as **Python packages**.
- Usually **empty**, but can contain package-wide configurations.

✔️ Without this file, **Python won't recognize the directory as a package**.

---

### **🔹 4. `items.py` (Defines Data Structures)**
📌 **Purpose:**
- Defines **structured data fields** that the scraper extracts.
- Works like a **database schema** for your scraped data.

📌 **Example `items.py`:**
```python
import scrapy

class ProductItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()
```
✔️ Helps organize scraped data in a **consistent format**.

---

### **🔹 5. `middlewares.py` (Custom Middleware for Scrapy)**
📌 **Purpose:**
- Contains **custom middlewares** to **process requests & responses**.
- You can modify **headers, handle captchas, or use proxies**.

📌 **Example Middleware:**
```python
from scrapy import signals

class CustomMiddleware:
    def process_request(self, request, spider):
        request.headers["User-Agent"] = "Mozilla/5.0"
        return None
```
✔️ Used for **rotating user agents, handling redirects, or injecting cookies**.

---

### **🔹 6. `pipelines.py` (Data Processing Pipeline)**
📌 **Purpose:**
- **Processes and cleans** scraped data before saving.
- Can **filter, modify, or store data in databases**.

📌 **Example `pipelines.py`:**
```python
class PricePipeline:
    def process_item(self, item, spider):
        item["price"] = float(item["price"].replace("$", ""))
        return item
```
✔️ **Data flows through pipelines** before being stored.

---

### **🔹 7. `settings.py` (Configuration Settings)**
📌 **Purpose:**
- Defines Scrapy **settings** like:
  - **User-Agent**
  - **Download delays**
  - **Concurrent requests**
  - **Pipeline activation**

📌 **Example `settings.py`:**
```python
BOT_NAME = "tutorial"
DOWNLOAD_DELAY = 2
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    "tutorial.pipelines.PricePipeline": 300,
}
```
✔️ Helps **control how Scrapy behaves**.

---

### **🔹 8. `spiders/` (Stores Spider Scripts)**
📌 **Purpose:**
- Contains **all web scraping scripts** (spiders).
- Each spider is a **Python class** that defines:
  - The **URL to scrape**.
  - The **data to extract**.

📌 **Example Spider (`spiders/example_spider.py`):**
```python
import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get()
            }
```
✔️ Scrapy automatically finds **all spiders inside this folder**.

---

### **🔹 9. `spiders/__init__.py`**
📌 **Purpose:**
- Marks `spiders/` as a **Python package**.
- Allows importing spiders from **other scripts**.

✔️ Usually **left empty**.

---

## **📌 Summary of Folder Structure**
| **File/Folder** | **Purpose** |
|----------------|------------|
| **`scrapy.cfg`** | Global Scrapy project configuration |
| **`tutorial/`** | Main project module |
| **`__init__.py`** | Marks directory as a Python package |
| **`items.py`** | Defines data structures (like database schema) |
| **`middlewares.py`** | Custom processing of requests & responses |
| **`pipelines.py`** | Cleans, processes, and saves scraped data |
| **`settings.py`** | Defines project settings (timeouts, delays, pipelines) |
| **`spiders/`** | Stores web scraping scripts (spiders) |
| **`spiders/__init__.py`** | Marks `spiders/` as a Python package |

✅ **Now you understand every part of a Scrapy project!** 🚀  




## **2. Writing a Spider**
A Scrapy **Spider** is a Python class that defines how a website should be scraped. Create a new file `quotes_spider.py` inside the `spiders/` directory and add the following code:

```python
import scrapy
from pathlib import Path

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
```

### **Understanding the Code**
- `name`: Identifies the spider uniquely within a project.
- `start_requests()`: Defines the starting URLs.
- `parse()`: Processes the response and extracts data.

## **3. Running the Spider**
Execute the spider using:
```sh
scrapy crawl quotes
```
This will create files `quotes-1.html` and `quotes-2.html`, containing the scraped pages.

## **4. Extracting Data with Scrapy Selectors**
Instead of saving HTML, we want to extract quotes and authors. We use **CSS Selectors** and **XPath** to extract elements.

Modify `parse()` in `quotes_spider.py`:

```python
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
```

### **Explanation**
- `quote.css("span.text::text").get()`: Extracts the quote text.
- `quote.css("small.author::text").get()`: Extracts the author.
- `quote.css("div.tags a.tag::text").getall()`: Extracts all tags.

Run the spider again:
```sh
scrapy crawl quotes -o quotes.json
```
This saves extracted data to `quotes.json`.

## **5. Recursively Following Links**
Modify the spider to follow pagination links and scrape all pages.

```python
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
        
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
```

## **6. Running Scrapy Shell**
Scrapy provides an interactive shell to test scraping commands. Run:
```sh
scrapy shell 'https://quotes.toscrape.com/page/1/'
```
Inside the shell, try:
```python
response.css("title::text").get()
response.css("div.quote span.text::text").getall()
```

## **7. Storing Data in Different Formats**
Scrapy allows exporting data in various formats:
```sh
scrapy crawl quotes -o quotes.json
scrapy crawl quotes -o quotes.csv
scrapy crawl quotes -o quotes.xml
```

## **8. Using Spider Arguments**
Scrapy allows passing arguments to spiders:
```sh
scrapy crawl quotes -a category=life
```
Modify `quotes_spider.py` to accept arguments:
```python
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def __init__(self, category=None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f"https://quotes.toscrape.com/tag/{category}/"]
```

## **9. Handling Middleware & Pipelines**
- **Middlewares** modify requests and responses.
- **Pipelines** process scraped data before storage.

Enable pipelines in `settings.py`:
```python
ITEM_PIPELINES = {
    'tutorial.pipelines.TutorialPipeline': 300,
}
```

Modify `pipelines.py`:
```python
class TutorialPipeline:
    def process_item(self, item, spider):
        item['text'] = item['text'].upper()  # Convert quotes to uppercase
        return item
```

## **10. Handling Robots.txt and User-Agent**
Some websites block scrapers. Modify `settings.py` to change headers:
```python
ROBOTSTXT_OBEY = False
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
```

## **11. Advanced Web Scraping with Scrapy**
- **Use Scrapy-Splash** for JavaScript-rendered pages.
- **Use Scrapy-Playwright** for handling dynamic content.
- **Integrate Proxies & User Agents** to avoid IP bans.
- **Deploy Scrapy Spiders** using `scrapy crawl quotes -s JOBDIR=crawls/quotes`.

## **Conclusion**
Scrapy is a powerful tool for web scraping, capable of handling simple and complex scraping tasks. By mastering **spiders, data extraction, following links, handling errors, and exporting data**, you can build efficient and scalable web scrapers.

🚀 **Next Steps:**
- Try scraping different websites.
- Explore Scrapy middlewares and advanced settings.
- Deploy Scrapy spiders to run automatically.

Happy Scraping! 🎯

# **Scrapy Spiders: A Detailed Guide**

## **Introduction to Scrapy Spiders**
Scrapy is a powerful Python framework for web scraping, and **Spiders** are the core components of Scrapy projects. Spiders define how a particular site (or a group of sites) will be scraped, including how to crawl (follow links) and extract structured data from web pages.

This guide covers:
- Understanding **Scrapy Spiders** and their lifecycle
- Key attributes and methods of spiders
- Implementing a basic spider
- Exploring advanced spider types like `CrawlSpider`

---

## **1. What is a Scrapy Spider?**
A **Scrapy Spider** is a Python class that defines how Scrapy should navigate and extract data from websites. It does this by:
- Sending initial requests to crawl URLs
- Parsing the responses (HTML pages) using Scrapy selectors
- Extracting data into structured formats like JSON, CSV, or databases
- Following links to navigate the site recursively

Spiders must inherit from the `scrapy.Spider` base class and define their behavior through attributes and methods.

---

## **2. Scrapy Spider Lifecycle**
A Scrapy Spider goes through the following steps:
1. **Generate Initial Requests**: The `start_requests()` method sends requests to the URLs in `start_urls`.
2. **Receive Response**: Scrapy processes the downloaded pages and sends responses to the callback function.
3. **Parse the Page**: The `parse()` method extracts data and identifies new URLs to follow.
4. **Follow Links**: New requests are generated based on extracted links, and the cycle repeats.
5. **Store Data**: Extracted data is saved in a structured format or a database.

---

## **3. Key Attributes of Scrapy Spiders**
Scrapy Spiders have several important attributes that control their behavior:

### **a) `name` (Required)**
Each spider must have a unique `name` that identifies it within the Scrapy project.
```python
class MySpider(scrapy.Spider):
    name = "quotes"
```

### **b) `allowed_domains` (Optional)**
A list of domains the spider is allowed to crawl. Scrapy won’t follow links outside these domains.
```python
allowed_domains = ["example.com"]
```

### **c) `start_urls` (Optional)**
A list of URLs from which the spider starts scraping.
```python
start_urls = ["https://quotes.toscrape.com/page/1/"]
```

### **d) `custom_settings` (Optional)**
A dictionary to override project-wide settings for this spider.
```python
custom_settings = {
    "ROBOTSTXT_OBEY": False,
    "DOWNLOAD_DELAY": 1
}
```

---

## **4. Creating a Basic Spider**
Let's create a simple spider to scrape quotes from `quotes.toscrape.com`.

### **Step 1: Set Up a Scrapy Project**
Run the following command to create a Scrapy project:
```bash
scrapy startproject tutorial
cd tutorial
```

### **Step 2: Create a Spider File**
Create a new file `quotes_spider.py` inside the `spiders/` directory:

```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        for quote in response.css(".quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
            }
```

### **Step 3: Run the Spider**
Execute the following command to run the spider:
```bash
scrapy crawl quotes -o quotes.json
```
This will extract quotes and save them in a JSON file.

---

## **5. Understanding the `parse()` Method**
The `parse()` method is the default callback for processing responses. It extracts data using **CSS Selectors** or **XPath**.

### **CSS Selectors Example**
```python
response.css("title::text").get()
```

### **XPath Example**
```python
response.xpath("//title/text()").get()
```

---

## **6. Advanced Spiders: CrawlSpider**
Scrapy provides generic spiders like `CrawlSpider` to automatically follow links based on defined rules.

### **Example: CrawlSpider for Crawling Links**
```python
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MyCrawlSpider(CrawlSpider):
    name = "crawl_quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow=r'/page/'), callback='parse_quotes', follow=True),
    )

    def parse_quotes(self, response):
        for quote in response.css(".quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
            }
```

This spider:
- Starts from `start_urls`
- Follows pagination links matching `/page/`
- Extracts quotes from each page

Run it using:
```bash
scrapy crawl crawl_quotes -o quotes.json
```

---

## **7. Using Spider Arguments**
Spiders can accept arguments using the `-a` flag.
```bash
scrapy crawl quotes -a category=humor
```
Inside the spider, access the argument using `self.category`:
```python
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def __init__(self, category=None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f"https://quotes.toscrape.com/tag/{category}"]
```

---

## **8. Logging and Debugging**
Scrapy provides logging methods to help debug spiders:
```python
self.logger.info("Processing page: %s", response.url)
```
To enable **detailed debugging**, run Scrapy with the `--loglevel` flag:
```bash
scrapy crawl quotes --loglevel=DEBUG
```

---

## **9. Conclusion**
Scrapy Spiders are powerful tools for web scraping, offering:
✅ Efficient crawling and link-following capabilities
✅ Flexible parsing using **CSS Selectors** and **XPath**
✅ Automatic handling of pagination with `CrawlSpider`
✅ Customizable behavior with `custom_settings` and arguments

This guide provides a strong foundation to create and optimize Scrapy spiders for various web scraping tasks. 🚀

For further learning, check out:
- **Scrapy Documentation**: https://docs.scrapy.org/en/latest/
- **Web Scraping Best Practices**
- **Handling AJAX and Dynamic Content in Scrapy**

Happy Scraping! 🕷️



