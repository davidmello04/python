print('Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados')

numero = str(input('Digite um número de 0 a 9999: ')).zfill(4)

print('unidade: {}'.format(numero[3]))
print('dezena: {}'.format(numero[2]))
print('centena: {}'.format(numero[1]))
print('milhar: {}'.format(numero[0]))
