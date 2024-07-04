from spire.pdf.common import *
from spire.pdf import *

# Create a PdfDocument object
pdf = PdfDocument()

# Load the PDF file
pdf.LoadFromFile("input.pdf")

# Save the PDF file to an Excel XLSX format
pdf.SaveToFile("output.xlsx", FileFormat.XLSX)

# Close the PdfDocument object
pdf.Close()
