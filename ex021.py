import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load('sozinho.mp3')
pygame.mixer.music.play()
lista = ['Você me ama bem, mas eu me distraio um pouco',
         'Se eu paro pra pensar', 'Concluo que sou louco',
         'Juro que eu não queria ser assim', 'Só gostar de quem não gosta de mim',
         'Ai meu Deus', 'Bem que a minha mãe me avisou', 'Que eu ia conhecer o amor',
         'E deixaria ele ir embora', 'Se você me amar demais', 'Eu paro de te amar',
         'Um amor fácil me apavora', 'Ai meu Deus', 'Eu vou morrer sozinho',
         'Se eu continuar nesse caminho']
print(len(lista))
play = 0,

for joao in range(0, 16):
    if play == 0:
        time.sleep(2)
        print(lista[0 ])
        play = 1
    if joao <= 1:
        time.sleep(4)
        print(lista[joao])
    if 2 <= joao <= 5:
        time.sleep(2)
        print(lista[joao])
    if 6 <= joao <= 10:
        print(joao)
        time.sleep(3)
        print(lista[joao])
    if joao >= 11:
        while True:
            print(joao)
            time.sleep(2)
            print(lista[joao])
    # if joao > 4 or joao < 12:
    #     time.sleep(3)
    #     print(lista[joao])
while pygame.mixer.music.get_busy():
    pass
