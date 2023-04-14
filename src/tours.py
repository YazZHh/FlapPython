import pygame
import random

class Tours(pygame.sprite.Sprite):

    def __init__(self, Jeu, taille, x, y, boolen=True):
        super().__init__()
        self.jeu = Jeu

        self.taille = taille
        self.vitesse = 2.5
        self.bas = boolen
        
        self.image = pygame.image.load('img/tours.png')
        self.image = pygame.transform.scale(self.image, (80, self.taille))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.rotation()


    def deplacement(self):
        if self.jeu.pret and self.rect.x >= 0:
            self.rect.x -= self.vitesse

    def rotation(self):
        if not self.bas:
            self.image = pygame.transform.rotate(self.image, 180)
