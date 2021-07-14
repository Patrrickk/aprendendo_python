cedulas = 50
quant_50 = 0
quant_20 = 0
quant_10 = 0
quant_1 = 0
print(f'{" BANCO PK ":=^50}')
valor = int(input('Qual é o valor do saque? R$ '))
while True:
    if valor >= 50:
        quant_50 += 1
        valor -= cedulas
    else:
        cedulas = 20
        if valor >= 20:
            quant_20 += 1
            valor -= cedulas
        elif valor >= 10:
            cedulas = 10
            quant_10 += 1
            valor -= cedulas
        elif valor > 0:
            cedulas = 1
            quant_1 += 1
            valor -= cedulas
        elif valor == 0:
            break
if quant_50 > 0:
    print(f'Total de {quant_50} Cédulas de R$50')
if quant_20 > 0:
    print(f'Total de {quant_20} Cédulas de R$20')
if quant_10 > 0:
    print(f'Total de {quant_10} Cédulas de R$10')
if quant_1 > 0:
    print(f'Total de {quant_1} Cédulas de R$1')
print(f'FIM')
