from datetime import date
ano = date.today().year

print('-='*20)
print('Categorias de Natação')
print('-='*20)

nascimento = int(input('Ano de nascimento: '))
idade = ano - nascimento

print('O atleta tem {} anos!'.format(idade))

if idade <= 9:
    print('Sua categoria é \033[34mMIRIM!\033[m')
elif idade <= 14:
    print('Sua categoria é \033[34mINFANTIL!\033[m')
elif idade <= 19:
    print('Sua categoria é \033[34mJUNIOR!\033[m')
elif idade <= 25:
    print('Sua categoria é \033[34mSÊNIOR!\033[m')
else:
    print('Sua categoria é \033[34mMASTER\033[m')