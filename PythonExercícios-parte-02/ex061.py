print('Gerador de PA')
print('-='*10)

primeiro = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} --> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')