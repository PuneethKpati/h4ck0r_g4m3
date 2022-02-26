
import pygame
from pygame.locals import *


class Map():
    def __init__(self):
        self.player = None
        # Window dimensions 
        self.resolutionx, self.resolutiony = pygame.display.get_window_size()
        # Define the boundaries for the player movement
        self.player_low_bound_y = 0.25 * self.resolutiony
        self.player_high_bound_y = 0.75 * self.resolutiony
        self.player_low_bound_x = 0.25 * self.resolutionx
        self.player_high_bound_x = 0.75 * self.resolutionx


    def add_player(self, player):
        self.player = player
        self.player.set_x(int(self.resolutionx/2))
        self.player.set_y(int(self.resolutiony/2))
        

    def update_player(self, pressed):
        self.player.move(pressed)
        self.player_bound_x()
        self.player_bound_y()
        

    def player_bound_y(self):
        if self.player.get_y() < self.player_low_bound_y:
            self.player.set_y(self.player_low_bound_y)

        elif self.player.get_y() > self.player_high_bound_y:
            self.player.set_y(self.player_high_bound_y)
        
        
    def player_bound_x(self):
        if self.player.get_x() < self.player_low_bound_x:
            self.player.set_x(self.player_low_bound_x)

        elif self.player.get_x() > self.player_high_bound_x:
            self.player.set_x(self.player_high_bound_x)
