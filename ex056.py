quant_p = soma_idade = 0
maior = 0
mulheres_menos_20 = 0
homem_velho = ''
for c in range(1, 3):
    quant_p += 1
    nome = str(input('Seu nome?: '))
    idade = int(input('Qual é sua idade: '))
    sexo = str(input('Qual é seu sexo? [M/F]: ')).strip().lower()
    if sexo[0] == 'm':
        if idade > maior:
            maior = idade
            homem_velho = nome
    if sexo[0] == 'f':
        if idade < 20:
            mulheres_menos_20 += 1
    soma_idade += idade
print(f'A média de idade é {soma_idade / quant_p}')
print(f'O homem mais velho é o {homem_velho} e sua idade é {maior} anos')
print(f'Tem {mulheres_menos_20} mulheres com menos de 20 anos')
