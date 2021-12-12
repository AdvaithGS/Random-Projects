from random import randrange
from requests import get
import requests
url = 'https://www.youtube.com/watch?v='
for i in range(11):
    url += str(chr(randrange(65,123)))
while get(url).text.find("This video isn't available anymore") != -1:
    url = 'https://www.youtube.com/watch?v='
    for i in range(11):
        url += str(chr(randrange(65,123)))
