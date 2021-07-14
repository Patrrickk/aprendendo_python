cedula = 50
quant_cedulas = 0
valor = int(input('Valor do saque? '))
while True:
    if valor >= cedula:
        quant_cedulas += 1
        valor -= cedula
    else:
        print(f'Total de R${quant_cedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        quant_cedulas = 0
        if valor == 0:
            break

