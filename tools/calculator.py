from math import *
from time import sleep
while True:
    choice = input('''1 for addition,\n2 for subtraction,\n3 for multiplication,\n4 for division,\n5 for exponentiation,\n6 for trigonometry (regular),\n7 for trigonometry (inverse)\n0 to exit: \n--> ''')
    if choice == '1':
        print(float(input('First number: '))+float(input('Second number: ')))
        sleep(2)
    elif choice == '2':
        print(float(input('First number: ')) - float(input('Second number: ')))
        sleep(2)
    elif choice == '3':
        print(float(input('First number: '))*float(input('Second number: ')))
        sleep(2)
    elif choice == '4':
        print(float(input('First number: '))/float(input('Second number: ')))
        sleep(2)
    elif choice == '5':
        print(float(input('First number: '))**float(input('Second number: ')))
        sleep(2)
    elif choice == '6':
        while True:
            choice = input('''Sin: 1,\nCos: 2,\nTan: 3\nBack: 0\n--> ''')
            if choice == '1':
                while True:
                    choice = input('''Radians Gang: 1,\nDegrees gang: 2,\nBack: 0\n--> ''')
                    if choice == '1':
                        s = input(f'Sine: Enter value in radians (you can write \"pi\" for pi): ')
                        try:
                            s = s.replace('pi',f'{pi}')
                        except:
                            pass
                        s = eval(s)
                        print(round(sin(s),5))
                        break
                    elif choice == '2':
                        print(sin(radians(float(input('Sine: Enter value in degrees: ')))))
                        break
                    elif choice == '0':
                        break
            elif choice == '2':
                while True:
                    choice = input('''Radians Gang: 1,\nDegrees gang: 2,\nBack: 0\n--> ''')
                    if choice == '1':
                        s = input(f'Cosine: Enter value in radians (you can write \"pi\" for pi): ')
                        try:
                            s = s.replace('pi',f'{pi}')
                        except:
                            pass
                        s = eval(s)
                        print(round(cos(s),5))
                        break
                    elif choice == '2':
                        print(cos(radians(float(input('Cosine: Enter value in degrees: ')))))
                        break
                    elif choice == '0':
                        break
            elif choice == '3':
                while True:
                    choice = input('''Radians Gang: 1,\nDegrees gang: 2,\nBack: 0\n--> ''')
                    if choice == '1':
                        s = input(f'Tangent: Enter value in radians (you can write \"pi\" for pi): ')
                        try:
                            s = s.replace('pi',f'{pi}')
                        except:
                            pass
                        s = eval(s)
                        print(round(tan(s),5))
                        break
                    elif choice == '2':
                        print(tan(radians(float(input('Tangent: Enter value in degrees: ')))))
                        break
                    elif choice == '0':
                        break
            elif choice == '0':
                break
            sleep(2)
    elif choice == '7':
        while True:
                choice = input('''Sin (inverse): 1,\nCos (inverse): 2,\nTan (inverse): 3,\nExit: 0\n--> ''')
                if choice == '1':
                    while True:
                        choice = choice = input('''Radians Gang: 1,\nDegrees Gang: 2,\nExit: 0\n--> ''')
                        if choice == '1':
                            print(asin(int(input('Sine (inverse): enter value: '))))
                            break
                        elif choice == '2':
                            print(degrees(asin(int(input('Sine (inverse): enter value: ')))))
                            break
                        elif choice == '0':
                            break
                elif choice == '2':
                    while True:
                        choice = choice = input('''Radians Gang: 1,\nDegrees Gang: 2,\nExit: 0\n--> ''')
                        if choice == '1':
                            print(acos(int(input('Cosine (inverse): enter value: '))))
                            break
                        elif choice == '2':
                            print(degrees(acos(int(input('Cosine (inverse): enter value: ')))))
                            break
                        elif choice == '0':
                            break
                elif choice == '3':
                    while True:
                        choice = choice = input('''Radians Gang: 1,\nDegrees Gang: 2,\nExit: 0\n--> ''')
                        if choice == '1':
                            print(atan(int(input('Tangent (inverse): enter value: '))))
                            break
                        elif choice == '2':
                            print(degrees(atan(int(input('Tangent (inverse): enter value: ')))))
                            break
                        elif choice == '0':
                            break
                elif choice == '0':
                    break
    elif choice == '0':
        break
    elif choice == '42':
        print('The number of the universe and everything.....I see youre a person of culture')
        sleep(2)