print('-='*37)
print('A soma dos números ímpares que são multiplos de 3 no intervalo de 1 a 500')
print('-='*37)

soma = 0
quat = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        quat += 1

print('Foram encontrados {} números e a soma de todos é {}.'.format(quat, soma))