from random import randrange
from requests import get
import requests
url = 'https://www.youtube.com/watch?v='
for i in range(11):
    url += str(chr(randrange(65,123)))
while get('https://www.youtube.com/watch?v=_NCdAHCuqpd').text.find("This video isn't available any more") != -1:
    url = 'https://www.youtube.com/watch?v='
    for i in range(11):
        url += str(chr(randrange(65,123)))
print(url)