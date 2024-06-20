from bs4 import BeautifulSoup
import requests
from termcolor import colored
import time


req = requests.get('https://finance.yahoo.com/world-indices/').text

soup = BeautifulSoup( req , 'lxml')


while True:
    for i in [635,41]:
        article  = soup.find('td', attrs = {'data-reactid': i})
        article2 = soup.find('td', attrs = {'data-reactid': i+2}).text
        article3 = soup.find('td', attrs = {'data-reactid': i+4}).text
        article4 = soup.find('td', attrs = {'data-reactid': i+9}).text
        if article3.startswith('-'):
            article3 =  colored(article3, 'red')
            article2 =  colored(article2, 'red')
        elif article3.startswith('0.00'):
            article3 =  colored(article3, 'yellow')
            article2 =  colored(article2, 'yellow')
        elif not article3.startswith('-'):
            article3 =  colored(article3, 'green')
            article2 =  colored(article2, 'green')
        if article4.startswith('-'):
            article4 =  colored(article4, 'red')
        elif article4.startswith('0.00'):
            article4 =  colored(article4, 'yellow')
        elif not article4.startswith('-'):
            article4 =  colored(article4, 'green')
        print(f'{article.text} : {article2} : {article3} : {article4}')
    time.sleep(5)