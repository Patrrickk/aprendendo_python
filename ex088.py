from time import sleep
from random import sample
jogos = [[]]
print(f'{"JOGAR NA MEGA SENA":^30}')
quant = int(input('Quantos jogos quer que eu sorteie? '))
cont = 0
print(f'{f"SORTEANDO {quant} JOGOS":^30}\n{"=" * 35}')
for a in range(1, 61):
    jogos[0].append(a)
while cont < quant:
    jogos.append(sample(jogos[0], k=6))
    cont += 1
    jogos[cont].sort()
    print(f'Jogo {cont}: {jogos[cont]}')
    sleep(1)
print(f'{" BOA SORTE! ":=^35}')
