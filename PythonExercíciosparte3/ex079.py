listavalores = []
cont = 1
while True:
    print('-' * 35)
    valor = int(input(f'Digite o {cont}º valor: '))

    while valor in listavalores:
        print('-' * 35)
        print('Valor repetido. Não é possível adicionar...')
        valor = int(input(f'Digite o {cont} valor: '))
    else:
        print('Adicionado com sucesso...')
        listavalores.append(valor)
    
    print('-' * 35)
    continuar = str(input('Deseja continuar? [S]/[N]: ')).strip().upper()

    while continuar not in ('N', 'S'):
        continuar = str(input('Opção inválida. Deseja continuar? [S]/[N]: ')).strip().upper()
    if continuar == 'N':
            break
    
    cont += 1

listavalores.sort()
print('-' * 35)
print(f'Você digitou os valores {listavalores}.')