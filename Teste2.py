from time import sleep
from random import sample
sorteo = []
fim = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{" SORTEANDO ":=^30} ')
for c in range(0, fim):
    sorteo.append(sample(range(60), k=6))
    sorteo[c].sort()
    print(f'Jogo :{len(sorteo)} {sorteo[c]}')
    sleep(1)
print(sorteo)
