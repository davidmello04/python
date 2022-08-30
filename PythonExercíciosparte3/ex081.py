listavalores = []
cont = 1

while True:
    listavalores.append(int(input(f'Digite o {cont}º valor: ')))
    print('-' * 35)

    continuar = str(input('Deseja continuar? [S]/[N]: ')).strip().upper()
    while continuar not in ('N', 'S'):
        continuar = str(input('Deseja continuar? [S]/[N]: ')).strip().upper()
    if continuar == 'N':
        print('-=' * 35)
        break
    print('-' * 35)

    cont += 1

print(f'Você digitou {len(listavalores)} números.')

listavalores.sort(reverse=True)
print(f'Lista na ordem decrescente: {listavalores}')

if 5 in listavalores:
    for pos, valor in enumerate(listavalores):
        if valor == 5:
            print(f'O valor 5 foi encontrado na lista na {pos}º posição.')
            break
else:
    print('O valor 5 não foi encontrado.')