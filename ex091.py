from random import randint
from time import sleep
jogadores = dict()
cont = 0
print('Sorteando:')
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)
    print(f'O jogador{c} tirou {jogadores[f"jogador{c}"]} no dado')
    sleep(1)
print(' === Ranking dos jogadores: ===')
for a in range(7, 0, -1):
    for k, v in jogadores.items():
        if a == v:
            cont += 1
            print(f' >> {cont}º lugar: {k} com {v}')
            sleep(1)
