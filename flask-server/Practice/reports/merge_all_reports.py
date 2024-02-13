import os
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(input_folder, output_file):
    pdf_writer = PdfWriter()

    # Iterate through all PDFs in the input folder
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                pdf_reader = PdfReader(pdf_path)
                
                # Add all pages to the writer
                for page_num in range(len(pdf_reader.pages)):
                    pdf_writer.add_page(pdf_reader.pages[page_num])

    # Write the combined PDF to the output file
    with open(output_file, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

# Specify the input folder containing your PDFs and the output file

