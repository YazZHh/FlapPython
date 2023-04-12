from dragon import Dragon
from jeu import Jeu
import pygame
pygame.init()


fenetre = pygame.display.set_mode((360,600))
arriere_plan = (255, 255, 255)
jeu = Jeu()

temps = pygame.time.Clock()
etat = True
while etat:
    fenetre.fill(arriere_plan)
    fenetre.blit(jeu.dragon.image, jeu.dragon.rect)
    jeu.toutes_tours.draw(fenetre)

    jeu.dragon.gravite()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            etat = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jeu.debut()

    temps.tick(60)
    pygame.display.flip()