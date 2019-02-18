import pygame
import consts

class Player(pygame.sprite.Sprite):
    """ This class represents the rectangle the player controls. """

    # Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        
        self.image = pygame.Surface([consts.width, consts.height])
        self.image.fill(consts.RED)
 
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        self.currentHeight = consts.height
 
        self.accel = 3000
        self.velocity = 0
        self.y = consts.height

        self.onGround = True
        self.jumpRequested = False
        
 
    def setPos(self , x , y):
        self.rect.x = x
        self.rect.y = y


    def update(self):
        if self.rect.y >= (consts.SCREEN_HEIGHT - self.currentHeight) and not self.jumpRequested:
            self.onGround = True
            self.rect.y = consts.SCREEN_HEIGHT - self.currentHeight
            
        else:
            self.gravity()
            self.jumpRequested = False
            self.onGround = False
        
        
 
    def gravity(self):
        self.velocity += self.accel * 1 / consts.FPS
        dY = self.velocity * 1 / consts.FPS
        self.rect.y += dY

 
    def jump(self):
        if self.onGround:
            self.jumpRequested = True
            self.velocity = -900

        
    def duck(self):
        oldX = self.rect.x
        oldY = self.rect.y

        self.currentHeight /= 2

        self.image = pygame.Surface((consts.width , self.currentHeight))
        self.image.fill((255 , 0 , 0))
        self.rect = self.image.get_rect()

        self.setPos(oldX , oldY + 25)
        
    def unDuck(self):
        oldX = self.rect.x
        oldY = self.rect.y

        self.currentHeight *= 2

        self.image = pygame.Surface((consts.width , self.currentHeight))
        self.image.fill((255 , 0 , 0))
        self.rect = self.image.get_rect()

        self.setPos(oldX , oldY - 25)