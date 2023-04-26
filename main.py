from src.dragon import Dragon
from src.game import Game
from src.floor import Floor
from src.score import *
import pygame
import sys

pygame.init()

window = pygame.display.set_mode((360, 600))    # make a window
icon = pygame.image.load('img/python.png')    

pygame.display.set_caption("Flappython")    # put a title
pygame.display.set_icon(icon)               # display a icon

# load background image
background = pygame.image.load("img/background.png")    
background = pygame.transform.scale(background, (370, 620))

# load pause logo
pause = pygame.image.load("img/pause.png")
pause = pygame.transform.scale(pause, (80, 80))

clock = pygame.time.Clock() # manage the time
running = True              # run the game

game = Game()
floor = Floor()
floor2 = Floor(360)

# load the score font
font = pygame.font.Font("font/HANGTHEDJ.ttf", 70)
font2 = pygame.font.Font("font/HANGTHEDJ.ttf", 30)


while running:

    # display images
    window.blit(background, (0, 0))
    window.blit(game.dragon.image, game.dragon.rect)
    game.all_towers1.draw(window)
    game.all_towers2.draw(window)

    # display score
    point = font.render(f"{game.dragon.point}", 1, (0, 0, 0))
    text_width, text_height = font.size(f"{game.dragon.point}")
    window.blit(point, (180-(text_width//2), 10))

    high_score = font2.render(f"High score: {score_min_max(2)}", 1, (0, 0, 0))
    high_score_width, high_score_height = font2.size(f"High score: {score_min_max(2)}")
 
    game.dragon.gravitate()
    game.game_over(window)

    if game.loose == True:
        window.blit(high_score, ((180-high_score_width//2), 490))

    if game.stop:
        window.blit(pause, (130, 220))

    for tower in game.all_towers1:
        tower.mouvement(1)

    for tower in game.all_towers2:
        tower.mouvement(2)

    game.dragon.rotation(game.ready)

    if game.ready and not game.stop:
        floor.move()
        floor2.move()
        game.add_point()
    
    floor.sprite.draw(window)
    floor2.sprite.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # exit game
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # when space is pressed
                game.jump()
            elif event.key == pygame.K_RIGHT:
                game.dragon.change_image()
            elif event.key == pygame.K_RETURN:
                game.start()
            elif event.key == pygame.K_ESCAPE:
                if game.ready:
                    if game.stop:
                        game.stop = False
                    else:
                        game.stop = True

    clock.tick(60)          # 60fps limit
    pygame.display.flip()   # update screen