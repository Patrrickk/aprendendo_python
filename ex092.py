from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = date.today().year - int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = 35 + (dados['idade'] - (date.today().year - dados['contratação']))
print('-' * 40)
for k, v in dados.items():
    print(f' - {k.upper()} tem o valor {v}')
