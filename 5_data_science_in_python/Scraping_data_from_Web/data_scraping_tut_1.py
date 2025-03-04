from bs4 import BeautifulSoup
from urllib import request

# Download the web page
url = "https://learncodethehardway.com/setup/python/ttb/"
response = request.urlopen(url)
html = response.read()

# Parse the HTML
soup = BeautifulSoup(html, "html5lib")
print(soup.title.text)  # Print the page title
