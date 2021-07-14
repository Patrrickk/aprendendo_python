maioridade = homens = mulheres_20 = 0
while True:
    idade = str(input('Quantos anos você tem? '))
    while idade.isnumeric() is not True:
        idade = str(input('Erro, tente novamente, Quantos anos você tem? '))
    idade = int(idade)
    if idade >= 18:
        maioridade += 1
    sexo = ' '
    while sexo.isalpha() is not True:
        sexo = str(input('Qual é seu sexo? [F/M] ')).strip().upper()
        while sexo != 'F' and sexo != 'M':
            sexo = str(input('Dados inválidos, tente mais uma vez, Qual é seu sexo? [F/M] ')).strip().upper()
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres_20 += 1
    stop = str(input('Quer continuar [S/N]')).upper().strip()
    while stop.isalpha() is not True:
        while stop != 'S' and stop != 'N':
            stop = str(input('Quer continuar [S/N]')).upper().strip()
    if stop == 'N':
        break
    print(f'{" CADASTRAR OUTRA PESSOA ":=^50}')
print(f'Ao todo foram cadastrados {maioridade} pessoas com mais de 18 anos')
print(f'Foram {homens} homens cadastrados e {mulheres_20} mulheres com menos de 20 anos')
