from datetime import date

ano_atual = date.today().year
maioridade = 0
menoridade = 0
idade = 0

for pessoa in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = ano_atual - ano
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1

print('{} pessoas atingiram a maioridade e {} pessoas ainda não atigiram.'.format(maioridade, menoridade))
