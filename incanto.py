import requests
from bs4 import BeautifulSoup as bs
# import pandas as pd
URL_TEMPLATE = "https://incanto.eu/catalog/byustgaltery_i_trusy/byustgaltery_bez_kostochek/byustgalter_s_treugolnymi_formovannymi_chashkami_bez_kostochek_na_peremychke_angelica/"
# URL_TEMPLATE = 'https://incanto.eu/catalog/byustgaltery_i_trusy/byustgaltery_push_up/byustgalter_push_up_s_formovannymi_chashkami_na_stane_sebbin/?option=4186180756'
 
allprice = []
discount = []

def parse(url=URL_TEMPLATE):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.2.612 Yowser/2.5 Safari/537.36'}
    r = requests.get(url, headers=headers)
#     print(r.status_code)
#     print(r.text)

    soup = bs(r.text, "html.parser")
#     allprice = soup.findAll(' ')
#     vacancies_names = soup.find_all('div', class_='price price--composite')
#     vacancies_info = soup.find_all('p', class_='overflow')
#     print(soup)
#     for name in vacancies_names:
#         print(name)
    q = str(soup)
    txt = '''<script>window.ad_product={"id":"130932","vendor":"Incanto","price":"3299.00","url":"/catalog/byustgaltery_i_trusy/byustgaltery_bez_kostochek/byustgalter_s_treugolnymi_formovannymi_chashkami_bez_kostochek_na_peremychke_angelica/'''
    
    if txt in q:
        print('прежняя цена')
        
    
    
#     print(q)
#         
#     n = soup.find_all(txt)
#     
#     q = '''<div class="price price--composite">
# <s>4699<span>q</span></s>
# 3289<span>q</span>
# </div>'''
# #     
#     print(n)
#     print(q)
#     
#     print(str(n) == q)
    
# #     print(n)
#     print(n)
#     for i in n:
#         print(i, 'qwerty')        
# #         result_list['href'].append('https://www.work.ua'+name.a['href'])
# #         result_list['title'].append(name.a['title'])
# #     for info in vacancies_info:
#         result_list['about'].append(info.text)
#     return result_list
#     print(allprice)

parse()
