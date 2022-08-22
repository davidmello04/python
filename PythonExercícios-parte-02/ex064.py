num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
print('Foram digitados {} números e a soma entre eles é {}, desconsiderando o 999.'.format(cont, soma))