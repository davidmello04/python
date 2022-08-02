salario = float(input('Qual é o salário do Funcionário? R$'))
novo = salario + (salario * 15 / 100)
print('O novo salário do Funcionário com aumento de 15% é R${:.2f}'.format(novo))
