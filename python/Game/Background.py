import pygame
import consts


class Background:
    def __init__(self):
        self.background = None

        
    def draw(self, screen):
        screen.fill(consts.BLUE)
