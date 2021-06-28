import emoji
import random

emojis = {'tesoura': ':v:',
          'pedra': ':facepunch:',
          'papel': ':hand:'}
pc = random.choice(list(reversed(emojis)))
player = str(input('Escolha tesoura ou pedra ou papel: ')).lower().strip()
print(player[0:2])
if pc == 'tesoura' and player[0:2] == 'pe':
    print('VC GANHOU \nO PC escolheu ', end='')
    print(emoji.emojize(emojis[pc], use_aliases=True))
    print('E você escolheu ', end='')
    print(emoji.emojize(emojis['pedra' if player == 'pe' else 'pedra'], use_aliases=True))
elif pc == 'tesoura' and player[0:2] == 'pa':
    print('VC PC GANHOU \nO PC escolheu ', end='')
    print(emoji.emojize(emojis[pc], use_aliases=True))
    print('E você escolheu ', end='')
    print(emoji.emojize(emojis['papel' if player == 'pa' else 'papel'], use_aliases=True))
elif pc == 'papel':
    print('O PC escolheu ', end='')
    print(emoji.emojize(emojis[pc], use_aliases=True))
    print('E você escolheu ', end='')
    print(emoji.emojize(emojis['pedra' if player == 'pe' else pc], use_aliases=True))
