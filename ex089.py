notas = list()
temp = notas[:]
cont = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    notas.append(temp[:])
    temp.clear()
    stop = str(input('Quer continuar? [S/N] '))
    if stop == 'n':
        break
print(f'{"No.":<6} {"NOME":<10} {"MÉDIA":>8}')
print('-' * 30)
for pos, c in enumerate(notas):
    notas[pos].insert(3, (c[1] + c[2]) / 2)
    print(f'{pos:<4} {c[0]:<10} {c[3]:>8.1f}')
    cont += 1
    if cont == len(notas):
        while True:
            print('-' * 30)
            ve = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
            if ve == 999:
                break
            print(f'Notas de {notas[ve][0]} são {notas[ve][1:3]}')
print('VOLTE SEMPRE')
