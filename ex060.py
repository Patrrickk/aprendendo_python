print('Utilizando WHILE')
c = int(input('Digite um número: '))
co = c
print(f'O fatorial de {c}! é ')
while c >= 2:
    print(f'{c}', end=' x ')
    c -= 1
    co *= c
print(f'1 = {co}')
print('Utilizando FOR')
fat = int(input('Digite um número: '))
soma = fat
co = fat
print(f'O fatorial de {fat}! é ')
for c in range(fat, 1, -1):
    print(f'{c}', end=' x ')
    soma -= 1
    co *= soma
print(f'1 = {co}')
