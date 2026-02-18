from pypdf import PdfReader
from nltk.tokenize import sent_tokenize
import nltk


nltk.download('punkt_tab')



reader = PdfReader("src/pdf_reader/01.pdf")
pages_list = []



def text_refactor(txt: str) -> str:

    cleaned_text = txt.replace("\n", " ").strip()

    return cleaned_text


for i in range(len(reader.pages)):
    

    pages_dict = {}
    page = reader.pages[i]
    pages_dict["Page_number"] = i
    text = page.extract_text()
    text = text_refactor(text)
    sentences = sent_tokenize(text)
    pages_dict["text_tokenized"] = sentences
    pages_list.append(pages_dict)


print(pages_list)


