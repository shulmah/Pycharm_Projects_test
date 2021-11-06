'''извлечем заголовки новостей с главной страницы журнала radio'''
import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.radio.ru/")
#response = requests.get("https://xakep.ru")
page = response.text

soup = BeautifulSoup(page, 'html.parser')
                                              # "span.news-d" "span.news-h" < in radio
headings = map(lambda e: e.text, soup.select("span.news-t")) #"h3.entry-title a span" <in xakep
for h in headings:
  print(h)
