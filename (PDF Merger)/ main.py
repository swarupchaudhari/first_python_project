from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []

n = int(input("How many PDFs do you want to merge? : "))

for i in range(n):
    name = input(f"Enter the name of PDF {i + 1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

print(" PDFs merged successfully into merged-pdf.pdf")