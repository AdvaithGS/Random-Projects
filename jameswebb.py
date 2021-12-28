import requests
from bs4 import BeautifulSoup
from json import loads
from time import strftime,gmtime

from requests.hooks import dispatch_hook
d = int(strftime('%d',gmtime()))
s = strftime(f'%Y/%m/{d-7}-%H:48:00',gmtime()) 
req = requests.get('https://jwst.nasa.gov/content/webbLaunch/whereIsWebb.html?s=09').text
soup = BeautifulSoup(req,'lxml')
page = soup.find_all('script')[6].text
a = page[page.find(s)-100 :page.find(s)+230].replace(s,s.replace(':','/'))
found = loads(a[a.index(',{')+1: a.rindex(',{') ].replace(',',',"').replace(':','":').replace('{','{"'))
daysPassed = int(float(found['elapsedDays']) // 1 )
hoursPassed = round((float(found['elapsedDays'])%1)*24)
elapsedtime = f'{daysPassed} days and {hoursPassed} hours'
fromEarth = float(found['distanceTravelledKm']) + float(found['velocityKmSec'])*(int(strftime('%M'))-48)*60
tol2 = round(1446320 - fromEarth,3)
completion = round(fromEarth/1446320*100,3)
print(elapsedtime,fromEarth,tol2,completion,sep = '\n')
#distance between Earth and l2 -1446320 