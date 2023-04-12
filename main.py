from dragon import Dragon
from jeu import Jeu
import pygame

pygame.init()

window = pygame.display.set_mode((360,600))
background = pygame.image.load("photos/fond.jpg")
jeu = Jeu()

temps = pygame.time.Clock()
running = True

while running:
    window.blit(background, (0, 0))
    window.blit(jeu.dragon.image, jeu.dragon.rect)
    jeu.toutes_tours.draw(window)

    jeu.dragon.gravite()
    for tour in jeu.toutes_tours:
        tour.deplacement()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jeu.debut()

    temps.tick(60)
    pygame.display.flip()