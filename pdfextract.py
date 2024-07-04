import os
import pypdf
import pyttsx4
from pypdf import PdfReader

#review: https://pypi.org/project/pyttsx4/
#review: https://pypi.org/project/PyPDF4/


text = ""

# Get the PDF file path from the user
pdf_file = input("Enter the path to the PDF file: ")

# Open the PDF file
with open(pdf_file, 'rb') as file:
    # Create a PDF reader object

    # Loop through each page and extract the text
    reader = pypdf.PdfReader(file)
    for page in reader.pages:
        text += page.extract_text()

print(text)
