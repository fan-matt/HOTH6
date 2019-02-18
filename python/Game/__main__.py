import pygame
import random
import consts

from Player import Player
from Background import Background
from MenuScreen import MenuScreen
from BlockPlatform import BlockPlatform
from ScoreCounter import ScoreCounter
from TextObject import TextObject



def checkCollision(players , obstacles , score):
    for i in players:
        for j in obstacles:
            if pygame.sprite.collide_rect(i , j):
                i.kill()
                i.fitness = score
                return True

    return False


def getNNInputs(player , obstacles):
    if len(obstacles) >= 1:
        deltaX = obstacles[0].rect.x - player.rect.x
        nextY = obstacles[0].rect.y

    # This is when the obstacle passes but hasn't been killed yet
    elif len(obstacles) >= 2 and obstacles[0].rect.x - player.rect.x < 0:
        deltaX = obstacles[1].rect.x - player.rect.x
        nextY = obstacles[1].rect.y
    
    else:
        deltaX = 0
        nextY = 0

    obstacleType = 1

    playerY = player.rect.y

    print((deltaX , nextY , obstacleType , playerY))

    return (deltaX , nextY , obstacleType , playerY)


def main():
    """ Main Program """
    pygame.init()
 
    # Set the height and width of the screen
    size = [consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Platformer Jumper")

 
    # Create all the levels
    background = Background()

 
    obstacles = pygame.sprite.Group()
    obstacles.add(BlockPlatform(500 , 500 , 4))
    obstacles.add(BlockPlatform(400 , 500 , 4))
    obstacles.add(BlockPlatform(600 , 500 , 4))


    players = pygame.sprite.Group()
    for i in range(50):
        tempPlayer = Player()
        tempPlayer.rect.x = 100
        tempPlayer.rect.y = consts.SCREEN_HEIGHT - tempPlayer.rect.height

        players.add(tempPlayer)

    scoreCounter = ScoreCounter(100 , 100 , screen)
    

 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    menuScreen = MenuScreen(screen , clock)

    menuScreen.show()


    # -------- Main Program Loop -----------
    while not done:
        
        scoreCounter.addTo()
        scoreCounter.updateCounter()

        print(scoreCounter.get())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP:
            #         player.jump()
            #     if event.key == pygame.K_DOWN:
            #         player.duck()
            
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_DOWN:
            #         player.unDuck()
 

        for i in range(len(players.sprites())):
            players.sprites()[i].update(getNNInputs(players.sprites()[i] , obstacles.sprites()))


        obstacles.update()
 

        checkCollision(players.sprites() , obstacles.sprites() , scoreCounter.get())


        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        background.draw(screen)
        players.draw(screen)
        obstacles.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(consts.FPS)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()