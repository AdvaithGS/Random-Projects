from termcolor import colored
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
    while ans[0] == '0':
        ans = ans[1:]
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

choice = int(input(colored('Data Type Quiz! Choose your Type. \n 1. Decimal to Binary \n 2. Binary to Decimal \n 3. Decimal to Octal \n 4. Octal to Decimal \n 5. Decimal to Hexadecimal \n 6. Hexadecimal to Decimal \n 7. Binary to Octal \n 8. Octal to Binary \n 9. Binary to Hexadecimal \n 10. Hexadecimal to Binary \n 11. Octal to Hexadecimal \n 12. Hexadecimal to Octal \n --> ','cyan')))
num = random.randrange(1,1000)
operations  = [
['Decimal to Binary!','decimal number to binary',num,binary(num)],
['Binary To Decimal!','binary number to decimal',binary(num),str(num)],
['Decimal to Octal!','decimal number to octal',num,octal(binary(num))],
['Octal to Decimal!','octal number to decimal',octal(binary(num)),str(num)],
['Decimal to Hexadecimal!','decimal number to hex',num,hexadecimal(binary(num))],
['Hexadecimal to Decimal!','hexadecimal number to decimal',hexadecimal(binary(num)),str(num)],
['Octal to Binary!','octal number to binary',octal(binary(num)),binary(num)],
['Binary to Octal!','binary number to octal',binary(num),octal(binary(num))],
['Binary to Hexadecimal!','binary number to hexadecimal',binary(num),hexadecimal(binary(num))],
['Hexadecimal to Binary!','hexadecimal number to binary',hexadecimal(binary(num)),binary(num)],
['Octal to Hexadecimal!','octal number to hexadecimal',octal(binary(num)),hexadecimal(binary(num))],
['Hexadecimal to Octal!','Hexadecimal number to Octal',hexadecimal(binary(num)),octal(binary(num))],
]
index = operations[choice-1]
print(colored(index[0],'yellow'))
score = 0
running  = True
print(colored(f'Your score is {score}','yellow'))
while running:
        if input(colored(f'Convert the following {index[1]}: {index[2]} --> ','magenta')) == str(index[3]):
            score += 1
            print(colored(f'Well done! You got the correct answer! You now have {score} points.','green'))
        else:
            print(colored(f'Your answer is incorrect. The correct answer was {index[3]}','red'))
        play_again = input(colored('Do you want to continue playing? Y/N or y/n or leave blank: ','magenta'))
        if play_again.lower() == 'y' or not play_again:
            num = random.randrange(1,1000)
            operations  = [
            ['Decimal to Binary!','decimal number to binary',num,binary(num)],
            ['Binary To Decimal!','binary number to decimal',binary(num),num],
            ['Decimal to Octal!','decimal number to octal',num,octal(binary(num))],
            ['Octal to Decimal!','octal number to decimal',octal(binary(num)),num],
            ['Decimal to Hexadecimal!','decimal number to hex',num,hexadecimal(binary(num))],
            ['Hexadecimal to Decimal!','hexadecimal number to decimal',hexadecimal(binary(num)),num],
            ['Octal to Binary!','octal number to binary',octal(binary(num)),binary(num)],
            ['Binary to Octal!','binary number to octal',binary(num),octal(binary(num))],
            ['Binary to Hexadecimal!','binary number to hexadecimal',binary(num),hexadecimal(binary(num))],
            ['Hexadecimal to Binary!','hexadecimal number to binary',hexadecimal(binary(num)),binary(num)],
            ['Octal to Hexadecimal!','octal number to hexadecimal',octal(binary(num)),hexadecimal(binary(num))],
            ['Hexadecimal to Octal!','Hexadecimal number to Octal',hexadecimal(binary(num)),octal(binary(num))],
            ]
            index = operations[choice-1]
            continue
        else:
            break