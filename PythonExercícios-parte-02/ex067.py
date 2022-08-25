while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num*cont}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')


#Solução 02

'''
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if num < 0:
        break
    while cont <= 10:
        print(f'{num} x {cont} = {num*cont}')
        cont += 1
    cont = 1
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')'''