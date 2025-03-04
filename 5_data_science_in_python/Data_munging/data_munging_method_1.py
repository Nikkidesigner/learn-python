import pdftotext
import re

# This script extracts beer production statistics from a PDF file.
# It retrieves:
# - Reporting period
# - Report date
# - Production and stock levels
# - Sales data


# Step 1: Install and import necessary libraries
# Step 2: Open and read the PDF file
# Step 3: Extract text content
# Step 4: Identify relevant data using regex
# Step 5: Convert extracted data into numerical format
# Step 6: Calculate sales as Production - Stock on Hand
# Step 7: Print the results


# Open the PDF file
with open("beer_statistics.pdf", "rb") as file:
    pdf = pdftotext.PDF(file)

# Convert PDF pages into a single text string
pdf_text = "\n".join(pdf)

# Print extracted text
# print(pdf_text)




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
