from wsgiref import headers

import requests
import bs4

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}
response = requests.get('https://habr.com/')
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    title = article.find_all('h2')
    hubs = article.find_all('a', class_="tm-article-snippet__hubs-item-link")
    hubes = set([hub.find('span').text for hub in hubs])
    if KEYWORDS & hubes:
        tages =title.find('a')
        tages_href = tages.attrs['href']
        times = title.find('time', id='datetime')
        url = 'https://habr.com/' + tages_href
        print(title.text, url , times)
        print(hubes)
        print('--------------------------------------------------')




