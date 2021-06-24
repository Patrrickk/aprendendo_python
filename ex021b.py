import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load('sozinho.mp3')  # Local da música


#   Link da música para baixar: " https://github.com/Patrrickk/aprendendo_python/raw/main/sozinho.mp3 "
#   link da lentra: https://www.letras.mus.br/jao/vou-morrer-sozinho/
#   Copie e cole a letra da música aqui  ↓  dentro das três aspas
letra = [''' ''']


thc = ['Tfuex$n(lhgda     uvcm     bstoihm   zedbfiyza',  # 0
       'Tçwejynizhxea     uqvmzoa     bpsoqka   ççtqwafarebdmqe',  # 1
       'ToIe23ndahjua     uqwmjta     bxçohsa   itnfbozqiiytpqe',  # 2
       'Vgyaqui   iedykolsrdxmitiqjr']  # 3
g = ['''O12b12r12i12g12a12d12o   12p12o1pr     t12e12s12t12a12r     m12e12u        c12ó12d12i12g12o     :  ) ',
     '... MoPefmuz#   DfUi2#szpci0ocbrlqdry   >     Pjkkf5#1w0zo6nx1aj6''']
ff = [g[0][::3]]
hora = time.localtime().tm_hour
lembrete = ['Ainda estou apredendo, a programar em Python...']
cor = '\033[1:35m'
play = 1

add_letra = len(letra[0])
while True:
    if add_letra <= 1500:
        time.sleep(3)
        print('\n\033[1:31mPrimeiro você precisa adicionar a letra da música!!! está na linha 9\033[m')
    else:
        pygame.mixer.music.play()
        if play == 1:
            for c in range(0, len(letra[0])):
                time.sleep(.1)
                print(letra[0][c], end='')
                play += 1
        print('\n\033[1:34m')
        for ss in range(0, len(lembrete[0])):
            time.sleep(.4)
            print(lembrete[0][ss], end='')
        if pygame.mixer.music.get_busy() == 0:
            pygame.mixer.music.stop()
            print('\n')
            for b in range(0, len(ff[0])):
                time.sleep(.1)
                print(ff[0][b], end='')
            print('\n')
            time.sleep(1)
            if 6 <= hora <= 12:
                print(thc[0][::3], end='')
            elif 12 <= hora <= 18:
                print(thc[1][::3], end='')
            elif 18 <= hora <= 24:
                print(thc[2][::3], end='')
            else:
                print(thc[3][::3], end='')
            break
