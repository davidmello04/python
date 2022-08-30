listavalores = []
listapar = []
listaimpar = []
cont = 1

while True:
    listavalores.append(int(input(f'Digite o {cont}º valor: ')))

    contin = str(input('Deseja continuar? [S]/[N]: ')).strip().upper()
    while contin not in ('S', 'N'):
        contin = str(input('Opção inválida. Deseja continuar? [S]/[N]: ')).strip().upper()
    if contin == 'N':
        print('-=' * 40)
        break
    print('-' * 40)

    cont += 1

for v in listavalores:
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)

print(f'Você digitou os números: {listavalores}.')
print(f'Os números pares são: {listapar}')
print(f'Os números ímpares são: {listaimpar}')