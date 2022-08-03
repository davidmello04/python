preço = float(input('Digite o valor do produto: R$ '))
desconto = preço - (preço * 5 / 100)
print('O valor com 5 porcento de desconto é R${:.2f}'.format(desconto))
