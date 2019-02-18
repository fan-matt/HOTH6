import pygame
import consts
from TextObject import TextObject


class ScoreCounter:
    def __init__(self , x , y , gameDisplay):
        self.score = 0
        self.gameDisplay = gameDisplay
        self.x = x
        self.y = y
        self.scoreFont = pygame.font.Font('freesansbold.ttf', 50)
        self.scoreLabel = TextObject("0" , self.scoreFont , consts.BLACK)
    

    def updateCounter(self):
        self.scoreLabel = TextObject(str(self.score) , self.scoreFont , consts.BLACK)
        TextSurf, TextRect = self.scoreLabel.get()
        TextRect.center = (self.x , self.y)
        self.gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()

    def addTo(self):
        self.score += 1
        self.updateCounter()


    def get(self):
        return self.score


    def reset(self):
        self.score = 0
        self.updateCounter()