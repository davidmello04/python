print('-='*20)
print('Conversão de bases númericas')
print('-='*20)

valor = int(input('Digite um número para conversão: '))
base = str(input('Para qual a base númerica você deseja converter? '))

if base == binário:
    print('O resultado da conversão de {} para binário é {}'.format(valor, (valor)))