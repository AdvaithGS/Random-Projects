from math import *
from time import sleep
while True:
    choice = int(input('''1 for addition,\n2 for subtraction,\n3 for multiplication,\n4 for division,\n5 for exponentiation,\n6 for trigonometry,\n0 to exit: \n--> '''))
    if choice == 1:
        while True:     
            choice = int(input('''Float: 1,\nInteger: 2,\nBack: 0\n--> '''))
            if choice == 1:
                print(float(input('First number: '))+float(input('Second number: ')))
                break
            elif choice == 2:
                print(int(input('First number: '))+int(input('Second number: ')))
                break
            elif choice == 0:
                break
            sleep(1)
    elif choice == 2:
        while True:
            choice = int(input('''Float: 1,\nInteger: 2,\nBack: 0\n--> '''))
            if choice == 1:
                print(float(input('First number: '))-float(input('Second number: ')))
                break
            elif choice == 2:
                print(int(input('First number: '))-int(input('Second number: '))) 
                break
            elif choice == 0:
                break
            sleep(1)
    elif choice == 3:
        while True:
            choice = int(input('''Float: 1,\nInteger: 2,\nBack: 0\n--> '''))
            if choice == 1:
                print(float(input('First number: '))*float(input('Second number: ')))
                break
            elif choice == 2:
                print(int(input('First number: '))*int(input('Second number: '))) 
                break
            elif choice == 0:
                break
                sleep(1)
    elif choice == 4:
        while True:    
            choice = int(input('''Float Divide: 1,\nInteger Divide: 2,\nBack: 0\n--> '''))
            if choice == 1:
                print(float(input('First number: '))/float(input('Second number: ')))
                break
            elif choice == 2:
                print(int(input('First number: '))//int(input('Second number: '))) 
                break
            elif choice == 0:
                break
                sleep(1)
    elif choice == 5:
        print(float(input('First number: '))**float(input('Second number: '))) 
        sleep(1)
    elif choice == 6:
        while True:
            choice = int(input('''Sin: 1,\nCos: 2,\nTan: 3\nBack: 0\n--> '''))
            if choice == 1:
                while True:
                    choice = float(input('''Radians Gang: 1,\nDegrees gang: 2,\nBack: 0\n--> '''))
                    if choice == 1:
                        print(sin(float(input('Enter value: '))))
                        break
                    elif choice == 2:
                        print(sin(radians(float(input('Enter value: ')))))
                        break
                    elif choice == 0:
                        break
            elif choice == 2:
                while True:
                    choice = int(input('''Radians Gang: 1,\nDegrees gang: 2,\nBack: 0\n--> '''))
                    if choice == 1:
                        print(cos(float(input('Enter value: '))))
                        break
                    elif choice == 2:
                        print(cos(radians(float(input('Enter value: ')))))
                        break
                    elif choice == 0:
                        break
            elif choice == 3:
                while True:
                    choice = int(input('''Radians Gang: 1,\nDegrees gang: 2,\nBack: 0\n--> '''))
                    if choice == 1:
                        print(tan(float(input('Enter value: '))))
                        break
                    elif choice == 2:
                        print(tan(radians(float(input('Enter value: ')))))
                        break
                    elif choice == 0:
                        break
            elif choice == 0:
                break
            sleep(1)
    elif choice == 0:
        break
    elif choice == 42:
        print('The number of the universe and everything.....I see youre a person of culture')
        sleep(1)