import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_html(url, headers):
    r = requests.get(url, headers=headers)
    return r.content


def rate_doll(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        doll = soup.find('div', class_='chart__info__row js-ticker').find('span', class_='chart__info__sum')

    except:
        doll = 'Rate of dollar not found'

    return doll.text

def rate_euro(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        euro = soup.find('div', class_='chart__info__row js-ticker').find('span', class_='chart__info__sum')
    except:
        euro = 'Rate of euro not found'

    return euro.text


def send_result(bot_tocken, chatID, message):
    url = f'https://api.telegram.org/bot{bot_tocken}/sendMessage?chat_id={chatID}&text={message}'
    response = requests.get(url)
    return response.json()


def main():
    doll_url = 'https://quote.rbc.ru/ticker/59111'
    euro_url = 'https://quote.rbc.ru/ticker/59090'
    user = UserAgent()
    headers = {'User-Agent': user.chrome}
    html_doll = get_html(doll_url, headers)
    html_euro = get_html(euro_url, headers)
    doll_rate = rate_doll(html_doll)
    euro_rate = rate_euro(html_euro)
    bot_token = '1757768498:AAH1sMha-FvYmelOMJcN2lwYEsVRsbTdUK4'
    chatID = '1156779262'


    bot = send_result(bot_token, chatID, f'Курс доллара = {doll_rate}\nКурс евро = {euro_rate}')


if __name__ == '__main__':
    main()