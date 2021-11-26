def binary(n):
    if n != '0' and n != 0:
        n = int(n)
        ans = []
        while n > 0:
            i = 0
            while 2**i <= n:
                i += 1
            n -= 2**(i-1)
            i -= 1
            ans.append(i)
        result = '0'*(int(ans[0]) + 1)
        for i in ans:
            result = result[:i] + '1' + result[i+1:]
    else:
        result = '0'
    return result[::-1]
def binary_to_decimal(num):
    num = num[::-1]
    ans = 0
    for i in range(len(num)):
        if num[i] == '1':
            ans += 2**i
    return ans

def octal(num):
    ans = ''
    num = str(num)
    num = '0'*(3 - len(num)%3) + num
    for i in range(len(num)//3):
        ans += str(binary_to_decimal(num[3*i:3*(i+1)]))
    return ans

def octal_to_decimal(num):
    num = str(num)
    ans = str(binary(int(num[0])))
    for i in num[1:]:
        bin = str(binary(int(i)))
        if len(bin) != 3:
            ans += '0'*(3 - len(bin)%3) + bin
        else:
            ans += bin
    return binary_to_decimal(ans)

def hexadecimal(num):
    ans = ''
    num = str(num)
    num = '0'*(4 - len(num)%4) + num
    for i in range(len(num)//4):
        res = str(binary_to_decimal(num[4*i:4*(i+1)]))
        alphabet = 'ABCDEF'
        if int(res) >= 10:
            ans += alphabet[int(res)-10]
        else:
            ans += res
    while ans[0] == '0':
        ans = ans[1:]
    return ans

def hexadecimal_to_decimal(num):
    ans = ''
    for i in num:
        if i.isdigit():
            if len(binary(i)) != 4:
                ans += '0'*(4 - len(binary(i))%4) + binary(i)
            else:
                ans += binary(i)
        else:
            alphabet = 'ABCDEF'
            if len(binary(alphabet.find(i) + 10)) != 4:
                ans += '0'*(4 - len(binary(alphabet.find(i) + 10))%4) + binary(alphabet.find(i) + 10)
            else:
                ans += binary(alphabet.find(i) + 10)
    return binary_to_decimal(ans)
import random

choice = input('Data Type Quiz! Choose your Type. \n 1. Decimal to Binary \n 2. Binary to Decimal \n 3. Decimal to Octal \n 4. Octal to Decimal \n 5. Decimal to Hexadecimal \n 6. Hexadecimal to Decimal \n 7. Binary to Octal \n 8. Octal to Binary \n 9. Binary to Hexadecimal \n 10. Hexadecimal to Binary \n 11. Octal to Hexadecimal \n 12. Hexadecimal to Octal \n --> ')
if choice == '1':
    print('Decimal to Binary!')
    score = 0
    running  = True
    print(f'Your score is {score}')
    while running:
        num = random.randrange(1,1000)
        if input(f'Convert the following decimal number to binary: {num} --> ') == binary(num):
            score += 1
            print(f'Well done! You got the correct answer! You now have {score} points.')
        else:
            print(f'Your answer is incorrect. The correct answer was {binary(num)}')
        play_again = input('Do you want to continue playing? Y/N or y/n or leave blank: ')
        if play_again.lower() == 'y' or not play_again:
            continue
        else:
            break
elif choice == '2':
    print('Binary to Decimal!')
    score = 0
    running  = True
    print(f'Your score is {score}')
    while running:
        num = binary(random.randrange(1,1000))
        if input(f'Convert the following binary number to decimal: {num} --> ') == binary_to_decimal(num):
            score += 1
            print(f'Well done! You got the correct answer! You now have {score} points.')
        else:
            print(f'Your answer is incorrect. The correct answer was {binary_to_decimal(num)}')
        play_again = input('Do you want to continue playing? Y/N or y/n or leave blank: ')
        if play_again.lower() == 'y' or not play_again:
            continue
        else:
            break
elif choice == '3':
    print('Decimal to Octal!')
    score = 0
    running  = True
    print(f'Your score is {score}')
    while running:
        num = random.randrange(1,1000)
        if input(f'Convert the following decimal number to octal: {num} --> ') == binary(num):
            score += 1
            print(f'Well done! You got the correct answer! You now have {score} points.')
        else:
            print(f'Your answer is incorrect. The correct answer was {octal(binary(num))}')
        play_again = input('Do you want to continue playing? Y/N or y/n or leave blank: ')
        if play_again.lower() == 'y' or not play_again:
            continue
        else:
            break
elif choice == '4':
    print('Octal to Decimal!')
    score = 0
    running  = True
    print(f'Your score is {score}')
    while running:
        num = octal(binary(random.randrange(1,1000)))
        if input(f'Convert the following octal number to decimal: {num} --> ') == binary(num):
            score += 1
            print(f'Well done! You got the correct answer! You now have {score} points.')
        else:
            print(f'Your answer is incorrect. The correct answer was {octal_to_decimal(num)}')
        play_again = input('Do you want to continue playing? Y/N or y/n or leave blank: ')
        if play_again.lower() == 'y' or not play_again:
            continue
        else:
            break
elif choice == '5':
    print('Decimal to Hexadecimal!')
    score = 0
    running  = True
    print(f'Your score is {score}')
    while running:
        num = random.randrange(1,1000)
        if input(f'Convert the following decimal number to hex: {num} --> ') == binary(num):
            score += 1
            print(f'Well done! You got the correct answer! You now have {score} points.')
        else:
            print(f'Your answer is incorrect. The correct answer was {hexadecimal(binary(num))}')
        play_again = input('Do you want to continue playing? Y/N or y/n or leave blank: ')
        if play_again.lower() == 'y' or not play_again:
            continue
        else:
            break
elif choice == '6':
    print('Hexadecimal to Decimal!')
    score = 0
    running  = True
    print(f'Your score is {score}')
    while running:
        num = hexadecimal(binary(random.randrange(1,1000)))
        if input(f'Convert the following Hexadecimal number to decimal: {num} --> ') == binary(num):
            score += 1
            print(f'Well done! You got the correct answer! You now have {score} points.')
        else:
            print(f'Your answer is incorrect. The correct answer was {hexadecimal_to_decimal(num)}')
        play_again = input('Do you want to continue playing? Y/N or y/n or leave blank: ')
        if play_again.lower() == 'y' or not play_again:
            continue
        else:
            break
elif choice == '7':
    print('Octal to Binary!')
    score = 0
    running  = True
    print(f'Your score is {score}')
    while running:
        num = octal(binary(random.randrange(1,1000)))
        if input(f'Convert the following Octal number to Binary: {num} --> ') == binary(num):
            score += 1
            print(f'Well done! You got the correct answer! You now have {score} points.')
        else:
            print(f'Your answer is incorrect. The correct answer was {binary(octal_to_decimal(num))}')
        play_again = input('Do you want to continue playing? Y/N or y/n or leave blank: ')
        if play_again.lower() == 'y' or not play_again:
            continue
        else:
            break