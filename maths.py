import random
import time
n = int(input('Choose between normal and endless mode 1/2: '))
if n == 1:
    right = 0
    max_ = 0
    start = time.time()
    for i in range(20):
        x = random.randint(1,30)
        y = random.randint(1,30)
        z = random.choice(['+','-','*','/'])
        a = time.time()
        if z == '+':
            if int(input(f'{x}+{y}: ')) == x+y:
                print('Correct!')
                right += 1
            else:
                print(f'Wrong. The correct answer was {x+y}')
        elif z == '-':
            if int(input(f'{x}-{y}: ')) == x-y:
                print('Correct!')
                right += 1
            else:
                print(f'Wrong. The correct answer was {x-y}')
        elif z == '*':
            if int(input(f'{x}*{y}: ')) == x*y:
                print('Correct!')
                right += 1
            else:
                print(f'Wrong. The correct answer was {x*y}')
        elif z == '/':
            x = random.randint(1,200)
            while x/y != int(x/y):
                y = random.randint(1,x)
            if int(input(f'{x}/{y}: ')) == x/y:
                print('Correct!')
                right += 1
            else:
                print(f'Wrong. The correct answer was {round(x/y,2)}')
        b = time.time()
        if b-a > max_:
            max_ = b-a
            max__ = f'{x}{z}{y}'  
    end = time.time()
    delta = round(end-start,3)
    print('20 Questions done. Stats:')
    print(f'\tTotal time taken:        {delta} seconds')
    print(f'\tTime taken per question: {round(delta/20,2)} seconds')
    print(f'\tCorrect answers:         {right}')
    print(f'\tWrong answers:           {20-right}')    
    print(f'\tAccuracy:                {round((right/20)*100,2)}%') 
    print(f'\tLongest time taken:      Question : {max__} , {round(max_,2)} seconds')
