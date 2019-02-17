import pygame
import sys
from TextObject import TextObject
import consts

class MenuScreen:
    def __init__(self , gameDisplay , clock):
        self.gameDisplay = gameDisplay
        self.clock = clock

    
    def show(self):
        show = True

        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                elif event.type == pygame.KEYDOWN:
                    show = False
                    print("Hello")
                
            self.gameDisplay.fill(consts.WHITE)
            largeText = pygame.font.Font('freesansbold.ttf', 115)

            title = TextObject("HOTH6" , largeText , consts.BLACK)

            TextSurf, TextRect = title.get()
            TextRect.center = ((consts.SCREEN_WIDTH / 2) , (consts.SCREEN_HEIGHT / 2))
            self.gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            self.clock.tick(15)
