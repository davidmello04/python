# O for é utilizado quando você sabe o limite
'''
for c in range(1, 10):
    print(c)
print('Fim')
'''

# O while é o usado quando você não sabe o limite e também quando sabe
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

# Condição de parada
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N]')).upper()
print('Fim')

n = 1
par = impar = 0 # Os dois recebem 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # Esse if serve para não contar o 0 como par
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))