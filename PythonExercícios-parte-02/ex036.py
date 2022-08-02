print('-='*30)
print('Aprovação de empréstimo bancário para a compra da sua casa!')
print('-='*30)

valorcasa = float(input('Qual o valor da casa desejada? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
parcelas = float(input('Em quantos anos você deseja fazer o parcelamento? '))

parcelamento = 12 * parcelas

if valorcasa / parcelamento <= (salario * 30 / 100):
    print('Parabéns! Seu empréstimo foi APROVADO!')
    print('O seu parcelamento será de R${:.2f}'.format(valorcasa / parcelamento))
else:
    print('Infelizmente o seu empréstimo não foi aprovado!')
    print('O seu parcelamento seria de R${:.2f}'.format(valorcasa / parcelamento))