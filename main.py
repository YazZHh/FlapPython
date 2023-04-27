from src.game import Game
from src.floor import Floor
from src.score import *
import pygame
import sys

pygame.init()

window = pygame.display.set_mode((360, 600))    # Make a window
icon = pygame.image.load('img/logo.png')    

pygame.display.set_caption("FlapPython")    # Set title
pygame.display.set_icon(icon)               # Display icon

# Load background image
background = pygame.image.load("img/background.png")    
background = pygame.transform.scale(background, (370, 620))

# Load pause logo
pause = pygame.image.load("img/pause.png")
pause = pygame.transform.scale(pause, (80, 80))

clock = pygame.time.Clock() # Manage the time
running = True              # Run the game

game = Game()
floor = Floor()
floor2 = Floor(360)

# Load the score font
font = pygame.font.Font("font/HANGTHEDJ.ttf", 70)
font2 = pygame.font.Font("font/HANGTHEDJ.ttf", 30)


while running:

    # Display images
    window.blit(background, (0, 0))
    window.blit(game.dragon.image, game.dragon.rect)
    game.all_towers1.draw(window)
    game.all_towers2.draw(window)

    # Display score
    point = font.render(f"{game.dragon.point}", 1, (0, 0, 0))
    text_width, text_height = font.size(f"{game.dragon.point}")
    window.blit(point, (180-(text_width//2), 10))

    # Generate high score message
    h_score = score_min_max(2)
    high_score = font2.render(f"High score: {h_score}", 1, (0, 0, 0))
    high_score_width, high_score_height = font2.size(f"High score: {h_score}")

    # Generate "Press SPACE to start !" mesage divided into 2 sections to seperate into 2 lines
    start_space_msg_line1 = font2.render("Press SPACE", 1, (0, 0, 0))
    start_space_msg_line1_width, start_space_msg_line1_height = font2.size("Press SPACE")
    start_space_msg_line2 = font2.render("to start !", 1, (0, 0, 0))
    start_space_msg_line2_width, start_space_msg_line2_height = font2.size("to start !")

    # Generate "Press ENTER !" message
    press_enter_msg = font2.render("Press ENTER !", 1, (0, 0, 0))
    press_enter_msg_width, press_enter_msg_height = font2.size("Press ENTER !")

    game.dragon.gravitate()
    game.game_over(window)

    if game.loose == True:
        if h_score != 0:
            window.blit(high_score, ((180 - high_score_width // 2), 490))
        window.blit(press_enter_msg, ((180 - press_enter_msg_width // 2), 420))

    if game.stop:
        window.blit(pause, (130, 220))

    for tower in game.all_towers1:
        tower.mouvement(1)

    for tower in game.all_towers2:
        tower.mouvement(2)

    game.dragon.rotation(game.ready)

    if game.go == True:
        window.blit(start_space_msg_line1, ((180 - start_space_msg_line1_width // 2), 400))
        window.blit(start_space_msg_line2, ((180 - start_space_msg_line2_width // 2), 400 + start_space_msg_line2_height + 5))

    if game.ready and not game.stop:
        floor.move()
        floor2.move()
        game.add_point()

    floor.sprite.draw(window)
    floor2.sprite.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # Exit game
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and (game.go == True or game.ready == True): # When space is pressed
                game.ready = True
                game.go = False
                game.jump()
            elif event.key == pygame.K_RIGHT:
                game.dragon.change_image()
            elif event.key == pygame.K_RETURN and not game.go:                          # When return is pressed
                game.start()
            elif event.key == pygame.K_ESCAPE:                                          # When escape is pressed
                if game.ready:
                    if game.stop:
                        game.stop = False
                    else:
                        game.stop = True

    clock.tick(60)          # Limit the game to 60fps
    pygame.display.flip()   # Update screen