maioridade = homens = mulhermenor = cont = 0

while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M]/[F] ')).upper().strip()
    print('-'*30)
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S]/[N] ')).upper().strip()
    if continuar == 'N':
        break
print('Cadastros encerrados...')
print(f'{cont} pessoas foram cadastradas.')
print(f'{maioridade} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulhermenor} mulheres menores de 20 anos foram cadastradas.')