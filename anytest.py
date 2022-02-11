#this program only works for astronomical objects and bodies
import requests
from json import loads
from pprint import pprint
from bs4 import BeautifulSoup
import webbrowser
from os import environ
language_code = 'en'
search_query = input('Enter query: ')
number_of_results = 1
website = 'wikipedia'
headers = {
        'Authorization': environ['api_key5'],
        'User-Agent': 'Advaith'
            }
#url = f'https://api.wikimedia.org/core/v1/{website}/en/page/{search_query}/bare'
#parameters = {'q': search_query, 'limit': number_of_results}
#response = requests.get(url, headers=headers)
url = f'https://en.wikipedia.org/w/rest.php/v1/page/{search_query}/html'
req = requests.get(url).text
soup = BeautifulSoup(req,'lxml')
#print(loads(response.text)['html_url'])
d = {}
try:
    if 'refer to' in soup.find_all('p')[1].text:
        x = d['13']
    text = soup.find_all('p')[0].text
    if len(text) < 100:
        text = soup.find_all('p')[1].text
        if len(text) < 100:
            text = soup.find_all('p')[2].text
            if len(text) < 100:
                text = soup.find_all('p')[3].text
    while '[' in text:
        text = text.replace(text[text.find('['):text.find(']',text.find('['))+1],'')
    print(text)
except:
    if 'refer' in soup.find_all('p')[0].text or 'refer' in soup.find_all('p')[1].text:
        for i in soup.find_all('a'):
            l = ['moon','star','space','astro','cluster','galaxy']
            if any([z in i.text.lower() for z in l]):
                search_query = i['href'][1:]
                url = 'https://en.wikipedia.org/w/rest.php/v1/page' + i['href'][1:] + '/html'
                req = requests.get(url).text
                soup = BeautifulSoup(req,'lxml')
                text = soup.find_all('p')[0].text
                if len(text) < 100:
                    text = ''
                    text += soup.find_all( 'p')[1].text
                while '[' in text:
                    text = text.replace(text[text.find('['):text.find(']',text.find('['))+1],'') 
                print(text)
                break
    else:
        print('Not found')
        exit()
url = f'https://api.wikimedia.org/core/v1/{website}/en/search/page'
parameters = {'q': search_query, 'limit': number_of_results}
response = requests.get(url, headers=headers, params=parameters)
try:
    image = 'https:' + loads(response.text)['pages'][0]['thumbnail']['url'].replace('/thumb','').rsplit('/',1)[0]
    webbrowser.open_new_tab(image)
except:
    image =  None





