import random

print('- SORTEIO -')
nome1 = str(input('Qual o primeiro nome? '))
nome2 = str(input('Qual o segundo nome? '))
nome3 = str(input('Qual o terceiro nome? '))
nome4 = str(input('Qual o quarto nome? '))

lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('A ordem da lista é: {}'.format(lista))
