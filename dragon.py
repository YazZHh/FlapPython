import pygame


class Dragon(pygame.sprite.Sprite):

    def __init__(self, Jeu):

        self.jeu = Jeu
        self.vitesse = 1.5
        
        self.image = pygame.image.load('C:/Users/Noah/Documents/code/FlapPython/photos/dragon.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 300

    def gravite(self):
        if self.jeu.pret:
            if self.rect.y < 540:
                self.rect.y += self.vitesse

