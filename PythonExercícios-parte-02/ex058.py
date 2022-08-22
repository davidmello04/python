from random import randint
print('-='*10)
print('Jogo da Adivinhação')
print('-='*10)
print('''Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi? ''')
computador = randint(0, 10)
acertou = False
jogadas = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    jogadas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('O número pensado foi {}.'.format(computador))
print('Você precisou de {} tentativas para acertar!'.format(jogadas))

# Solução 02
'''jogador = 0
jogadas = 0
while jogador != computador:
    jogador = int(input('Qual é seu palpite? '))
    jogadas += 1
print('O número pensado foi {}.'.format(computador))
print('Você precisou de {} tentativas para acertar!'.format(jogadas))'''
