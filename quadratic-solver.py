a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
d = (b**2 - 4*a*c)**(1/2)

x1 = (-b + d)/2
x2 = (-b - d)/2
print('First root (+):',x1,'And second root:',x2)