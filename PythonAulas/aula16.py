lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#Tuplas são imutáveis
#print(lanche[-2:])

for comida in lanche:
    print(f'Eu vou comer {comida} ')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi demais!')

print(sorted(lanche)) #Em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) #Não soma valores, apenas junta.
print(c.count(5))#Conta
print(c.index(4))#Indica a posição