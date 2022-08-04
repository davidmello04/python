print('-='*20)
print('Média Escolar')
print('-='*20)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

print('\033[34mSua média final foi {:.1f} !\033[m'.format(media))

if media < 5:
    print('\033[7;31mVocê foi reprovado!\033[m')
elif 7 > media >= 5:
    print('\033[7;33mVocê está na recuperação, estude mais!\033[m')
elif media >= 7:
    print('\033[7;32mPARABÉNS! Você foi aprovado!\033[m')