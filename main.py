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
#
# # pagination_count = int(soup.find('ul', class_='pagination').find_all('a')[-2].text)
# # print(pagination_count)
#
#
# articles_urls_list = list()
# count = 0
# pagination_count = 10
# for page in range(1, pagination_count+1):
#     count += 1
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
#     print(f'Программа работает {count}/{pagination_count}')
#
# print(f'Операция записи ссылок в файл завершена!\n'
#       f'Проанализировано {pagination_count} страниц')



result_data = list()

file_name = 'articles_urls_list.txt'
print(os.path.exists(file_name))
with open(file_name, 'r') as file:
    # print(file.read())
    data_urls = [line.strip() for line in file.readlines()]

for s_url in data_urls[:30]:
    s_page = requests.get(s_url)
    s_soup = BeautifulSoup(s_page.text, "html.parser")

    try:
        news_title = s_soup.find(class_='head-single').text.strip()
        news_date = s_soup.find(class_='date-time').text.strip()
        news_pic = f"https://tengrinews.kz/{s_soup.find('picture', class_='content_main_thumb_img').find('img').get('src')}"
        news_text = s_soup.find(class_='content_main_text').text.replace('\n', '')

        result_data.append(
            {
                'url': s_url,
                'news_title': news_title,
                'news_date': news_date,
                'news_pic': news_pic,
                'news_text': news_text
            }
        )

    except:
        print('Ошибка...')
    # print(news_title.text.strip())
    # print(news_date.text.strip())
    # print(news_pic)
    # print(news_text.text.replace('\n', ''))

with open('result_json.json', 'w') as file:
    json.dump(result_data, file, ensure_ascii=False, indent=2)


print('Программа завершила работу.')