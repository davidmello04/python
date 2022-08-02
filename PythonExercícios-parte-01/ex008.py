## medida = float(input('Digite uma medida para conversão: '))
## print('{} metros covertido em centímetros é igual a {} cm e convertido em milímetros é igual a {} mm'.format(medida, medida*100, medida*1000))

medida = float(input('Digite uma medida metros para conversão: '))
cm = medida * 100
mm = medida * 1000
km = medida * 0.001
print('{}m corresponde a {}km, a {}cm e a {}mm'.format(medida, km, cm, mm))
