import pygame
import random
import consts
import time

from Player import Player
from Background import Background
from MenuScreen import MenuScreen
from BlockPlatform import BlockPlatform
from ScoreCounter import ScoreCounter
from GenerationCounter import GenerationCounter
from TextObject import TextObject



def collisionHandler(players , obstacles , score):
    for i in players:
        for j in obstacles:
            if pygame.sprite.collide_rect(i , j):
                i.kill()
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


def nextGen(players , playerGroup , genCounter , scoreCounter):
    for i in players:
        i.kill()

    genCounter.addTo()
    genCounter.updateCounter()

    players.sort(key = lambda x: x.fitness)

    print("Fitness")
    for i in players:
        print(i.fitness)

    # Kill bottom 25
    players = players[:25]

    survivalLen = len(players)
    for i in range(survivalLen - 1):
        average = []
        for j in range(len(players[i].nnetwork.getAllValues())):
            print(players[i].nnetwork.getAllValues()[j])
            average.append((players[i].nnetwork.getAllValues()[j] + players[i + 1].nnetwork.getAllValues()[j]) / 2)

        newPlayer = Player()
        newPlayer.nnetwork.setAllValues(average)
        newPlayer.rect.x = 100
        newPlayer.rect.y = consts.SCREEN_HEIGHT - newPlayer.rect.height

        playerGroup.add(newPlayer)
    
    newPlayer = Player()
    newPlayer.rect.x = 100
    newPlayer.rect.y = consts.SCREEN_HEIGHT - newPlayer.rect.height
    playerGroup.add(newPlayer)

    # Mutate offspring
    # Add a random one

    wait = True

    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    wait = False

    scoreCounter.reset()
    scoreCounter.updateCounter()
    genCounter.updateCounter()

    return playerGroup


def main():
    """ Main Program """
    pygame.init()
 
    # Set the height and width of the screen
    size = [consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Platformer Jumper")

 
    # Create all the levels
    background = Background()

    blockSpeed = 4.5
 
    obstacles = pygame.sprite.Group()
    # obstacles.add(BlockPlatform(800 , 500 , blockSpeed))
    # obstacles.add(BlockPlatform(1200 , 550 , blockSpeed))
    # obstacles.add(BlockPlatform(1600 , 525 , blockSpeed))
    # obstacles.add(BlockPlatform(2000 , 500 , blockSpeed))
    # #obstacles.add(BlockPlatform(1600 , 525 , blockSpeed))
    players = pygame.sprite.Group()
    for i in range(50):
        tempPlayer = Player()
        tempPlayer.rect.x = 100
        tempPlayer.rect.y = consts.SCREEN_HEIGHT - tempPlayer.rect.height

        players.add(tempPlayer)

    scoreCounter = ScoreCounter(100 , 100 , screen)
    genCounter = GenerationCounter(500 , 100 , screen)
    genCounter.updateCounter()      # go ahead and show right away
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    menuScreen = MenuScreen(screen , clock)

    menuScreen.show()

    startTimer = 0
    interval = 50

    # -------- Main Program Loop -----------
    while not done:

        if(len(players.sprites()) > 0):
            scoreCounter.addTo()
        scoreCounter.updateCounter()
        
        
        numGreenBlocks = len(obstacles.sprites())
        if scoreCounter.get() - startTimer > interval:
            generatedNum = random.randint(1,3)
            randomNum = 0
            if generatedNum == 1:
                randomNum = 500
            if generatedNum == 2:
                randomNum = 525
            if generatedNum == 3:
                randomNum = 550
            obstacles.add(BlockPlatform(800 , randomNum , blockSpeed))
            startTimer = scoreCounter.get()
            interval += 0.25
            blockSpeed += 0.2
            print(blockSpeed)
        
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    players = nextGen(players.sprites() , players , genCounter , scoreCounter)
 

        for i in range(len(players.sprites())):
            players.sprites()[i].update(getNNInputs(players.sprites()[i] , obstacles.sprites()))
            players.sprites()[i].fitness = scoreCounter.get()


        obstacles.update()
 

        collisionHandler(players.sprites() , obstacles.sprites() , scoreCounter.get())


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