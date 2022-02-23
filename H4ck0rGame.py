import pygame
from pygame.locals import *
import os
import sys


class H4ck0rGame:

    def __init__(self):
        pygame.init()

        windowDim   = (800, 800)
        gameSurface = pygame.display.set_mode((0,0), HWSURFACE | DOUBLEBUF | RESIZABLE)
        pygame.display.set_caption('h4ck0r g4me')

        icon = pygame.image.load('./assets/icon.png')
        pygame.display.set_icon(icon)

    def run(self):
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


game = H4ck0rGame()
game.run()

        
    

    


