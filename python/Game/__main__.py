import pygame
import random
import consts

from Player import Player
from Level_01 import Level_01
from MenuScreen import MenuScreen



def main():
    """ Main Program """
    pygame.init()
 
    # Set the height and width of the screen
    size = [consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Platformer Jumper")
 
    # Create the player
    player = Player()
 
    # Create all the levels
    level_list = []
    level_list.append( Level_01(player) )
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 100
    player.rect.y = consts.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)


 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    menuScreen = MenuScreen(screen , clock)

    menuScreen.show()


    # -------- Main Program Loop -----------
    while not done:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_DOWN:
                    player.duck()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player.revert()
 
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right > consts.SCREEN_WIDTH:
            player.rect.right = consts.SCREEN_WIDTH
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left < 0:
            player.rect.left = 0
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()