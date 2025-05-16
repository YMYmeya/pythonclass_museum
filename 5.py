import requests
import bs4

html = requests.get("http://fx.sjtulib.superlib.net/s?sw=python").text
soup = bs4.BeautifulSoup(html, 'lxml')
mainList = soup.find('div', id='mainlist')
zylists = mainList.find_all('div', class_='fr zyList_right')
for zylist in zylists:
    book_name = zylist.find('a').text
    lis = zylist.find_all('span', class_='fl col9')
    divs = zylist.find_all('div', class_='fl zylist_font')
    print(book_name.replace(' ', '').replace('\r\n', ''))
    for i in range(len(divs)):
        print(lis[i].text, divs[i].text)