situacao = dict()
situacao['nome'] = str(input('Nome: '))
situacao['media'] = float(input(f'Média de {situacao["nome"]}: '))
for k, v in situacao.items():
    print(f'{k} é igual a {v}')
if situacao['media'] <= 5:
    print(f'Situação é igual á Reprovado')
elif situacao['media'] <= 8:
    print('Situação é igual a Recuperação')
elif situacao['media'] >= 9:
    print('Situação é igual a Aprovado')
