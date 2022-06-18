import requests
from bs4 import BeautifulSoup as bs
import telebot
import time

URL_TEMPLATE = "https://incanto.eu/catalog/byustgaltery_i_trusy/byustgaltery_bez_kostochek/byustgalter_s_treugolnymi_formovannymi_chashkami_bez_kostochek_na_peremychke_angelica/"
# URL_TEMPLATE = 'https://incanto.eu/catalog/byustgaltery_i_trusy/byustgaltery_push_up/byustgalter_push_up_s_formovannymi_chashkami_na_stane_sebbin/?option=4186180756'
bot = telebot.TeleBot ( "НОМЕР БОТА" )
 
def parse(url=URL_TEMPLATE):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.2.612 Yowser/2.5 Safari/537.36'}
    r = requests.get(url, headers=headers)

    soup = bs(r.text, "html.parser")

    q = str(soup)
    txt = '''<script>window.ad_product={"id":"130932","vendor":"Incanto","price":"3299.00","url":"/catalog/byustgaltery_i_trusy/byustgaltery_bez_kostochek/byustgalter_s_treugolnymi_formovannymi_chashkami_bez_kostochek_na_peremychke_angelica/'''
    
    if txt in q:
        bot.send_message('250690401', 'Цена не изменилась, Динуля, отбой по покупкам трусиков')
        print('прежняя цена')
    else:
        bot.send_message('250690401', 'Цена изменидась на сайте Incanto, нужно проверить')
        print('новая цена на сайте')

while True:
    time.sleep(7200)
    parse()
