import  PyPDF2


pdfiles=["1.pdf","2.pdf"]
merger = PyPDF2.PdfWriter()

for filename in pdfiles:
    pdfile=open(filename,'rb')
    pdfReader=PyPDF2.PdfReader(pdfile)
    merger.append(pdfReader)
pdfile.close()
merger.write('merged.pdf')
