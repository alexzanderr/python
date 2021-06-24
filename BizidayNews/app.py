
import requests
from bs4 import BeautifulSoup
from core.aesthetics import *
import logging
from core.romania import remove_diacritics

file_handler = logging.FileHandler("biziday_news.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("[%(asctime)s] - [%(name)s] - [%(levelname)s] - [\n%(message)s\n]\n"))

file_logger = logging.getLogger("biziday - news")
file_logger.setLevel(logging.INFO)
file_logger.addHandler(file_handler)


biziday_ro = "https://www.biziday.ro/"
response = requests.get(biziday_ro)
# print(response.status_code)
# print(response.text)

sp = BeautifulSoup(response.text, "html.parser")
elems = sp.findAll("li", {
    "class": "article"
})


class Article:
    def __init__(self, content: str, url):
        self.content = content
        self.content = remove_diacritics(self.content)

        self.content_formatted = self.content
        for i in range(len(self.content)):
            if i % 60 == 0:
                self.content_formatted = self.content_formatted[:i] + "\n" + self.content_formatted[i:]
        self.url = url


articles = []
for article in elems:
    a = article.findNext() # web element child
    if a.has_attr("title") and a.has_attr("href"):
        content = a["title"].strip()
        url = a["href"].strip()
        articles.append(Article(content, url))



print("Biziday News")
print("=" * 50 + "\n")
for index, ar in enumerate(articles, start=1):
    file_logger.info(ar.content)
    print(f"[ {index} ]")
    print(yellow(ar.content_formatted))
    print(blue(ar.url))
    print("\n")
print("Total contents: {}".format(len(elems)))