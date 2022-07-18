print('Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome')

nome = str(input('Qual o seu nome? ')).strip().lower().title()
print(nome)
print('Silva' in nome)
