valores = [[], [], []]
for c in range(0, 9):
    n = int(input('Digite um número: '))
    if c < 3:
        valores[0].append(n)
    elif c <= 5:
        valores[1].append(n)
    elif c <= 9:
        valores[2].append(n)
for c in range(0, 3):
    print(f'[ {valores[c][0]:^4} ]', end='')
    print(f'[ {valores[c][1]:^4} ]', end='')
    print(f'[ {valores[c][2]:^4} ]\n', end='')
