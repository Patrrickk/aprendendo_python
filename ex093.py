jogador = dict()
gol = list()
jogador['nome'] = str(input('Nome do Jogador: '))
quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, quant):
    gol.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = gol[:]
    jogador['total'] = 0
    for gols in jogador['gols']:
        jogador['total'] += gols
print('-=-' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-' * 20)
print(f'O jogador {jogador["nome"]} jogou {quant} partidas.')
for p in range(0, quant):
    print(f'{"=>":>5} ' f'Na partida {p}, fez {jogador["gols"][p]}.')
print(f'Foi um total de {jogador["total"]} gols.')
