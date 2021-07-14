valores = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
           int(input('Digite mais valor: ')), int(input('Digite o último valor: ')))
posi = 0
print(f'O valor 9 apareceu {valores.count(9)} vezes')
print('Os valores pares digitados foram ', end='')
for pos, c in enumerate(valores):
    if c == 3:
        posi = pos + 1
    if c % 2 == 0:
        print(c, end=' ')
if posi > 0:
    print(f'\nO número 3 apareceu na posição {posi}')
else:
    print('\nO valor 3 não foi digitado em nenhuma posição')
