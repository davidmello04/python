print('Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.')

soma = 0
quat = 0

for c in range(1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        quat += 1
print('Você informou {} números PARES e a soma foi {}'.format(quat, soma))