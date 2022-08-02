a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))

#SOLUÇÃO 01 - CÓDIGO MENOR

menor = a
if b < a and b < c:
  menor = b
if c < a and c < b:
  menor = c

maior = a
if b > a and b > c:
  maior = b
if c > a and c > b:
  maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))         

# SOLUÇÃO 02
'''if a > b and a > c:
  print('O maior número é {}.'.format(a))
  if b > c:
    print('O menor número é {}.'.format(c))
  else:
    print('O menor número é {}.'.format(b))

elif b > a and b > c:
  print('O maior número é {}.'.format(b))
  if a > c:
    print('O menor número é {}.'.format(c))
  else:
    print('O menor número é {}.'.format(a))

elif c > a and c > b:
  print('O maior número é {}.'.format(c))
  if a > b:
    print('O menor número é {}.'.format(b))
  else:
    print('O menor número é {}.'.format(a))'''
