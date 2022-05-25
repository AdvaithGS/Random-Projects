from requests import get
from json import loads
from random import choice
words = loads(get('https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json').text)
x = choice(list(words.keys()))
typ = input('Type: ')
def check(typ,x):
  try:
    res = loads(get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{x}').text)[0]['meanings']
  except:
    return False
  for i in res:
    if i['partOfSpeech'] == typ:
      return True
  return False

l = []
while len(l) < int(input('How many words?: ')):
  x = choice(list(words.keys()))
  if check(typ,x):
    l.append(x)
for x in l:
  res = loads(get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{x}').text)
  try:
    print(x,':',res[0]['meanings'][0]['definitions'][0]['definition'])
  except:
    print(x,None)
