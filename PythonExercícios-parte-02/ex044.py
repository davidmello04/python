print('{:=^40}'.format('LOJA - ART PARADISE'))

valor = float(input('Digite o valor total das compras: R$'))
print('''Opções de Pagamento:
[ 1 ] - À vista - Dinheiro ou Cheque | Desconto de 10%
[ 2 ] - Cartão | Desconto de 5%
[ 3 ] - Cartão 2x | Valor normal
[ 4 ] - Cartão 3x ou mais | Juros de 20%''')

pagamento = int(input('Digite a opção de pagamento: '))

if pagamento == 1:
    total = valor - (valor * 10 / 100)
    print('\033[32mO valor total a vista é de R${:.2f}.\033[m'.format(total))
elif pagamento == 2:
    total = valor - (valor * 5 / 100)
    print('\033[32mO valor total no cartão é de R${:.2f}.\033[m'.format(total))
elif pagamento == 3:
    total = valor / 2
    print('\033[32mSua compra será parcelada em 2x de R${} SEM JUROS.\033[m'.format(total))
elif pagamento == 4:
    total = valor + (valor * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    parcelamento = total / parcelas
    print('\033[32mSua compra será parcelada em {}x de R${:.2f} COM JUROS.\033[m'.format(parcelas, parcelamento))
    print('Sua compra de R${:.2f} vai custar R${:.2f} com o juros.'.format(valor, total))
else:
    print('\033[31mOpção de pagamento inválida, tente novamente!\033[m')