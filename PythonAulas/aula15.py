n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}.')



# OBS: EVOLUÇÃO DO PRINT
nome = 'Mario'
idade = 20
salario = 987.55
print(f'O {nome} tem {idade} anos e recebe R${salario:.2f}.') # PYTHON 3.6
print('O {} tem {} anos e recebe R${}.'.format(nome, idade, salario)) # PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) # PYTHON 2