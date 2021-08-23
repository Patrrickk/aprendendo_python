from random import randint
from time import sleep


def sorteio(dados):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        p = randint(1, 9)
        dados.append(p)
        print(p, end=' ')
        sleep(.5)
    print('PRONTO!')


def somapar(pares):
    par = 0
    for c in pares:
        if c % 2 == 0:
            par += c
    print(f'Somando os valores pares de {pares}, temos {par}')


numeros = []
sorteio(numeros)
somapar(numeros)
