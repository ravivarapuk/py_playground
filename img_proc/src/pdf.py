import PyPDF2

with open('dummy.pdf', 'rb') as file:
    print(file)
    reader = PyPDF2.PdfFileReader(file)


template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output = PyPDF2.PdfFileWriter()

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)