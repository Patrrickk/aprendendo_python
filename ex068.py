from random import *
vit = 0
while True:
    pc = randint(1, 100)
    pc_escolha = choice(['p', 'i'])
    jogador = int(input('Digite um valor: '))
    jogador_escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().lower()[0]
    soma = jogador + pc
    par = soma % 2
    impar = soma % 2
    print(f'Voce jogou {jogador} e o computador {pc}.', end='')
    if jogador_escolha == 'p' or 'i':
        if par == 0:
            print(f' Total de {soma} DEU PAR')
            if jogador_escolha == 'p' and pc_escolha == 'i':
                vit += 1
                print('Você venceu!')
                print('Vamos jogar novamente...')
            elif pc_escolha == 'p' and jogador_escolha == 'i':
                print('Você perdeu!')
                break
            else:
                print('EMPATE, os dois pediram PAR tente de novo')
        if impar == 1:  # ÍMPAR
            print(f' Total de {soma} DEU ÍMPAR')
            if jogador_escolha == 'i' and pc_escolha == 'p':
                vit += 1
                print('Você venceu')
                print('Vamos jogar novamente...')
            elif pc_escolha == 'i' and jogador_escolha == 'p':
                print('Você perdeu')
                break
            else:
                print('EMPATE, os dois pediram PAR tente de novo')
print(f'GAME OVER! Você venceu {vit} vezes.')
