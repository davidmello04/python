maior = 0
menor = 0

for pessoas in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}Kg'.format(maior))
print('O menor peso foi {}Kg'.format(menor))


# Segunda forma de executar
'''
maior = 0
menor = 1000

for pessoas in range(1, 6):
    peso = float(input('Qua o peso da {}ª pessoa? '.format(pessoas)))
    if peso > maior:
        maior = peso
        if peso < menor:
            menor = peso
print('Peso menor {} e peso maior {}'.format(menor, maior))
'''