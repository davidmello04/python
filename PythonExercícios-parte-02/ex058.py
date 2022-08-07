from random import randint
computador = randint(0, 10)
jogador = 0
jogadas = 0
while jogador != computador:
    jogador = int(input('Digite um valor: '))
    jogadas += 1
print('O número pensado foi {}.'.format(computador))
print('Você precisou de {} tentativas para acertar!'.format(jogadas))
