jogador = dict()
gol = list()
time = list()
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, quant):
        gol.append(int(input(f'Quantos gols na partida {c}? ')))
        jogador['gols'] = gol[:]
        jogador['total'] = 0
        for gols in jogador['gols']:
            jogador['total'] += gols
    gol.clear()
    time.append(jogador.copy())
    jogador.clear()
    stop = ''
    while stop != 'S' and stop != 'N':
        stop = str(input('Quer continuar: [S/N]')).strip().upper()
    if stop == 'N':
        break
print('-=-' * 20)
print(f'{"Cod nome":<20} {"GOLS":<20} {"TOTAL":>10}')
print('-' * 60)
for k, c in enumerate(time):
    print(f" {k:<3}{c['nome']:<16}", f"{c['gols']!s:<26s}", f"{c['total']}")
while True:
    print('-' * 60)
    stop = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if stop == 999:
        break
    for a in range(0, len(time)):
        gol.append(a)
    if stop not in gol:
        print(f'ERRO! Não existe jogador com código {stop}! Tente novamente')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[stop]["nome"]}:')
        for pos, c in enumerate(time[stop]['gols']):
            print(f'    No jogo {pos} fez {c} gols.')
print('PROGRAMA FINALIZADO COM SUCESSO')
print('<<< VOLTE SEMPRE >>>')
