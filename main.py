from src.dragon import Dragon
from src.game import Game
from src.floor import Floor
import pygame
import sys

pygame.init()

window = pygame.display.set_mode((360, 600))
background = pygame.image.load("img/fond.jpg")

clock = pygame.time.Clock()
running = True

game = Game()
floor = Floor()
floor2 = Floor(360)

while running:
    window.blit(background, (0, 0))
    window.blit(game.dragon.image, game.dragon.rect)
    game.toutes_tours.draw(window)

    game.dragon.gravite()

    for tour in game.toutes_tours:
        tour.deplacement()

    if game.pret:
        floor.move()
        floor2.move()
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
