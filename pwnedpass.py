#Inspired by the Computerphile video featuring the Have I Been Pwned API 
#Finding out whether your password has been found out in any leak
import hashlib
from requests import get
s = input('Enter password: ')
x = hashlib.sha1(s.encode()).hexdigest().capitalize()

req = get(f'https://api.pwnedpasswords.com/range/{x[:5]}').text.replace('\r','').split('\n')
for i in range(len(req)):
    req[i] = req[i].split(':')
req = dict(req)
for i in req:
    if i == x:
        print(f'Password Found: {s}')
        print(f'Hash: {x}  Times Found: {req[i]}')
        break
else:
    print('Not Found, Congrats!')