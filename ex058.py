from random import randint
from time import sleep
print('-=-' * 18)
frase = ['Vou pensar em um número entre 0 e 10 tente adivinhar..']
for c in range(0, len(frase[0])):
    print(frase[0][c], end='')
    sleep(.09)
print('\n', '-=-' * 18)
pc = randint(0, 10)
player = 11
palpites = 0
while pc != player:
    player = int(input('Em qual número eu pensei: '))
    palpites += 1
    if pc != player:
        print('\033[1:91mErrooooou, tente de novo\033[m')
    else:
        print('\033[1:92mAcertou mizeravi\033[m')
print(f'Ao todo foram {palpites} palpites até acertar')
