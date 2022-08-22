num = 0
cont = 1
while True:
    print('-'*30)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if num < 0:
        break
    while cont <= 10:
        print(f'{num} x {cont} = {num*cont}')
        cont += 1
    cont = 1    
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!' )