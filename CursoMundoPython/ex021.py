# add arquivo de midia mp3 musica

import pygame
pygame.init()
pygame.mixer_music.load('exm21.mp3')
pygame.mixer_music.play()
pygame.event.wait()


