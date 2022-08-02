from random import randint
from time import sleep

numero = randint(0,5)

print('-=-' * 20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

chute = int(input('Em qual número pensei? '))
print('PROCESSANDO...')
sleep(3) # O computador aguarda um pouco para dar o resultado

if chute == numero:
  print('PARABÉNS! Você acertou!')
else:
  print('QUE PENA! Você errou! O número pensado foi {} e não o {}.'.format(numero, chute))
