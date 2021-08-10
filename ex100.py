from random import randint
from time import sleep


def sorteio(dados):
    print('Sordeando 5 valores da lista: ', end='')
    for c in range(0, 5):
        dados.append(randint(1, 9))
    for p in dados:
        print(p, end=' ')
        sleep(.5)
    print('PRONTO!')


def somapar(pares):
    print(f'Somando os valores pares de {pares}, temos ', end='')
    par = 0
    for c in pares:
        if c % 2 == 0:
            par += c
    print(par)


numeros = []
sorteio(numeros)
somapar(numeros)
