import PyPDF2
import os


merger = PyPDF2.PdfWriter()
resourcesDir = os.curdir + "/resources"
print(f"Working directory: {resourcesDir}")
for file in os.listdir(resourcesDir):
    if file.endswith(".pdf"):
        absfile = os.path.join(resourcesDir, file)
        merger.append(absfile)
merger.write("resources/combinedPdf.pdf")
merger.close()

