from datetime import date

print('-='*20)
print('Categorias de Natação')
print('-='*20)

ano = date.today().year

nascimento = int(input('Qual o ano que você nasceu? '))
idade = ano - nascimento

print('Você tem {} anos!')

if idade <= 9:
    print('Sua categoria é a \033[34mMIRIM!\033[m')
elif idade > 9 and idade <= 14:
    print('Sua categoria é a \033[34mINFANTIL!\033[m')
elif idade > 14 and idade <= 19:
    print('Sua categoria é a \033[34mJUNIOR!\033[m')
elif idade > 19 and idade <= 20:
    print('Sua categoria é a \033[34mSÊNIOR!\033[m')
else:
    print('Sua categoria é a \033[34mMASTER\033[m')