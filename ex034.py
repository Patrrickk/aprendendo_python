salario = float(input('Qual é seu salário: '))
if salario >= 1250:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)
print(f'Seu novo salário passa a ser R${aumento}')
