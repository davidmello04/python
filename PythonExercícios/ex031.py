dis = float(input('Qual a distância da sua viagem em km: '))
print('Você está prestes a começar uma viagem de {}km.'.format(dis))
if dis <= 200:
  preço = dis * 0.50
else:
  preço = dis * 0.45
print('O preço da sua passagem será de R${:.2f}.'.format(preço))
