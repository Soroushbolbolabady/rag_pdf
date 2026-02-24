from pypdf import PdfReader
from nltk.tokenize import sent_tokenize
import nltk


nltk.download('punkt_tab')


pdf_path = "src/pdf_reader/01.pdf"
pdf2_path = "src/pdf_reader/02.pdf"





def text_refactor(txt: str) -> str:

    cleaned_text = txt.replace("\n", " ").strip()

    return cleaned_text



def tokenize_pdf(pdf_path : str) -> list[dict]:

    reader = PdfReader(pdf_path)
    
    pages_list = []
    
    for i in range(len(reader.pages)):
        page_dict = {}
        page = reader.pages[i]
        page_dict["page_number"] = page.page_number
        text = page.extract_text()
        text = text_refactor(text)
        page_dict["page_text"] = text
        sentences = sent_tokenize(text)
        page_dict["page_text_tokenized"] = sentences
        page_dict["token_count"] = len(text) / 4
        pages_list.append(page_dict)
    
    return pages_list


