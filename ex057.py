sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Erro de digitação, por favor, informe seu sexo: ')).upper().strip()
print(f'SEXO [{sexo}] CADASTRADO COM SUCESSO')
