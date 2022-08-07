print('Faça um programa que leia o primeiro termo e a razão de uma PA. no final, mostre os 10 primeiros termos\ndessa progressão.')

a = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão: '))
termo_geral = a + (10 - 1) * r # Formula para calcular o termo - décimo termo

for c in range(a, termo_geral+1, r):
    print(c , end=' -> ')
print('ACABOU')