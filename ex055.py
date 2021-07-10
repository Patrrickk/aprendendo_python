maior = menor = 0
for c in range(1, 6):
    peso = float(input(f'Pessoa {c}ª Qual é seu peso(kg): '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior} e o menor peso {menor}')
