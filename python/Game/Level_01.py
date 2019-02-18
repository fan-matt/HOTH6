import pygame
from Level import Level
from Platform import Platform
from MovingPlatform import MovingPlatform
import random


class Level_01(Level):
    """ Definition for level 1. """
    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)
 
        # Array with width, height, x, and y of platform
        level = []#[[210, 70, 550, 550]]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
            
        block1 = MovingPlatform(25, 50)
        block1.rect.x = 800
        block1.rect.y = 550
        block1.boundary_left = -50
        block1.boundary_right = 800
        block1.change_x = 5
        block1.player = self.player
        block1.level = self
        self.platform_list.add(block1)        

        block2 = MovingPlatform(25, 50)
        block2.rect.x = 1050
        block2.rect.y = 525
        block2.boundary_left = -50
        block2.boundary_right = 1050
        block2.change_x = 5
        block2.player = self.player
        block2.level = self
        self.platform_list.add(block2)        

