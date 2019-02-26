#import scrapy

import requests
#user_id = str(12345)
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
url = 'https://www.calc.ru/forex-USD-RUB.html'\
      #% (user_id) # url для второй страницы
r = requests.get(url, headers = headers)

with open('test.html', 'wb') as output_file:
    output_file.write(r.text.encode('cp1251'))