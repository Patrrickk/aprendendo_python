import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load('sozinho.mp3')  # Local da música


#   Link da música para baixar: " encurtador.com.br/klmEW "
#   link da lentra: https://www.letras.mus.br/jao/vou-morrer-sozinho/
#   Copie e cole a letra da música aqui  ↓  dentro das três aspas
letra = ['''Você me ama bem
Mas eu me distraio um pouco
Se eu paro pra pensar
Concluo que eu sou louco
Juro que eu não queria ser assim
Só gostar de quem não gosta de mim

Ai, meu Deus
Bem que a minha mãe me avisou
Que eu ia conhecer o amor
E deixaria ele ir embora
Se você me amar demais
Eu paro de te amar
Um amor fácil me apavora

Ai, meu Deus, eu vou morrer sozinho
Se eu continuar nesse caminho
Ai, meu Deus, eu vou morrer sozinho
Se eu continuar nesse caminho
De não deixar ninguém me amar
E de só me apaixonar
Por quem me faz chorar e me maltrata
Ai, meu Deus, eu vou morrer sozinho

Ai, meu Deus, eu vou morrer sozinho
Ai, meu Deus, eu vou morrer sozinho
Ai, meu Deus, eu vou morrer sozinho
Ai, meu Deus, eu vou morrer sozinho

Você me ama bem
Mas eu me distraio um pouco
Se eu paro pra pensar
Concluo que eu sou louco
Juro que eu não queria ser assim
Só gostar de quem não gosta de mim

Ai, meu Deus
Bem que a minha mãe me avisou
Que eu ia conhecer o amor
E deixaria ele ir embora
Se você me amar demais
Eu paro de te amar
Um amor fácil me apavora

Ai, meu Deus, eu vou morrer sozinho
Se eu continuar nesse caminho
Ai, meu Deus, eu vou morrer sozinho
Se eu continuar nesse caminho (vou morrer sozinho)
De não deixar ninguém me amar
E de só me apaixonar
Por quem me faz chorar e me maltrata
Ai, meu Deus, eu vou morrer sozinho

Ai, meu Deus, eu vou morrer sozinho
Ai, meu Deus, eu vou morrer sozinho
Ai, meu Deus, eu vou morrer sozinho
Ai, meu Deus, eu vou morrer sozinho

Ai, meu Deus
Ai, meu Deus, eu vou morrer sozinho''']


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
        print('\n\033[1:31mVocê precisa adicionar a letra primeiro!!!\033[m')
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
