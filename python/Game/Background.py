import pygame
import consts


class Background:
    def __init__(self):
        self.background = None

        
    def draw(self, screen):
        background_image = pygame.image.load("menu.png").convert()
        screen.blit(background_image, [0,0])
