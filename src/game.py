import pygame
import random
from src.dragon import Dragon
from src.tours import Tours

pygame.init()

class Game:

    def __init__(self):
        self.dragon = Dragon(self)


        self.taille_tour = random.randint(100, 350)
        self.tour1 = Tours(self, self.taille_tour, 310, 0, False)
        self.tour2 = Tours(self, 500-self.taille_tour, 310, self.taille_tour + 150)
        self.taille_tour = random.randint(100, 350)
        self.tour3 = Tours(self, self.taille_tour, 510, 0, False)
        self.tour4 = Tours(self, 500-self.taille_tour, 510, self.taille_tour + 150)
        self.toutes_tours = pygame.sprite.Group()

        self.pret = False

    def creation_tour(self):
        self.toutes_tours.add(self.tour1)
        self.toutes_tours.add(self.tour2)
        self.toutes_tours.add(self.tour3)
        self.toutes_tours.add(self.tour4)
        self.taille_tour = random.randint(100, 350)
        self.tour1 = Tours(self, self.taille_tour, 310, 0, False)
        self.tour2 = Tours(self, 500-self.taille_tour, 310, self.taille_tour + 150)
        self.taille_tour = random.randint(100, 350)
        self.tour3 = Tours(self, self.taille_tour, 510, 0, False)
        self.tour4 = Tours(self, 500-self.taille_tour, 510, self.taille_tour + 150)
        

    def start(self):
        if not self.pret:
            self.creation_tour()
            self.pret = True
        else:
            self.saut()

    def saut(self):
        if self.dragon.rect.y > 10:
            self.dragon.vitesse_descendante = -8