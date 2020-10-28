import requests
from bs4 import BeautifulSoup

URL = 'https://www.irk.ru/weather/'
HEADERS = {
    'user-agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'accept': '*/*'
}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    global temperature
    temperature = soup.find('div', class_='b-weather-main-current-info').\
        find('div', class_='b-weather-main-current').\
        find('span', class_='b-weather-main-current-degree').get_text().strip()

    global wind
    wind = soup.find('div', class_='b-weather-main-current-info').\
        find('div', class_='b-weather-main-current').\
        find('div', class_='b-weather-main-current-wind').get_text().strip()

    global humidity
    humidity = soup.find('div', class_='b-weather-main-current-info').\
        find('ul', class_='b-weather-main-current-properties').\
        find('li').find('p').get_text().strip()


def start_parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("ERROR")


start_parse()