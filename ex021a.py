import pygame
pygame.mixer.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
while True:
    if pygame.mixer.music.get_busy() == 0:
        pygame.mixer.music.stop()
        break
