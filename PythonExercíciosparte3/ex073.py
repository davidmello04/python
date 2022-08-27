times = ('Palmeiras', 'Fluminense', 'Flamengo', 'Vasco', 'Corinthians', 'Atlético-MG', 'Athletico', 'Internacional', 'São Paulo', 'Santos',
'Fortaleza', 'Bragantino', 'América-MG', 'Botafogo', 'Ceará', 'Goiás', 'Atlético-GO', 'Coritiba', 'Avaí', 'Juventude')

print('=' * 32 + f'\n{" TABELA DO BRASILEIRÃO ": ^32}\n' + '=' * 32)

print('-' * 32)
print(f'Lista de times do Brasileirão: {times}')
print('-' * 32)

print('Os 5 primeiros colocados do campeonato são:')
print('-' * 32)
cont = 0
for pos in range(0, 5):
    cont += 1
    print(f'{cont} - {times[pos]}')
print('-' * 32)

print('O 4 últimos colocados do campeonato são:')
print('-' * 32)
cont2 = 16
for pos in range(16, 20):
    cont2 += 1
    print(f'{cont2} - {times[pos]}')
print('-' * 32)

print(f'Times em Ordem Alfabética: {sorted(times)}')
print('-' * 32)

print(f'Posição do Vasco: {times.index("Vasco") + 1}º Posição.')
print('-' * 32)


#SOLUÇÃO 02
'''
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'O Vasco está na posição {times.index("Vasco") + 1}º posição.')
print('-=' * 15)
'''