import pygame

class Dragon(pygame.sprite.Sprite):

    def __init__(self, Jeu):
        self.jeu = Jeu
        self.vitesse_descendante = -8
        self.image = pygame.transform.scale(pygame.image.load("img/dragon.png"), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 60
        self.rect.y = 100

    def gravite(self):
        if self.jeu.pret:
            if self.rect.y < 460:
                self.rect.y += self.vitesse_descendante
                self.vitesse_descendante += 0.45

    def check_collision(self, group):
        return pygame.sprite.spritecollide(self, group, False, pygame.sprite.collide_mask)