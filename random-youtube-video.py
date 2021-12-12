from random import choice
from requests import get
alphabet = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
url = 'https://www.youtube.com/watch?v='

for i in range(11):
    url += choice(alphabet)
remove = []
while True:
    url = 'https://www.youtube.com/watch?v='
    for i in range(11):
        url += choice(alphabet)
    if url in remove:
        continue
    text = get(url).text
    if not "Video unavailable" in text:
        print(url,"Video unavailable" in text)
        break
    else:
        remove.append(url) 

print(url,"Video unavailable" in get(url).text)