import pygame


# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

class Block(pygame.sprite.Sprite):

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

        self.change_x = 0

    def changespeed(self, elapsed_time):
        self.change_x = self.change_x + elapsed_time

    def update(self):
        self.rect.x = self.change_x + self.rect.change_x
    
        if self.rect.x < 0
            self.remove(self.rect)
