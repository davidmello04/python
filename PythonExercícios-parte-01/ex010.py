print('Seja bem-vindo ao nosso conversor!')
real = float(input('Por favor digite quantos R$ você tem? '))
dolar = real / 5.39
print('- Conversão em US$-Dólar -\nCom R${} você poderá comprar US${:.2f}'.format(real, dolar))
