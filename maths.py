import random
import time
n = int(input('Choose between normal and endless mode 1/2: '))
right = 0
max_ = 0
start = time.time()
if n == 1:
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
            while x%y == 0:
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
    number = 20
elif n ==2:
    number = 0
    while True:
        number += 1
        a = time.time()
        x = random.randint(1,30)
        y = random.randint(1,30)
        z = random.choice(['+','-','*','/'])
        if z == '+':
            inp = input(f'{x}+{y}: ')
            if inp == 'exit':
                number -= 1
                print('Exiting...')
                break
            elif int(inp) == x+y:
                print('Correct!')
                right += 1
            else:
                print(f'Wrong. The correct answer was {x+y}')
        elif z == '-':
            inp = input(f'{x}-{y}: ')
            if inp == 'exit':
                number -= 1
                print('Exiting...')
                break
            elif int(inp) == x-y:
                print('Correct!')
                right += 1
            else:
                print(f'Wrong. The correct answer was {x-y}')
        elif z == '*':
            inp = input((f'{x}*{y}: '))
            if inp == 'exit':
                number -= 1
                print('Exiting...')
                break
            elif int(inp) == x*y:
                print('Correct!')
                right += 1
            else:
                print(f'Wrong. The correct answer was {x*y}')
        elif z == '/':
            x = random.randint(1,200)
            while x/y != int(x/y):
                y = random.randint(1,x)
            inp = input(f'{x}/{y}: ')
            if inp == 'exit':
                number -= 1
                print('Exiting...')
                break
            elif int(inp) == x/y:
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
print(f'{number} Questions done. Stats:')
print(f'\tTotal time taken:        {delta} seconds')
print(f'\tTime taken per question: {round(delta/number,2)} seconds')
print(f'\tCorrect answers:         {right}')
print(f'\tWrong answers:           {number-right}')    
print(f'\tAccuracy:                {round((right/number)*100,2)}%') 
print(f'\tLongest time taken:      Question : {max__} , {round(max_,2)} seconds')   
    