galera = list()
dados = []
totpes = 0
menor_pes = maior_pes = 0
while True:
    dados.append(str(input('Qual é seu nome: ')))
    dados.append(float(input('Seu peso: [kg] ')))
    galera.append(dados[:])
    dados.clear()
    totpes += 1
    stop = str(input('Quer continuar: ')).strip().lower()
    if stop in 'n':
        break
print(f'Foram cadastradas {totpes} pessoas.')
for pos, p in enumerate(galera):
    if pos == 0:
        maior_pes = menor_pes = p[1]
    else:
        if p[1] >= maior_pes:
            maior_pes = p[1]
        if p[1] <= menor_pes:
            menor_pes = p[1]
print(f'O maior peso foi de {maior_pes}Kg. peso de', end='')
for ga in galera:
    if ga[1] == maior_pes:
        print(f'{ga[0]},', end='')
print()
print(f'\nO menor peso foi de {menor_pes}Kg. peso de', end='')
for ga in galera:
    if ga[1] == menor_pes:
        print(f'{ga[0]},', end='')
