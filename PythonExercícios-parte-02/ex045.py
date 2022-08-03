from random import choice

print('-='*20)
print('JOGO - PEDRA, PAPEL E TESOURA')
print('-='*20)

print('Começou!')
print('1 - Pedra \n2 - Papel \n3 - Tesoura')
escolha = str(input('Digite a opção escolhida: '))

a = 'pedra'
b = 'papel'
c = 'tesoura'

sorteio = [a, b, c]
resultado = choice(sorteio)

print('\033[34mO computador escolheu {} e você {}.\033[m'.format(resultado, escolha))

if  escolha == a and resultado == c or escolha == b and resultado == a or escolha == c and resultado == b:
    print('\033[32mParabéns, você ganhou!\033[m')
elif escolha == a and resultado == a or escolha == b and resultado == b or escolha == c and resultado == c:
    print('\033[33mEmpate!\033[m')
elif escolha == a and resultado == b or escolha == b and resultado == c or escolha == c and resultado == a:
    print('\033[31mVocê perdeu!\033[m')