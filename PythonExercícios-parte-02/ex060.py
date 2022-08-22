num = int(input('Digite um número para ver seu fatorial: '))
cont = num
fat = 1
print('Calculando {}!'.format(num))
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont # fat = fat * cont
    cont -= 1 # cont = cont - 1
print('{}'.format(fat))

# Solução 02
'''from math import factorial
n = int(input('Digite um número para ver seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''