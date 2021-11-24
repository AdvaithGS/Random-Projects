choice = input('Choose operation: 1 - Decimal to Binary: 2 - Binary to Decimal: 3 - Decimal to Octal: 4 - Octal to Decimal: 5 - Decimal to Hexadecimal: 6 - Hexadecimal to Decimal: ')
# Typing 640 in octal to decimal somehow breaks it

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
if choice == '1':
    num = int(input('Decimal to Binary: Enter Number: '))
    print(binary(num))

elif choice ==  '2':
    num = input('Binary to Decimal: Enter Number: ')
    print(binary_to_decimal(num))
elif choice == '3':
    num = int(input('Decimal to Octal: Enter Number: '))
    print(octal(int(binary(num))))
elif choice == '4':
    num = int(input('Octal to Decimal: Enter Number: '))
    print(octal_to_decimal(num))
elif choice == '5':
    num = int(input('Decimal to Hexadecimal: Enter Number: '))
    print(hexadecimal(int(binary(num))))
elif choice == '6':
    num = input('Hexadecimal to Decimal: Enter Number: ')
    print(hexadecimal_to_decimal(num))
