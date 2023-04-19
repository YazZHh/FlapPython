from src.dragon import Dragon
from src.game import Game
from src.floor import Floor
import pygame
import sys

pygame.init()

window = pygame.display.set_mode((360, 600))
background = pygame.image.load("img/background.png")
background = pygame.transform.scale(background, (370, 620))

clock = pygame.time.Clock()
running = True

game = Game()
floor = Floor()
floor2 = Floor(360)

font = pygame.font.SysFont("monospace", 80)

while running:
    window.blit(background, (0, 0))
    window.blit(game.dragon.image, game.dragon.rect)
    game.toutes_tours1.draw(window)
    game.toutes_tours2.draw(window)

    point = font.render( f"{game.dragon.point}", 1 , (0,10,0))
    window.blit(point, (150,10))

    game.dragon.gravite()
    # game.game_over()

    for tour in game.toutes_tours1:
        tour.deplacement(1)

    for tour in game.toutes_tours2:
        tour.deplacement(2)

    game.dragon.rotation(game.pret)

    if game.pret:
        floor.move()
        floor2.move()
        game.add_point()
    floor.sprite.draw(window)
    floor2.sprite.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game.start()

    clock.tick(60)
    pygame.display.flip()
