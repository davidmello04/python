total = maisdemil = menor = cont = 0
barato = ' '
while True:
    print('-'*30)
    print('LOJA SUPER MAKRO')
    print('-'*30)
    produto = str(input('Nome do produto: '))
    valor = int(input('Preço: R$'))
    total += valor
    cont += 1
    if valor > 1000:
        maisdemil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S]/[N]: ')).upper().strip()[0]
    if continuar in 'N':
        break

print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {maisdemil} produtos custando mais de R$1.000.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
print('{:-^40}'.format(' FIM DO PROGRAMA '))