import random
pc = random.choice(['tesoura', 'pedra', 'papel'])
print('''suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
player = int(input('Escolha uma: '))
print(f'PC JOGOU {pc}')
if player == 0:  # pedra
    print(f'JOGADOR JOGOU PEDRA')
    if pc == 'papel':
        print('PC VENCEU')
    elif pc == 'tesoura':
        print('JOGADOR VENCEU')
    elif pc == 'pedra':
        print('EMPATOU')
    else:
        print('Opcão inválida')
elif player == 1:  # papel
    print(f'JOGADOR JOGOU PAPEL')
    if pc == 'pedra':
        print('JOGADOR VENCEU')
    elif pc == 'tesoura':
        print('PC VENCEU')
    elif pc == 'pepel':
        print('EMPATOU')
    else:
        print('Opcão inválida')
elif player == 2:  # tesoura
    print(f'JOGADOR JOGOU TESOURA')
    if pc == 'pedra':
        print('PC VENCEU')
    elif pc == 'papel':
        print('JOGADOR VENCEU')
    elif pc == 'tesoura':
        print('EMPATOU')
    else:
        print('Opcão inválida')

else:
    print('Opcão inválida!')
