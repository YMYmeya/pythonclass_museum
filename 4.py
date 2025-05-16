import requests
import bs4

html = requests.get("http://fx.sjtulib.superlib.net/s?sw=python").text
soup = bs4.BeautifulSoup(html, 'lxml')
ps = soup.find_all('p', class_='hitsNum')
print(ps)
for p in ps:
    print(p.text)