import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_html(url, headers):
    r = requests.get(url, headers=headers)
    return r.content


def rate_doll(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        doll = soup.find('div', class_='chart__info__row js-ticker').find('span', class_='chart__info__sum').text
    except:
        doll = 'Rate of dollar not found'


def rate_euro(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        euro = soup.find('div', class_='chart__info__row js-ticker').find('span', class_='chart__info__sum').text
    except:
        euro = 'Rate of euro not found'


def main():
    doll_url = 'https://quote.rbc.ru/ticker/59111'
    euro_url = 'https://quote.rbc.ru/ticker/59090'
    user = UserAgent()
    headers = {'User-Agent': user.chrome}
    html_doll = get_html(doll_url, headers)
    html_euro = get_html(euro_url, headers)
    doll_rate = rate_doll(html_doll)
    euro_rate = rate_euro(html_euro)


if __name__ == '__main__':
    main()