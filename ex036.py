valor_casa = float(input('Qual é o valor do imóvel? '))
salario = float(input('E qual é o valor do seu salário? '))
ano = int(input('Em quantos anos quer pagar? '))
limite_30 = salario * 30 / 100
valor_prestac = valor_casa / ano
if valor_prestac > limite_30:
    print(f'Infelizmente seu empréstimo foi \033[1;91mNEGADO!\033[m')
else:
    print(f'Seu empréstimo acaba de ser \033[1;92mAPROVADO!\033[m \nFicando com parcelas mensais no valor de '
          f'\033[1;92mR$ {valor_prestac:.2f}\033[m')
print('Tenha um bom dia!')
