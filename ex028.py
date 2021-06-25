from random import randint
pc = randint(0, 5)
print('-=-' * 18)
print('Vou pensar em um número entre 0 e 5 tente adivinhar..')
print('-=-' * 18)
player = int(input('Em qual número eu pensei?: '))
if pc == player:
    print(f'Parabéns! você acertou eu pensei no número {pc}')
else:
    print(f'Você errou, pensei no {pc} e você falou {player}. Tente novamente!!')
