import pygame
import random


# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

class Car(pygame.sprite.Sprite):

   def __init__(self, color, width, height):
    
    # Call the parent class (Sprite) constructor
        super().__init__()

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
