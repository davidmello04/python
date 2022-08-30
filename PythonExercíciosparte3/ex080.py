listavalores = []

for cont in range(5):
    valor = int(input(f'Digite o {cont + 1}º valor: '))

    while valor in listavalores:
        print('-' * 50)
        print('Valor repetido. Não é possível adicionar...')
        valor = int(input(f'Digite o {cont + 1}º valor: '))

    
    if len(listavalores) == 0 or valor > max(listavalores):
        listavalores.append(valor)
        print(f'O {cont + 1}º valor foi adicionado no final da lista...')
        print('-' * 50)

    for pos, v in enumerate(listavalores):
        if valor < v:
            listavalores.insert(pos, valor)
            print(f'O valor foi adicionado na {pos}º posição.')
            print('-' * 50)
            break

print(f'Você adicionou os valores {listavalores}')