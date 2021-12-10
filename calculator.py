from math import *
while True:
    choice = int(input('''1 for addition, 
        2 for subtraction, 3 for multiplication, 4 for division, 5 for exponentiation, 6 for trigonometry, 0 to exit: '''))
    if choice == 1:
        while True:     
            choice = int(input('''Float: 1,
                    Integer: 2,
                    Back: 0'''))
            if choice == 1:
                print(float(input('First number'))+float(input('Second number')))
                break
            elif choice == 2:
                print(int(input('First number'))+int(input('Second number'))) 
                break
            elif choice == 0:
                break
    elif choice == 2:
        while True:    
            choice = int(input('''Float: 1,
                    Integer: 2,
                    Back: 0'''))
            if choice == 1:
                print(float(input('First number'))-float(input('Second number')))
                break
            elif choice == 2:
                print(int(input('First number'))-int(input('Second number'))) 
                break
            elif choice == 0:
                break
    elif choice == 3:
        while True:
            choice = int(input('''Float: 1,
                    Integer: 2,
                    Back: 0'''))
            if choice == 1:
                print(float(input('First number'))*float(input('Second number')))
                break
            elif choice == 2:
                print(int(input('First number'))*int(input('Second number'))) 
                break
            elif choice == 0:
                break
    elif choice == 4:
        while True:    
            choice = int(input('''Float Divide: 1,
                    Integer Divide: 2,
                    Back: 0'''))
            if choice == 1:
                print(float(input('First number'))/float(input('Second number')))
                break
            elif choice == 2:
                print(int(input('First number'))//int(input('Second number'))) 
                break
            elif choice == 0:
                break
    elif choice == 5:
        print(float(input('First number'))**float(input('Second number'))) 
    elif choice == 6:
        while True:
            choice = int(input('''Sin: 1,
                    Cos: 2,
                    Tan: 3
                    Back: 0 '''))
            if choice == 1:
                while True:
                    choice = int(input('''Radians Gang: 1
                    Degrees gang: 2, Back: 0 '''))
                    if choice == 1:
                        print(sin(int(input('Enter value'))))
                        break
                    elif choice == 2:
                        print(sin(radians(int(input('Enter value')))))
                        break
                    elif choice == 0:
                        break
            elif choice == 2:
                while True:
                    choice = int(input('''Radians Gang: 1
                    Degrees gang: 2, Back: 0 '''))
                    if choice == 1:
                        print(cos(int(input('Enter value'))))
                        break
                    elif choice == 2:
                        print(cos(radians(int(input('Enter value')))))
                        break
                    elif choice == 0:
                        break
            elif choice == 3:
                while True:
                    choice = int(input('''Radians Gang: 1
                    Degrees gang: 2, Back: 0 '''))
                    if choice == 1:
                        print(tan(int(input('Enter value'))))
                        break
                    elif choice == 2:
                        print(tan(radians(int(input('Enter value')))))
                        break
                    elif choice == 0:
                        break
            elif choice == 0:
                break
    elif choice == 0:
        break
    elif choice == 42:
        print('The number of the universe and everything.....I see youre a person of culture')