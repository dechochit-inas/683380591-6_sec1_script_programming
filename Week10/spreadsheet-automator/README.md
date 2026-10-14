# Week 10: Automating Spreadsheets (Excel & Google Sheets)

This project demonstrates how to automate Microsoft Excel
(.xlsx) files using Python and the openpyxl library.

## Key Concepts Demonstrated

- Reading and writing Excel files using openpyxl
- Workbook and Worksheet Management
- Cell Manipulation
- Sales Data Processing
- Basic Formatting
- Column Width Adjustment

## Project Structure

spreadsheet-automator/
├── src/
│   ├── __init__.py
│   ├── excel_processor.py
│   └── data_models.py (Optional)
├── data/
│   ├── input_sales.xlsx
│   └── output_sales_report.xlsx
├── main.py
├── .gitignore
└── README.md

## Installation

Install the required library:

    python -m pip install openpyxl

## Input Data

Create an Excel file named input_sales.xlsx
inside the data folder.

The file must contain these columns:

| Product Name | Quantity | Unit Price |
|--------------|----------|------------|
| Laptop       | 2        | 1200.50    |
| Mouse        | 5        | 25.00      |
| Keyboard     | 3        | 75.99      |
| Monitor      | 1        | 300.00     |
| Printer      | 1        | 150.00     |

## How to Run

Run the following command:

    python main.py

## Expected Output

The program generates:

    data/output_sales_report.xlsx

The report includes:

- Product Name
- Quantity
- Unit Price
- Total Price
- Grand Total

## Error Handling

- Handles missing input files
- Skips empty rows
- Skips invalid numeric values
- Reports workbook loading and saving errors

## Ethical Notes

- Use only authorized spreadsheet data.
- Avoid exposing sensitive information.
- Validate data before processing.
