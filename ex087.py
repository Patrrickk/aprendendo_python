valores = [[], [], []]
pares = soma_t = 0
for c in range(0, 9):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        pares += n
    if c < 3:
        valores[0].append(n)
    elif c <= 5:
        valores[1].append(n)
    elif c <= 9:
        valores[2].append(n)
print('=' * 60)
for c in range(0, 3):
    soma_t += valores[c][2]
    print(f'[ {valores[c][0]:^4} ]', end='')
    print(f'[ {valores[c][1]:^4} ]', end='')
    print(f'[ {valores[c][2]:^4} ]\n', end='')
print('=' * 60)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma_t}')
print(f'O maior valor da segunda linha é {max(valores[1])}')
