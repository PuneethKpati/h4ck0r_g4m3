import pygame
from pygame.locals import *
import os
import sys


class H4ck0rGame:

    def __init__(self):
        pygame.init()

        windowDim   = (800, 800)
        self.gameSurface = pygame.display.set_mode((0,0), HWSURFACE | DOUBLEBUF )

        pygame.display.set_caption('h4ck0r g4me')
        icon = pygame.image.load('./assets/icon.png')
        pygame.display.set_icon(icon)

    def run(self):
        
        while True: 
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == TEXTINPUT:
                    self.handleKey(event.text)
            
            self.welcome()
            pygame.draw.rect(self.gameSurface, (255,255,255), (100,100,150,150))
            
            pygame.display.update() 

    def welcome(self):

        background = pygame.image.load('./assets/background.gif')
        scaledBack = pygame.transform.scale(background, (self.gameSurface.get_width(), self.gameSurface.get_height()))
        self.gameSurface.blit(scaledBack, (0,0))

    def handleKey(self, key):
        print('key pressed: ', key)

game = H4ck0rGame()
game.run()

        
    

    


