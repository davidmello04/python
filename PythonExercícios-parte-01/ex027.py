print('Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separademente')

nome = str(input('Digite seu nome completo: ')).strip().lower().title().split()

print('O primeiro nome é: {}'.format(nome[0]))
print('O último nome é: {}'.format(nome[len(nome)-1]))
