cont = n = 10
print(f'{"TABUADA V3":^50}')
while True:
    if cont == 10:
        print('=' * 50)
        n = int(input('Digite um número para ver sua tabuada: '))
        print('=' * 50)
        if n * 1 < 0:
            break
        cont = 0
    cont += 1
    print(f'{n} X {cont:2} = {n * cont}')
print('Programa finalizado com sucesso!')
