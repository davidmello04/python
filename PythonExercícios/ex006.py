## n = int(input('Digite um valor: '))
## print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {}'.format(n, (n*2), (n*3), (n**(1/2))))

n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é {}. \nO triplo de {} é {}. \nA raiz quadrada de {} é {:.2f}'.format(n, d, n, t, n, r))
