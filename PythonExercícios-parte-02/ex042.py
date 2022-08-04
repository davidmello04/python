print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Primeiro seguimento: '))
r3 = float(input('Primeiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    if r1 == r2 == r3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES.')
    elif r1 != r2 != r3 != r1:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')