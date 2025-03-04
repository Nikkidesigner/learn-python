import os
import pdftotext
from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # ✅ Helps convert relative URLs to absolute



# Step 1: Scrape Web Page
base_url = "https://learncodethehardway.com/setup/python/ttb/"
response = request.urlopen(base_url)
soup = BeautifulSoup(response, "html5lib")

# Step 2: Extract PDF Links
pdf_links = [urljoin(base_url, link["href"]) for link in soup.find_all("a", href=True) if link["href"].endswith(".pdf")]

# Step 3: Download and Process PDFs
for pdf_link in pdf_links[:5]:  # Limit to 5 PDFs
    pdf_name = pdf_link.split("/")[-1]

    # Download PDF if not already cached
    if not os.path.exists(pdf_name):
        save_path = os.path.abspath(pdf_name)
        with request.urlopen(pdf_link) as response, open(pdf_name, "wb") as pdf_file:
            pdf_file.write(response.read())
        print(f"\n \n ✅ Downloaded: {pdf_name} at {save_path}")


    # Step 4: Extract Text from PDF
    with open(pdf_name, "rb") as f:
        pdf = pdftotext.PDF(f)

    # Step 5: Extract Statistics
    for line in "".join(pdf).split("\n"):
        if line.startswith("Reporting Period"):
            print(f"📄 {pdf_name} - {line}")
