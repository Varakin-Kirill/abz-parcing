import ebooklib
from ebooklib import epub
import requests
from bs4 import BeautifulSoup

book = epub.read_epub('C:\\Users\\kiril\\.vscode\\ProjectTemplates\\Новая папка\\pg72112-images-3.epub')
for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        Content=item.get_content().decode()
        soup=BeautifulSoup(Content, features="lxml")
        Text=soup.get_text()
        with open("text.txt", 'a', encoding='utf-8') as F:
            F.write(Text)