import pygame
import random

class towers(pygame.sprite.Sprite):

    def __init__(self, Game, size, x, y, boolen=True):
        super().__init__()
        self.game = Game

        self.size = size
        self.vitesse = 2.65
        self.bas = boolen

        # management of the image for the towers
        self.image = pygame.image.load('img/towers.png')
        self.image = pygame.transform.scale(self.image, (80, self.size))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.image_normal = pygame.transform.scale(self.image, (80, self.size))

        self.rotation()


    def deplacement(self, pseudo):
        """move the towers on the axe x"""
        if self.game.ready and not self.game.stop:
            if self.rect.x >= -85:
                self.rect.x -= self.vitesse
            elif self.rect.x <= -85:
                self.game.respawn(pseudo)


    def rotation(self):
        """do a rotation of 180°"""
        if not self.bas:
            self.image = pygame.transform.rotate(self.image, 180)
            self.image_normal = pygame.transform.scale(self.image, (80, self.size))
