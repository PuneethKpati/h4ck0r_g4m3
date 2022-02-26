from hashlib import new
import pygame
from pygame.locals import *
import os
from Map import Map

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        self.map = map

        self.image = pygame.image.load(image)
        self.rect  = self.image.get_rect()

        self.speed = 2


    def move(self, pressed):
        if pressed[K_w]:
            self.set_y(self.rect.y - self.speed)

        if pressed[K_s]:
            self.set_y(self.rect.y + self.speed)

        if pressed[K_a]:
            self.set_x(self.rect.x - self.speed)

        if pressed[K_d]:
            self.set_x(self.rect.x + self.speed)

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def set_x(self, x):
        self.rect.x = x

    def set_y(self, y):
        self.rect.y = y 

    
        
    

        