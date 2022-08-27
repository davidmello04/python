num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze',
'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

print('-' * 32 + f'\n{" NÚMERO POR EXTENSO ": ^32}\n' + '-' * 32)

while True:
    valor = int(input('Digite um número entre 0 e 20: '))
    while valor < 0 or valor > 20:
        valor = int(input('Por favor, digite um número entre 0 e 20: '))

    print(f'Você digitou o número {num[valor]}.')
    print('-' * 32)    

    continuar = str(input('Quer continuar? [S]/[N]: ')).upper()
    print('-' * 32)
    while continuar != 'S' and continuar != 'N':
        print('Opção inválida!')
        continuar = str(input('Quer continuar? [S]/[N]: ')).upper()
    if continuar == 'N':
        print('FIM DO PROGRAMA')
        break