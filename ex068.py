from random import *
vit = 0
while True:
    pc = randint(1, 11)
    jogador = int(input('Digite um valor: '))
    jogador_escolha = ' '
    while jogador_escolha not in 'pi':
        jogador_escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().lower()[0]
    soma = jogador + pc
    par = soma % 2
    print(f'Voce jogou {jogador} e o computador {pc}.', end='')
    if jogador_escolha == 'p' or 'i':
        if par == 0:
            print(f' Total de {soma} DEU PAR')
            if jogador_escolha == 'p':
                vit += 1
                print('Você venceu!')
                print('Vamos jogar novamente...')
            else:
                print('Você perdeu!')
                break
        if par == 1:  # ÍMPAR
            print(f' Total de {soma} DEU ÍMPAR')
            if jogador_escolha == 'i':
                vit += 1
                print('Você venceu')
                print('Vamos jogar novamente...')
            else:
                print('Você perdeu')
                break
print(f'GAME OVER! Você venceu {vit} vezes.')
