from requests import get
l = []
def get_next(req):
  a = req.find('"title":{"simpleText":')
  req_ = req[a-4:]
  req = req[:a-4]
  channel = req[req.rfind('"')+1:]
  print(channel)
  if channel not in l:
    return get_next(get(f'https://www.youtube.com/{channel}/channels').text)
  elif '/' not in channel:
    return 
  else:
    return get_next(channel,req_)
print(get_next(get(f'https://www.youtube.com/c/ImpulseSV/channels').text))
