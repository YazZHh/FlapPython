import pygame
import random

class Tours(pygame.sprite.Sprite):

    def __init__(self, Jeu, taille, x, y, boolen=True):
        super().__init__()
        self.jeu = Jeu

        self.taille = taille
        self.vitesse = 2.65
        self.bas = boolen

        self.image = pygame.image.load('img/towers.png')
        self.image = pygame.transform.scale(self.image, (80, self.taille))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.image_normal = pygame.transform.scale(self.image, (80, self.taille))

        self.rotation()


    def deplacement(self, pseudo):
        if self.jeu.pret:
            if self.rect.x >= -85:
                self.rect.x -= self.vitesse
            elif self.rect.x <= -85:
                self.jeu.respawn(pseudo)


    def rotation(self):
        if not self.bas:
            self.image = pygame.transform.rotate(self.image, 180)
            self.image_normal = pygame.transform.scale(self.image, (80, self.taille))
