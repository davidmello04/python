from random import shuffle

print('- SORTEIO -')
nome1 = str(input('Qual o primeiro aluno? '))
nome2 = str(input('Qual o segundo aluno? '))
nome3 = str(input('Qual o terceiro aluno? '))
nome4 = str(input('Qual o quarto aluno? '))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
