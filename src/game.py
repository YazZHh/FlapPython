import pygame
import random
from src.dragon import Dragon
from src.tours import Tours

class Game:

    def __init__(self):
        self.dragon = Dragon(self)

        self.toutes_tours1 = pygame.sprite.Group()
        self.toutes_tours2 = pygame.sprite.Group()

        self.pret = False

    def creation_tour(self):
        self.taille_tour = random.randint(50, 325)
        self.tour1 = Tours(self, self.taille_tour, 330, 0, False)
        self.tour2 = Tours(self, 375-self.taille_tour, 330, self.taille_tour + 175)
        self.toutes_tours1.add(self.tour1)
        self.toutes_tours1.add(self.tour2)
        
        self.taille_tour = random.randint(50, 325)
        self.tour3 = Tours(self, self.taille_tour, 560, 0, False)
        self.tour4 = Tours(self, 375-self.taille_tour, 560, self.taille_tour + 175)
        self.toutes_tours2.add(self.tour3)
        self.toutes_tours2.add(self.tour4)


    def start(self):
        if not self.pret:
            self.creation_tour()
            self.pret = True
        else:
            self.saut()

    def saut(self):
        if self.dragon.rect.y > 10:
            self.dragon.vitesse_descendante = -8
            self.dragon.image = self.dragon.image_up

    def respawn(self, pseudo):
        if pseudo == 1:
            self.taille_tour = random.randint(50, 325)
            self.tour1.rect.x = 360
            self.tour2.rect.x = 360
            self.tour1.rect.y = 0
            self.tour2.rect.y = self.taille_tour + 175
            self.tour1.image = pygame.transform.scale(self.tour1.image, (80, self.taille_tour))
            self.tour2.image = pygame.transform.scale(self.tour2.image, (80, 375 - self.taille_tour))
        else:
            self.taille_tour = random.randint(50, 325)
            self.tour3.rect.x = 360
            self.tour4.rect.x = 360
            self.tour3.rect.y = 0
            self.tour4.rect.y = self.taille_tour + 175
            self.tour3.image = pygame.transform.scale(self.tour3.image, (80, self.taille_tour))
            self.tour4.image = pygame.transform.scale(self.tour4.image, (80, 375 - self.taille_tour))
        self.dragon.point += 1
            

    def game_over(self):
        if self.dragon.rect.y >= 460 or self.dragon.check_collision(self.toutes_tours1) or self.dragon.check_collision(self.toutes_tours2):
            self.pret = False
            self.toutes_tours1 = pygame.sprite.Group()
            self.toutes_tours2 = pygame.sprite.Group()
            self.dragon.vitesse_descendante = -8
            self.dragon.reset()
            self.dragon.image = self.dragon.image_normal