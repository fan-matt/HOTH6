import pygame, sys
from pygame.locals import *


pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# Set up the window
screen_width = 1000
screen_height = 700
display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game')

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

background=pygame.image.load('white.png')
sprite=pygame.image.load('cat.png')
spritex=300
spritey=300
direction='right'

while True:
    display.blit(background,(0,0))

    display.blit(sprite,(spritex,spritey))

    # for event in pygame.event.get():
    #     # if event.type==QUIT:
    #     #     pygame.quit()
    #     #     sys.exit()

    #     if event.type == KEYDOWN:
    #         if (event.key == pygame.K_LEFT):
    #             sprite=pygame.image.load('left.png')
    #         elif (event.key == pygame.K_RIGHT):
    #             sprite=pygame.image.load('right.png')
    #         elif (event.key == pygame.K_UP):
    #             sprite=pygame.image.load('up.png')
    #         elif (event.key == pygame.K_DOWN):
    #             sprite=pygame.image.load('down.png')
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    spritex -= 5
                if event.key == pygame.K_RIGHT:
                    spritex += 5
        
    pygame.display.update()
    fpsClock.tick(FPS)