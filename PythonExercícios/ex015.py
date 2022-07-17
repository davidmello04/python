dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))
valor = (dias * 60) + (km * 0.15)
print('O valor total a pagar é R${:.2f}'.format(valor))
