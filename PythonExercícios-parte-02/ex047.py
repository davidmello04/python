print('-='*22)
print('Os números pares entre 1 e 50 são:')
print('-='*22)

for c in range(2, 51, 2): # Possibilidade com um menor número de interações
    print(c, end=' ')
print('Fim')

'''
for c in range(1, 51):
    if c % 2 == 0:
        print(c)
print('Fim')
'''