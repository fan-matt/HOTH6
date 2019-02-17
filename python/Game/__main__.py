import pygame
import random
from Player import Player
import consts


# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

player.setPos(50 , 50)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(consts.FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.duck()
            
            if event.key == pygame.K_UP:
                player.jump()

            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.unDuck()

    # Draw / render
    screen.fill(consts.BLACK)

    # Update
    all_sprites.update()
    all_sprites.draw(screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()