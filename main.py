import os
import json
import requests
from bs4 import BeautifulSoup
from random import randrange
import time


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
          'application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 '
                 'Safari/537.36'
}

url = f'https://tengrinews.kz/news/'
page = requests.get(url)
print('pageStatus:', page.status_code)
soup = BeautifulSoup(page.text, "html.parser")


'''
Достаем количество страниц пагинации
'''

# pagination_count = int(soup.find('ul', class_='pagination').find_all('a')[-2].text)
# print(pagination_count)

#
# articles_urls_list = list()
#
# pagination_count = 10
# for page in range(1, pagination_count+1):
#
#     response = requests.get(url=f'https://tengrinews.kz/news/page/{page}/', headers=headers)
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     articles_urls = soup.find_all(class_='content_main_item_title')
#     for au in articles_urls:
#         art_url = au.find('a').get('href')
#         articles_urls_list.append(f'https://tengrinews.kz{art_url}')
#
#     time.sleep(randrange(2, 4))
#
#     with open('articles_urls_list.txt', 'w') as file:
#         for url in articles_urls_list:
#             file.write(f'{url}\n')
#
# print(f'Операция записи ссылок в файл завершена!\n'
#       f'Проанализировано {pagination_count} страниц')

s_url = 'https://tengrinews.kz/kazakhstan_news/tokaev-pavodkah-vozmojno-samoe-krupnoe-bedstvie-poslednie-80-531444/'
s_page = requests.get(s_url)
s_soup = BeautifulSoup(s_page.text, "html.parser")

news_title = s_soup.find(class_='head-single')
news_date = s_soup.find(class_='date-time')
news_pic = f"https://tengrinews.kz/{s_soup.find('picture', class_='content_main_thumb_img').find('img').get('src')}"
news_text = s_soup.find(class_='content_main_text')

print(news_title.text.strip())
print(news_date.text.strip())
print(news_pic)
print(news_text.text)
# head-single



