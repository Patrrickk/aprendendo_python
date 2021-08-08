dados = dict()
grupro = list()
soma = quant = 0
while True:
    nome = str(input('Nome: '))
    while nome.isalpha() is not True:
        nome = str(input('For favor, apenas letras! Nome: '))
    dados['nome'] = nome
    sexo = ''
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
        if sexo != 'M' and sexo != 'F':
            print(f'ERRO! Por favor {dados["nome"]}, digite apenas M ou F.')
    dados['sexo'] = sexo
    idade = str(input('Idade: ')).strip()
    while idade.isnumeric() is not True:
        idade = str(input(f'{dados["nome"]}, digite apenas números! por gentileza, Idade: '))
        if idade.isalpha():
            print('Apenas números meu nobre companheiro')
    dados['idade'] = int(idade)
    soma += dados['idade']
    stop = ''
    while stop != 'S' and stop != 'N':
        stop = str(input('Quer continuar? [S/N]: ')).upper().strip()
        if stop != 'S' and stop != 'N':
            print('ERRO! Responda apenas S ou N.')
    grupro.append(dados.copy())
    dados.clear()
    if stop == 'N':
        break
print(f'A) O grupo tem {len(grupro)} pessoas cadastradas.')
media = soma / len(grupro)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram:', end=' ')
for f in grupro:
    if f['sexo'] == 'F':
        print(f'{f["nome"]}', end=' ')
print()
print('D) Lista de pessoa que estão acima da média:')
for p in grupro:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'  {k}; {v}', end=' ')
        print()
print('<<< ENCERRADO >>>')
