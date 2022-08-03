print('-='*20)
print('Cálculo de Índice de Massa Corporal - IMC -')
print('-='*20)

peso = float(input('Digite o seu peso Kg: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)

print('\033[34mO seu IMC é {:.1f} !\033[m'.format(imc))
if imc < 18.5:
    print('\033[31mVocê está abaixo do peso!\033[m')
elif imc >= 18.5 and imc <= 25:
    print('\033[32mVocê está no peso ideal!\033[m')
elif imc > 25 and imc <= 30:
    print('\033[31mVocê está com sobrepeso!\033[m')
elif imc > 30 and imc <= 40:
    print('\033[31mVocê está com obesidade!\033[m')
elif imc > 40:
    print('\033[31mVocê está com obesidade mórbida!\033[m')