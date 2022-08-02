num = int(input('Digite um número qualquer: '))
par = num % 2
if par == 0:
  print('O seu número {} é par.'.format(num))
else:
  print('O seu número {} é ímpar.'.format(num))