import requests
from bs4 import BeautifulSoup
import telebot
import lxml
import time

bot = telebot.TeleBot('Token')
# forecaset
chat_id = 'group_id'
admin_id = 'You_id'


# emoji
# 🔴 red circle
# 🟠 orange circle
# 🟢 green circle
# 🔵 blue circle

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
}



def list_pars(soup):
    for a in soup.find_all('a', href=True, class_="not-link single-announce-container"):

        try:
            response1 = requests.get("https://stavkiprognozy.ru" + a['href'], headers=headers, params=None)
            soup1 = BeautifulSoup(response1.text, 'lxml')
        except:
            bot.send_message(chat_id=admin_id, text=str('🚨 <b>Error: 0</b> 🚨 '), parse_mode='HTML')

        try:
            for ss in soup1.find_all('li', class_='breadcrumb-item'):
                sport = ss.find('span', itemprop='name').text
                if(sport != 'Главная'):
                    if(sport != 'Прогнозы'):
                        # print(sport)
                        break
        except:
            bot.send_message(chat_id=admin_id, text=str('🚨 <b>Error: 1</b> 🚨 '), parse_mode='HTML')

        try:
            game = soup1.find('span', class_='sinfor-main-panel-champ-text').text.replace(". ", " ")
            # print(game)
        except:
            bot.send_message(chat_id=admin_id, text=str('🚨 <b>Error: 2</b> 🚨 '), parse_mode='HTML')

        try:
            players = soup1.find('div', class_='sinfor-main-panel-body-title')
            span1 = players.find('span', itemprop='homeTeam')
            span2 = players.find('span', itemprop='awayTeam')
            player = span1.find('span', itemprop='name').text + ' - ' + span2.find('span', itemprop='name').text
            # print(player)
        except:
            bot.send_message(chat_id=admin_id, text=str('🚨 <b>Error: 3</b> 🚨 '), parse_mode='HTML')

        try:
            date = soup1.find('time', class_='time-item sinfor-main-panel-time-item').text.replace("                        ", " ")
            # print(date)
        except:
            bot.send_message(chat_id=admin_id, text=str('🚨 <b>Error: 4</b> 🚨 '), parse_mode='HTML')

        try:
            text1 = soup1.find('div', class_='box-item-content sinfor-properties-content').text
            texts = text1[1: -1]
            # print(texts)
        except:
            bot.send_message(chat_id=admin_id, text=str('🚨 <b>Error: 5</b> 🚨 '), parse_mode='HTML')

        try:
            win = "Прогноз: " + soup1.find('div', class_='list-info-strong list-info-prop').text
            # print(win)
        except:
            print("bot_4")
            bot.send_message(chat_id=admin_id, text=str('🚨 <b>Error: 6</b> 🚨 '), parse_mode='HTML')

        try:
            message = '❗ ' + '<b>' + str(player) + '</b>' + "\n" +' ('+str(game) +')' + "\n" + "\n" + '📅 ' + str(date) + "\n" + "\n" + '📌 ' + str(texts) + "\n" + "\n" + '📈 ' + '<b>' + str(win) + '</b>' + "\n" + "\n" + '#'+str(sport)
            bot.send_message(chat_id=chat_id, text=message, parse_mode='HTML')
        except:
            bot.send_message(chat_id=admin_id, text=str('🚨 <b>Error: 7</b> 🚨 '), parse_mode='HTML')

        time.sleep(3600)

def parser(url):
    html = requests.get(url, headers=headers,params=None)
    soup = BeautifulSoup(html.text, 'lxml')

    if html.status_code == 200:
        list_pars(soup)
    else:
        bot.send_message(chat_id=admin_id, text=str('🚨 <b>Нет ответа</b> 🚨 '), parse_mode='HTML')


if __name__ == "__main__":
    parser('https://stavkiprognozy.ru/prognozy/page_1/')
    parser('https://stavkiprognozy.ru/prognozy/page_2/')
    bot.send_message(chat_id=admin_id, text=str('🚨 <b>Reset</b> 🚨 '), parse_mode='HTML')


