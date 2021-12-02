import random
import pyperclip
password = ''
while len(password) != 24:
    password += random.choice("!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
print(password)
pyperclip.copy(password)
print('Copied to clipboard')
