import webbrowser
import pyautogui as pgui
import time
#works only with a python file called contacts
from contacts import contacts
user = input('''Send message: 1
Send message with image: 2 
Edit Contacts: 3
''')
if user == '1':
    num = contacts[input('Enter name: ')]
    mes = input('Enter message: ').replace(' ','%20')
    try:
        when = int(input('How many seconds from now? Leave blank if immediately: '))
    except:
        when = 0
    print('It shall be done.')
    webbrowser.open_new_tab(f'https://web.whatsapp.com/send?phone=+91{num}&text={mes}')
    if when > 200:
        time.sleep(when - 17)
    else:
        time.sleep(17)
    width,height = pgui.size()
    pgui.click(width/2,height/2)
    pgui.press('enter')
elif user == '3':
    n = 1
    for i in contacts:
        print(n ,i ,' - ' , contacts[i])
        n += 1
    choice = input('1- Edit names, 2- Edit number: ')
    s = int(input('Enter index number: '))
    keys = list(contacts.keys())
    if choice == '1':
        contacts[input('Enter updated name: ')] = contacts[keys[s-1]]
        del contacts[keys[s-1]]
    elif choice == '2':
        contacts[keys [s-1]]  = input('Enter updated number: ')
