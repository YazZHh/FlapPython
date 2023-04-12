import pygame
import random


class Tours(pygame.sprite.Sprite):

    def __init__(self, Jeu, taille, y):
        super().__init__()
        self.jeu = Jeu

        self.taille = taille
        self.vitesse = 2
        
        self.image = pygame.image.load('C:/Users/Noah/Documents/code/FlapPython/photos/tours.png')
        self.image = pygame.transform.scale(self.image, (80, self.taille))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = random.randint(360, 400)


    def deplacement(self):
        if self.jeu.pret and self.rect.x >= 0:
            self.rect.x -= self.vitesse
