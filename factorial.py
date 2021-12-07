def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    else:
        return 1
ans = factorial(int(input('Enter number: ')))
if ans > 10**5:
    ans = str(ans)
    ans = ans[0] +'.' + ans[1:5] + ' x 10^' + str(len(ans) -1)
print(ans)
