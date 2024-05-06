from pypdf import PdfReader
import pyttsx3


book = open("read.pdf", "rb")
reader = PdfReader(book)
pages = reader.get_num_pages()
speaker = pyttsx3.init()
for num in range(0,pages):
    page = reader.pages[0]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()