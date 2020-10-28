import requests
from bs4 import BeautifulSoup

HOST = 'https://www.irk.ru/'
URL = 'https://www.irk.ru/covid'
HEADERS = {
    'user-agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'accept': '*/*'
}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    global date_news
    date_news = soup.find('div', class_='ucard').find('div', class_='ucard__date').get_text()
    global title_news
    title_news = soup.find('div', class_='ucard').find('h2', class_='ucard__title').get_text()
    global content_news
    content_news = soup.find('div', class_='ucard').find('div', class_='ucard__content').get_text()
    global irk_infected
    irk_infected = soup.find('div', class_='aside__content__slide j-aside-slide').find('div').find('span').get_text()


def start_parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("ERROR")


start_parse()
