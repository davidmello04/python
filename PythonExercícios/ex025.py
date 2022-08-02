print('Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome')

nome = str(input('Qual o seu nome completo? ')).strip().lower().title()
print(nome)
print('Seu nome tem Silva? {}'.format('Silva' in nome))
