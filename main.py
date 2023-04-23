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

# make a background
background = pygame.image.load("img/background.png")    
background = pygame.transform.scale(background, (370, 620))

clock = pygame.time.Clock()
running = True  # the window is open

game = Game()
floor = Floor()
floor2 = Floor(360)

# fonts for the score
font = pygame.font.SysFont("Hang the DJ", 70)
font2 = pygame.font.SysFont("Hang the DJ", 30) 

while running:
    # display the images
    window.blit(background, (0, 0))
    window.blit(game.dragon.image, game.dragon.rect)
    game.all_towers1.draw(window)
    game.all_towers2.draw(window)

    # display the score
    point = font.render(f"{game.dragon.point}", 1, (0,0,0))
    text_width, text_height = font.size(f"{game.dragon.point}")
    window.blit(point, (180-(text_width//2),10))

    high_point = font2.render(f"High score: {score_min_max(2)}", 1, (0,0,0))
    text_width, text_height = font2.size(f"{score_min_max(2)}")
 
    game.dragon.gravite()
    game.game_over()
    if game.loose == True:
        window.blit(high_point, (0,490))

    for tower in game.all_towers1:
        tower.deplacement(1)

    for tower in game.all_towers2:
        tower.deplacement(2)

    game.dragon.rotation(game.ready)

    if game.ready:
        floor.move()
        floor2.move()
        game.add_point()
    floor.sprite.draw(window)
    floor2.sprite.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # to quit the window
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # if space pressed
                game.start()
            elif event.key == pygame.K_x:
                game.dragon.change_image()

    clock.tick(60)  # put 60fps max
    pygame.display.flip() # update the window
