from ast import literal_eval
from requests import get
from bs4 import BeautifulSoup
req= get('https://www.jwst.nasa.gov/content/webbLaunch/deploymentExplorer.html').text
soup = BeautifulSoup(req, 'lxml')
s = soup.find_all('script')[-5].text[soup.find_all('script')[-5].text.find('[',202):soup.find_all('script')[-5].text.rfind(']')+1].replace('\\x20',' ' ).replace('\\x27' , ' ' ).split(',')
for i in range(len(s)):
    if 'Launch + 3 days' in s[i] and 'nominalEventTime' in s[i]:
        print(s[i],s[i+1].split(':')[1].split('(')[1][:-1][2:])
        print(s[467],s[466],s[465],s[561],s[639])