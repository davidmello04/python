from datetime import date

print('-='*20)
print('Alistamento Militar')
print('-='*20)

ano = date.today().year

nascimento = int(input('Em qual ano você nasceu? '))
idade = ano - nascimento

print('Você tem {} anos!'.format(idade))

if idade >= 18:
    if idade == 18:
        print('É hora de se alistar!')
    else:
        print('Seu alistamento está atrasado em {} anos!'.format((idade - 18))) 
else:
    print('Ainda não é hora de se alistar, ainda faltam {} anos!'.format((18-idade)))

