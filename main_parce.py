from bs4 import BeautifulSoup
from lxml import html

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
filename = 'test.html'

def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
    return text

def find_num(filename):
    text = read_file(filename)
    soup = BeautifulSoup(text, 'lxml')
    #soup.find('div', {'class': 'profileFilmsList'})
    #kurs = soup.find('div', {'class': 't18'}).find_all('b').text
    print ([tag.text.strip() for tag in soup.find_all('div', {'class': 't18'})])
    #return kurs
    #print (kurs)

find_num(filename)