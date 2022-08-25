from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
cont = 0

while True:
    computador = randint(0, 11)
    jogador = int(input('Qual número você escolhe? '))
    soma = computador + jogador
    opçao = int(input('''Você escolhe:
    [1] PAR
    [2] ÍMPAR
    Qual sua opção? '''))
    print(f'O computador escolheu {computador} e você escolheu {jogador}.')
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


# SOLUÇÃO 02
'''v = 0
while True:
    jogador = int('Digite um valor')
    computador = randint(1, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI'
        tipo = str(input('Par ou ímpar? ')).strip().upper()
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end='')
    print('Deu Par' if total % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')'''