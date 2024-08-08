import PyPDF2
import os

def combine_pdfs(pdf_list, output):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_list:
        try:
            pdf_reader = PyPDF2.PdfReader(pdf)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
        except PyPDF2.errors.PdfReadError:
            print(f"Could not read {pdf}, skipping.")

    with open(output, 'wb') as out_file:
        pdf_writer.write(out_file)

def get_pdf_files(folder):
    pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]
    pdf_files = [os.path.join(folder, f) for f in pdf_files]  # Include full path
    return pdf_files

folder_path = 'path/to/your/folder'  # Replace with the path to your folder
pdf_files = get_pdf_files(folder_path)
combine_pdfs(pdf_files, 'combined.pdf')