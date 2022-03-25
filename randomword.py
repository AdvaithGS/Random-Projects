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
  

while not check(typ,x):
  x = choice(list(words.keys()))

print(x)