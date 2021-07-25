valores = list()
par = list()
impar = list()
while True:
    valores.append(int(input('Digite um número: ')))
    stop = ' '
    while stop != 'S' and stop != 'N':
        stop = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if stop == 'N':
        break
for c in valores:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Lista completa {valores}')
print(f'Lista de pares {par}')
print(f'Lista de Ímpares {impar}')
