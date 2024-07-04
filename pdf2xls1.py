import tabula

def pdf_to_excel(pdf_file_path, excel_file_path):
  """
  Converts a PDF file to an XLSX file.

  Args:
      pdf_file_path (str): Path to the PDF file.
      excel_file_path (str): Path to the output XLSX file.
  """
  # Read the PDF file and extract tables as a list of DataFrames
  tables = tabula.read_pdf(pdf_file_path, multiple_tables=True)

  # Create an Excel writer object
  writer = pd.ExcelWriter(excel_file_path, engine='xlsxwriter')

  # Write each DataFrame to a separate sheet in the Excel file
  for i, table in enumerate(tables):
      table.to_excel(writer, sheet_name=f'Sheet{i+1}')

  # Save the Excel file
  writer.save()

# Example usage
pdf_file_path = "your_pdf_file.pdf"
excel_file_path = "output.xlsx"
pdf_to_excel(pdf_file_path, excel_file_path)

print(f"PDF converted to Excel and saved as: {excel_file_path}")
