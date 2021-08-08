nome = dict()
nome['nome'] = str(input('Nome: '))
nome['media'] = float(input(f'Média de {nome["nome"]}: '))
if nome['media'] <= 4:
    nome['Situação'] = 'Reprovado'
elif nome['media'] <= 6:
    nome['Situação'] = 'Recuperação'
elif nome['media'] >= 7:
    nome['Situação'] = 'Aprovado'
print('=' * 20)
for k, v in nome.items():
    print(f' - {k} é igual a {v}')
