!pip install PyPDF2

import PyPDF2
from google.colab import files

uploaded = files.upload()  # Upload 2 or more PDF files here

def merge_pdfs(pdf_list, output_filename):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_filename)
    merger.close()
    print(f"Merged PDF saved as: {output_filename}")

# Merge uploaded files
pdf_filenames = list(uploaded.keys())
merge_pdfs(pdf_filenames, "merged_output.pdf")
