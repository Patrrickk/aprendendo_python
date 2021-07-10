termos = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
fim = 10
while cont <= fim:
    print(termos, end='')
    print(' → ' if cont < fim - 1 else ' → PAUSA', end='')
    termos += razao
    cont += 1
    if cont >= fim:
        razao = int(input('\nMais quantos termos: '))
        fim += razao
        if razao == 0:
            fim = 0
print(f'Progressão finalizada com {cont} termos mostrados.')
