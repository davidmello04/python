from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('-='*20)
print('JOKENPO - PEDRA, PAPEL E TESOURA')
print('-='*20)

print('''Começou!
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura''')

jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('\033[34m-=\033[m'*11)
print('\033[34mComputador jogou {}\033[m'.format(itens[computador]))
print('\033[34mVocê jogou {}\033[m'.format(itens[jogador]))
print('\033[34m-=\033[m'*11)

if computador == 0: # Pedra
    if jogador == 0:
        print('\033[33mEMPATE!\033[m')
    elif jogador == 1:
        print ('\033[32mVOCÊ VENCEU!!!\033[m')
    elif jogador == 2:
        print ('\033[31mCOMPUTADOR VENCEU!\033[m')
    else:
        print('Jogada Inválida!')

elif computador == 1: # Papel
    if jogador == 1:
        print('\033[33mEMPATE!\033[m')
    elif jogador == 2:
        print ('\033[32mVOCÊ VENCEU!!!\033[m')
    elif jogador == 0:
        print ('\033[31mCOMPUTADOR VENCEU!\033[m')
    else:
        print('Jogada Inválida!')

elif computador == 2: # Tesoura
    if jogador == 2:
        print('\033[33mEMPATE!\033[m')
    elif jogador == 0:
        print ('\033[32mVOCÊ VENCEU!!!\033[m')
    elif jogador == 1:
        print ('\033[31mCOMPUTADOR VENCEU!\033[m')
    else:
        print('Jogada Inválida!')