from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
cont = 0

while True:
    opçao = int(input('''Você escolhe:
    [1] PAR
    [2] ÍMPAR
    Qual sua opção? '''))
    computador = randint(0, 10)
    jogador = int(input('Qual número você escolhe? '))
    soma = computador + jogador
    if opçao == 1 and soma % 2 == 0:
        print(f'A soma foi {soma} e é par.')
        print('Parabéns, você venceu!')
        print('Vamos jogar novamente...')
        cont += 1
    elif opçao == 1 and soma % 2 != 0:
        print(f'A soma foi {soma} e é ímpar.')
        if cont == 0:
            print(f'GAME OVER, você perdeu!')
        else:
            print(f'GAME OVER, você perdeu! Mas conseguiu {cont} vitórias consecultivas.')
        break
    elif opçao == 2 and soma % 2 != 0:
        print(f'A soma foi {soma} e é ímpar.')
        print('Parabéns, você venceu!')
        print('Vamos jogar novamente...')
        cont += 1
    elif opçao == 2 and soma % 2 == 0:
        print(f'A soma foi {soma} e é par.')
        if cont == 0:
            print(f'GAME OVER, você perdeu!')
        else:
            print(f'GAME OVER, você perdeu! Mas conseguiu {cont} vitórias consecultivas.')
        break