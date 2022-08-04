from sqlite3 import paramstyle


print('-='*30)
print('Aprovação de empréstimo bancário para a compra da sua casa!')
print('-='*30)

valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador? R$'))
parcelas = int(input('Quantos anos de financiamento? '))

parcelamento = valorcasa / (parcelas * 12)
mínimo = (salario * 30 / 100)

print('\033[34mPara pagar uma casa de R${:.2f} em {} anos\033[m'.format(valorcasa, parcelas), end='')
print('\033[34m a parcela será de R${:.2f}\033[m'.format(parcelamento))
if parcelamento <= mínimo:
    print('\033[32mEmpréstimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[31mInfelizmente o empréstimo foi NEGADO!\033[m')