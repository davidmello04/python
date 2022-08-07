for c in range(0, 6):
    print('Oi')
print('Fim')

for c in range(1, 7): # Vai de 1 até 6 / ignora o último
    print(c)
print('Fim')

for c in range(6, 0, -1): # Contagem inversa
    print(c)
print('Fim')

for c in range(0, 7, 2): # Contagem de 2 em 2
    print(c)
print('Fim')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f, p):
    print(c)
print('Fim')

for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('Fim')

s = 0 # Repete a estrutura somando
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n # Ou s = s + n
print('O somatório de todos os valores foi {}'.format(s))