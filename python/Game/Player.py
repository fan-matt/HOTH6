import pygame
import consts

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.Surface((50, 50))
        self.image.fill((255 , 0 , 0))

        self.rect = self.image.get_rect()

        self.accel = 3000  # Positive because computer graphics, gravity
        self.velocity = 0
        self.yPos = self.rect.y


    def jump(self):
        self.velocity = -1000


    def duck(self):
        oldX = self.rect.x
        oldY = self.rect.y

        self.image = pygame.Surface((50 , 25))
        self.image.fill((255 , 0 , 0))
        self.rect = self.image.get_rect()

        self.setPos(oldX , oldY + 25)

    
    def unDuck(self):
        oldX = self.rect.x
        oldY = self.rect.y

        self.image = pygame.Surface((50 , 50))
        self.image.fill((255 , 0 , 0))
        self.rect = self.image.get_rect()

        self.setPos(oldX , oldY - 25)


    def setPos(self , x , y):
        self.rect.x = x
        self.rect.y = y
        

    def update(self):
        self.velocity += self.accel * 1 / consts.FPS
        dY = self.velocity * 1 / consts.FPS
        self.rect.y += dY