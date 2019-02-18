import pygame
import consts
from TextObject import TextObject


class GenerationCounter:
    def __init__(self , x , y , gameDisplay):
        self.gen = 0
        self.gameDisplay = gameDisplay
        self.x = x
        self.y = y
        self.genFont = pygame.font.Font('freesansbold.ttf', 50)
        self.genLabel = TextObject("Generation 0" , self.genFont , consts.BLACK)
    

    def updateCounter(self):
        self.genLabel = TextObject("Generation " + str(self.gen) , self.genFont , consts.BLACK)
        TextSurf, TextRect = self.genLabel.get()
        TextRect.center = (self.x , self.y)
        self.gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()

    def addTo(self):
        self.gen += 1
        self.updateCounter()


    def get(self):
        return self.score


    def reset(self):
        self.score = 0
        self.updateCounter()