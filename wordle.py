from requests import get
from json import loads
f= open('words.txt')
l = []
for i in f.read().splitlines():
    if len(i) == 5:
        l.append(i)
f.close()
s = []
for i in range(len(l)):
    try:
        if type((loads(get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{l[i]}').text))) == list:
            s.append(l[i] + '\n')
    except:
        pass
f = open('wordle.txt','w')
f.writelines(l)
f.close()
