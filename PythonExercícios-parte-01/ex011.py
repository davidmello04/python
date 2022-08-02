larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = area / 2
print('A sua parede possui {}m². Você irá utilizar {} litros de tinta para pintar a parede.'.format(area, tinta))
