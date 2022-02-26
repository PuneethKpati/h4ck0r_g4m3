from hashlib import new
import pygame
from pygame.locals import *
import os

class Player(pygame.sprite.Sprite):
    

    def __init__(self, image):
        super().__init__()
        ICON_SIZE = (100,100)
        self.image = pygame.image.load(image)
        self.rect  = self.image.get_rect()


        self.fox_sitting_count = 0
        self.fox_sitting = [pygame.transform.scale(pygame.image.load('./assets/fox_sitting_1.png'), ICON_SIZE), 
        pygame.transform.scale(pygame.image.load('./assets/fox_sitting_2.png'), ICON_SIZE),
        pygame.transform.scale(pygame.image.load('./assets/fox_sitting_3.png'), ICON_SIZE)]
        

        self.speed = 2

    def update(self):
        self.sitting_animation(animation_speed=0.1)
        
    def sitting_animation(self, animation_speed):
        
        self.fox_sitting_count = (self.fox_sitting_count + animation_speed) 
        next_frame = int(self.fox_sitting_count) % len(self.fox_sitting)

        self.image = self.fox_sitting[next_frame]

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

    
        
    

        