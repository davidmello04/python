print('Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com santo')

cidade = str(input('Digite o nome da cidade: ')).strip().lower().title()
print(cidade)
print('Santo' in cidade[:5])
