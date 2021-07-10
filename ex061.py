n = ' GERADOR DE PA '
print(f'{n:=^50}')
termos = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
parada = 0
quant = 0
while parada != 1:
    print(termos, end=' → ')
    termos += razao
    quant += 1
    if quant == 10:
        parada = 1
print('fim')
