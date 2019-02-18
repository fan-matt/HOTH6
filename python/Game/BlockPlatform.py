import pygame
import consts


class BlockPlatform(pygame.sprite.Sprite):
    def __init__(self , x , y , speed):
        super().__init__()

        self.speed = speed
        self.x = x
        self.y = y

        self.image = pygame.Surface([consts.PLAT_WIDTH, consts.PLAT_HEIGHT])
        self.image.fill(consts.GREEN)
 
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        self.setPos(self.x , self.y)



    def update(self):
        self.rect.x -= self.speed

        if self.checkOffScreen():
            print("I'm dead")
            self.kill()
            


    def setPos(self , x , y):
        self.rect.x = x
        self.rect.y = y


    def checkOffScreen(self):
        return self.rect.x < -25