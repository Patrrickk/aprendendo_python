maior = menor = 0
for c in range(1, 6):
    peso = float(input('Qual é seu peso(kg): '))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    else:
        menor = peso
print(f'O maior peso é {maior} e o menor peso {menor}')
