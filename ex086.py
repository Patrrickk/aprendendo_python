valores = list()
for c in range(0, 9):
    n = int(input('Digite um número: '))
    if c == 0:
        valores.append([])
    if c < 3:
        valores[0].append(n)
    elif c <= 5:
        if c == 3:
            valores.append([])
        valores[1].append(n)
    elif c <= 9:
        if c == 6:
            valores.append([])
        valores[2].append(n)
for c in range(0, 3):
    print(f'[{valores[0][c]}]')
    print(f'[{valores[1][c]}]')
    print(f'[{valores[2][c]}]')
