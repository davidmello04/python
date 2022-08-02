vel = float(input('Qual a velocidade do carro? km\h: '))
multa = (vel - 80) * 7
if vel > 80:
  print('MULTADO! Você ultrapassou a velocidade permitida que é de 80km\h e recebeu uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
