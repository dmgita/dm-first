import requests
# from bs4 import BeautifulSoup as bs
# import pandas as pd
URL_TEMPLATE = "https://incanto.eu/catalog/byustgaltery_i_trusy/"

def parse(url=URL_TEMPLATE):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.2.612 Yowser/2.5 Safari/537.36'}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.text)

#     soup = bs(r.text, "html.parser")
#     vacancies_names = soup.find_all('h2', class_='add-bottom-sm')
#     vacancies_info = soup.find_all('p', class_='overflow')
#     for name in vacancies_names:
#         result_list['href'].append('https://www.work.ua'+name.a['href'])
#         result_list['title'].append(name.a['title'])
#     for info in vacancies_info:
#         result_list['about'].append(info.text)
#     return result_list

parse()
