print('-='*4)
print('TABUADA')
print('-='*4)

num = int(input('Digite um número ver a tabuada? '))
multiplicaçao = 0

print('-=' * 6)

for c in range(1, 11):
    multiplicaçao = num * c
    print('{} x {:2} = {}'.format(num, c, multiplicaçao))

print('-=' * 6)

'''
for c in range(1, 11):
    num = int(input('Digite um número ver a tabuada? '))
    print('{} x {:2} = {}'.format(num, c, num*c))
'''