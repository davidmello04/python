maiorIdadeHomem = 0
menorIdadeMulher = 0
somaIdade = 0
mediaIdade = 0
maisVelho = str

for p in range(1, 5):
    print( '----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        maisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        maisVelho = nome
    if sexo in 'Ff' and idade < 18:
        menorIdadeMulher += 1


mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, maisVelho))
print('Ao todo são {} mulheres com menos de 18 anos'.format(menorIdadeMulher))