import pygame

class Dragon(pygame.sprite.Sprite):

    def __init__(self, Jeu):
        self.jeu = Jeu
        self.vitesse_descendante = -8
        
        self.image = pygame.image.load("img/dragon.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 60
        self.rect.y = 100

        self.image_normal = self.image
        self.image_up = pygame.transform.rotate(self.image, 30)
        self.image_down = pygame.transform.rotate(self.image, -20)

    def gravite(self):
        if self.jeu.pret:
            if self.rect.y < 460:
                self.rect.y += self.vitesse_descendante
                self.vitesse_descendante += 0.45
            if self.rect.y > 280:
                self.image = self.image_down

    def check_collision(self, group):
        return pygame.sprite.spritecollide(self, group, False, pygame.sprite.collide_mask)
    