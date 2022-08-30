num = [5, 1, 9, 7]
num[2] = 6 #Listas são mutáveis

num.append(2) #Adicionando elemento
num.sort() #Colocando em ordem
#num.sort(reverse=True)
num.insert(2, 0) #Inserir um valor na lista

num.pop() #Elimina o último elemento
num.pop(2) #Elimina o item do índice selecionado
num.remove(2) #Elimina o primeiro valor (2) da lista
if 5 in num:
    num.remove(5)
else:
    print('Não achei o valor 5')

print(num)
print(f'Essa lista tem {len(num)} elementos.')


valores = []
valores.append(4)
valores.append(7)
valores.append(2)

for v in valores:
    print(f'{v}...')

for c, v in enumerate(valores):
    print(f'Na posisão {c} encontrei o valor {v}!')

numeros = list()
for cont in range(0, 5):
    numeros.append(int(input('Digite um valor: ')))
for c, v in enumerate(numeros):
    print(f'Na posisão {c} encontrei o valor {v}!')


a = [2, 7, 4, 3]
#b = a #Faz uma ligação
b = a[:] #Faz uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')