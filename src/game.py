import pygame
import random
from src.dragon import Dragon
from src.tours import Tours

class Game:

    def __init__(self):
        self.dragon = Dragon(self)


        self.taille_tour = random.randint(100, 350)
        self.tour1 = Tours(self, self.taille_tour, 310, 0, False)
        self.tour2 = Tours(self, 400-self.taille_tour, 310, self.taille_tour + 150)
        self.toutes_tours1 = pygame.sprite.Group()

        self.taille_tour = random.randint(100, 350)
        self.tour3 = Tours(self, self.taille_tour, 510, 0, False)
        self.tour4 = Tours(self, 400-self.taille_tour, 510, self.taille_tour + 150)
        self.toutes_tours2 = pygame.sprite.Group()

        self.pret = False

    def creation_tour(self):
        self.toutes_tours1.add(self.tour1)
        self.toutes_tours1.add(self.tour2)
        self.taille_tour = random.randint(100, 350)
        self.tour1 = Tours(self, self.taille_tour, 310, 0, False)
        self.tour2 = Tours(self, 400-self.taille_tour, 310, self.taille_tour + 150)

        self.toutes_tours2.add(self.tour3)
        self.toutes_tours2.add(self.tour4)
        self.taille_tour = random.randint(100, 350)
        self.tour3 = Tours(self, self.taille_tour, 510, 0, False)
        self.tour4 = Tours(self, 400-self.taille_tour, 510, self.taille_tour + 150)


    def start(self):
        if not self.pret:
            self.creation_tour()
            self.pret = True
        else:
            self.saut()

    def saut(self):
        if self.dragon.rect.y > 10:
            self.dragon.vitesse_descendante = -8

    def respawn(self, pseudo):
        self.tour1 = Tours(self, self.taille_tour, 410, 0, False)
        self.tour2 = Tours(self, 400-self.taille_tour, 410, self.taille_tour + 150)
        if pseudo == 1:
            self.toutes_tours1.add(self.tour1)
            self.toutes_tours1.add(self.tour2)
            self.taille_tour = random.randint(100, 350)
            self.tour1 = Tours(self, self.taille_tour, 410, 0, False)
            self.tour2 = Tours(self, 400-self.taille_tour, 410, self.taille_tour + 150)
        else:
            self.toutes_tours2.add(self.tour1)
            self.toutes_tours2.add(self.tour2)
            self.taille_tour = random.randint(100, 350)
            self.tour1 = Tours(self, self.taille_tour, 410, 0, False)
            self.tour2 = Tours(self, 400-self.taille_tour, 410, self.taille_tour + 150)

    def game_over(self):
        if self.dragon.rect.y >= 460 or (self.dragon.check_collision(self.toutes_tours1) and self.dragon.check_collision(self.toutes_tours1)):
            self.pret = False
            self.toutes_tours1 = pygame.sprite.Group()
            self.toutes_tours2 = pygame.sprite.Group()
            self.dragon.vitesse_descendante = -8
            self.dragon.rect.x = 60
            self.dragon.rect.y = 100