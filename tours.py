import pygame


class Tours(pygame.sprite.Sprite):

    def __init__(self, Jeu, taille, y):
        super().__init__()
        self.jeu = Jeu

        self.taille = taille
        
        self.image = pygame.image.load('C:/Users/Noah/OneDrive/PGM/trophé nsi/trophés_nsi/photos/tours.png')
        self.image = pygame.transform.scale(self.image, (80, self.taille))
        self.rect = self.image.get_rect()
        self.rect.y = y
