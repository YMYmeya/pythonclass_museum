import requests
import bs4

html = requests.get("http://fx.sjtulib.superlib.net/s?sw=python").text
print(html)
soup = bs4.BeautifulSoup(html, 'lxml')
title = soup.find('title')
print(title)
