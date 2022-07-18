print("""Faça um programa que leia uma frase e mostre:
1- Quantas vezes aparece a letra A
2- Em que posição ela aparece a primeira vez
3- Em que posição ela aparece a ultima vez""")

frase = str(input('\nDigite uma frase: ')).strip().upper()

print('\nQuantas vezes aparece a letra A: {}'.format(frase.count('A')))
print('Em que posição ela aparece a primeira vez: {}'.format(frase.find('A')))
print('Em que posição ela aparece a ultima vez: {}'.format(frase.rfind('A')))
