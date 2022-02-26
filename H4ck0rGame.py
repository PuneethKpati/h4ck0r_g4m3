from turtle import back
import pygame
from pygame.locals import *
import os
import sys
from Player import Player
from Map import Map

class H4ck0rGame:
    def __init__(self):
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()

        gameSurface = pygame.display.set_mode((0,0), HWSURFACE | DOUBLEBUF )

        pygame.display.set_caption('h4ck0r g4me')
        icon = pygame.image.load('./assets/icon.png')
        pygame.display.set_icon(icon)

        background = pygame.image.load('./assets/background.jpg')

        # Map 
        map = Map()

        # Player 
        player = Player('./assets/icon.png')
        playerGroup = pygame.sprite.Group()
        playerGroup.add(player)
        map.add_player(player)

        while True: 
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                    
            pressed = pygame.key.get_pressed()
            if self.movement_key_pressed(pressed):
                map.update_player(pressed)



            pygame.display.flip()
            gameSurface.fill((0,0,0))
            
            
            playerGroup.draw(gameSurface)
            pygame.display.update()
            
            clock.tick(120)

    def movement_key_pressed(self, pressed):
        return pressed[K_w] or pressed[K_s] or pressed[K_a] or pressed[K_d]
game = H4ck0rGame()
game.run()

        
    

    


