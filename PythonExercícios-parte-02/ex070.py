total = maisdemil = maisbarato = cont = 0
while True:
    print('-'*30)
    print('LOJA SUPER MAKRO')
    print('-'*30)
    produto = str(input('Nome do produto: '))
    valor = int(input('Preço: R$'))
    total += valor
    maisbarato = valor
    if valor > 1000:
        maisdemil += 1
    if valor < maisbarato:
        maisbarato = valor
    continuar = str(input('Quer continuar? [S]/[N]: ')).upper().strip()[0]
    if continuar in 'N':
        break
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {maisdemil} produtos custando mais de R$1.000.')
print('FIM')