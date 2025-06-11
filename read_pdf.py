import PyPDF2

def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Ошибка при чтении PDF: {e}")
        return None

if __name__ == "__main__":
    pdf_path = "Frontend_kehittaja_Vladimir_Piniazhin_CV.pdf"
    content = read_pdf(pdf_path)
    if content:
        print(content) 