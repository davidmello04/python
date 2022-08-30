valores = [int(input(f'Informe o valor da posição {cont}º: ')) for cont in range(5)]

print(f'Você digitou os valores {valores}')

for c, v in enumerate(valores):
    if v == max(valores):
        print(f'O maior valor foi o {max(valores)} que está na {c}º posição.')

for c, v in enumerate(valores):
    if v == min(valores):
        print(f'O menor valor foi o {min(valores)} que está na {c}º posição')