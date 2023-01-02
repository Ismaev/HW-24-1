from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL = "https://animevost.org/zhanr/romantika/"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}


def get_html(url):
    req = requests.get(url=url, headers=HEADERS)
    return req

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="shortstory")
    anime = []
    for item in items:
        info = item.find('div', class_='shortstoryContent').find('p')
        card = {
            'title': item.find('div', class_='shortstoryContent').find('h4'),
            'link': item.find('div', class_='shoortstoryFuter').find('a').get('href'),
            'date': info[0],
            'genre': info[1],
            'type': info[2],
            'series': info[3],
        }
        anime.append(card)
    return anime


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f"{URL}page/{i}/")
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Bad request!")