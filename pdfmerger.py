import PyPDF2
import os
import sys

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger=PyPDF2.PdfFileMerger()
        merger.append(file)
    merger.write("merged.pdf")