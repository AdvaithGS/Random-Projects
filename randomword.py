from requests import get
from random import choice
words = get('https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json').json()
x = choice(list(words.keys()))
typ = input('Type: ')
def check(typ,x):
  try:
    res = get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{x}').json()[0]['meanings']
  except:
    return False
  for i in res:
    if i['partOfSpeech'] == typ:
      return True
  return False

l = []
n = int(input('How many words?: '))
while len(l) < n:
  x = choice(list(words.keys()))
  if check(typ,x):
    l.append(x)
for x in l:
  res = get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{x}').json()
  try:
    print(x,':',res[0]['meanings'][0]['definitions'][0]['definition'])
  except:
    print(x,None)
