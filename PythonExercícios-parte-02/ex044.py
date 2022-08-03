print('-='*20)
print('- Valor a ser Pago -')
print('-='*20)

valor = float(input('Digite o valor a ser pago: R$'))
print('Opções de Pagamento: \n1 - À vista - Dinheiro ou Cheque | Desconto de 10% \n2 - Cartão | Desconto de 5% \n3 - Cartão 2x | Valor normal \n4 - Cartão 3x ou mais | Juros de 20%')
pagamento = int(input('Digite o número da opção de pagamento: '))

if pagamento == 1:
    print('\033[32mO valor total a vista é de R${:.2f}\033[m'.format(valor - (valor * 10 / 100)))
elif pagamento == 2:
    print('\033[32mO valor total no cartão é de R${:.2f}\033[m'.format(valor - (valor * 5 / 100)))
elif pagamento == 3:
    print('\033[32mO valor total no cartão em 2x é de R${}\033[m'.format(valor))
elif pagamento == 4:
    print('\033[32mO valor total no cartão em 3x é de R${}\033[m'.format(valor + (valor * 20 / 100)))
else:
    print('\033[31mEsta opção não existe, por favor selecionar uma das opções listadas acima!\033[m')