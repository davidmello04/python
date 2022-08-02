sal = float(input('Qual o salário do funcionário? R$: '))
if sal <= 1250:
  novo = sal + (sal * 15 / 1000)
else:
  novo = sal + (sal *10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, novo))

# SOlUÇÃO 02
'''a1 = sal + (sal * 10 / 100)
a2 = sal + (sal * 15 / 100)

if sal > 1250:
  print('O novo salário com aumento será R${:.2f}'.format(a1))
else:
  print('O novo salário com aumento será R${:.2f}'.format(a2))'''
