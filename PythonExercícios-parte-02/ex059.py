from time import sleep
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
cont = 0
while cont != 5:
    print('''--- MENU ---
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    cont = int(input('Digite sua opção: '))
    print('Os valores digitados foram {} e {}'.format(valor1, valor2))
    if cont == 1:
        soma = valor1 + valor2
        print('A soma entre os valores é {}'.format(soma))
    elif cont == 2:
        mult = valor1 * valor2
        print('A multiplicação entre os valores é {}'.format(mult))
    elif cont == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('O maior número é {}'.format(maior))
    elif cont == 4:
        print('Informe os novos números.')
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite outro valor: '))
    elif cont == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    sleep(2)
print('Fim do programa! Volte sempre!')