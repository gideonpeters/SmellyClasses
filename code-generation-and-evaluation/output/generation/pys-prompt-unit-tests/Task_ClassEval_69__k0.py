import os
from PyPDF2 import PdfFileReader
from reportlab.pdfgen import canvas


class PDFHandler:
    def __init__(self, pdf_files):
        self.pdf_files = pdf_files

    def merge_pdfs(self, output_filename):
        merger = PdfFileMerger()
        for pdf_file in self.pdf_files:
            merger.append(pdf_file)
        merger.write(output_filename)
        merger.close()
        return f"Merged PDFs saved at {output_filename}"

    def extract_text_from_pdfs(self):
        extracted_text = []
        for pdf_file in self.pdf_files:
            with open(pdf_file, "rb") as file:
                pdf = PdfFileReader(file)
                text = ""
                for page_num in range(pdf.getNumPages()):
                    page = pdf.getPage(page_num)
                    text += page.extract_text()
                extracted_text.append(text)
        return extracted_text
