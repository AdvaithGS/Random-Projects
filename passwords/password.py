import random
import pyperclip
length = int(input('Max length?(24 is the usual): '))
password = ''
while len(password) != length:
    password += random.choice("!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
print(password)
pyperclip.copy(password)
print('Copied to clipboard')
