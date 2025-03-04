import pdftotext
import sys
import re  # Import regex module

# Ensure a file argument is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <pdf_file>")
    sys.exit(1)

pdf_file = sys.argv[1]

try:
    # Open the PDF
    with open(pdf_file, "rb") as infile:
        pdf = pdftotext.PDF(infile)

    # Convert PDF pages into text
    text = "\n".join(pdf)  # Combine all text into a single string

    # Extract reporting period and report date
    reporting_period = re.search(r"Reporting Period:\s*([A-Za-z]+\s\d{4})", text)
    report_date = re.search(r"Report Date:\s*([\dA-Z]+)", text)

    # Extract production and stock values (new regex to handle format in PDF)
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
    print(f"Reporting Period: {reporting_period}")
    print(f"Reporting Date: {report_date}")
    print(f"Production (Current Month): {production_current_month}")
    print(f"Stocks on Hand End of Month: {stock_current_month}")
    print(f"Sales (Production - Stocks): {sales}")

except FileNotFoundError:
    print(f"Error: The file '{pdf_file}' was not found.")
except pdftotext.Error as e:
    print(f"Error processing PDF: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
