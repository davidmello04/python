from datetime import date

print('-='*20)
print('Alistamento Militar')
print('-='*20)

ano = date.today().year

sexo = int(input('''Qual o seu sexo:
[ 1 ] Masculino
[ 2 ] Feminino
Digite 1 ou 2 para escolher: '''))

if sexo == 1:
    print('Você tem que fazer o alistamento militar obrigatório.')
    nascimento = int(input('Ano de nascimento: '))
    idade = ano - nascimento

    print('Você tem {} anos em {}.'.format(idade, ano))

    if idade >= 18:
        if idade == 18:
            print('É hora de se alistar!')
        else:
            saldo = idade - 18
            print('Seu alistamento está atrasado, você deveria ter se alistado há {} anos!'.format((saldo)))
            anoalistamento = ano - saldo
            print('Seu alistamento foi em {}'.format(anoalistamento))
    else:
        saldo = 18 - idade
        print('Ainda não é hora de se alistar, ainda faltam {} anos para o alistamento!'.format((saldo)))
        anoalistamento = ano + saldo
        print('Seu alistamento será em {}'.format(anoalistamento))
elif sexo == 2:
    print('Você não precisa fazer alistamento militar obrigatório.')
else:
    print('Opção inválida.')