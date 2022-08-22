cont = total = maior = menor = media = 0
seguir = 'S'

while seguir in 'Ss':
    num = int(input('Digite um valor inteiro: '))
    total += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    seguir = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
media = total / cont
print('''A média entre todos os valores digitados é {:.1f}
O maior número digitado foi {}
O menor número digitado foi {}'''.format(media, maior, menor))