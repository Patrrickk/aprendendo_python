jogador = dict()
gol = list()
jogador['nome'] = str(input('Nome do Jogador: '))
quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, quant):
    gol.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = gol
print(jogador)
