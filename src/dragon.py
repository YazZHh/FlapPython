import pygame

class Dragon(pygame.sprite.Sprite):

    def __init__(self, Jeu):
        self.jeu = Jeu
        self.vitesse_descendante = -8
        
        # management of the image for the dragon
        self.image = pygame.image.load("img/dragon2.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 60
        self.rect.y = 200

        # image for the different position
        self.image_normal = self.image
        self.image_up = pygame.transform.rotate(self.image, 30)
        self.image_down = pygame.transform.rotate(self.image, -20)

        self.point = 0 # score of the player
        

    def gravite(self):
        """move the dragon on the axe y"""
        if self.jeu.ready:
            if self.rect.y < 470:
                self.rect.y += self.vitesse_descendante
                self.vitesse_descendante += 0.5
            if self.rect.y > 280:
                self.image = self.image_down

    def check_collision(self, group):
        """check if its a collision"""
        return pygame.sprite.spritecollide(self, group, False, pygame.sprite.collide_mask)
    
    def reset(self):
        """reset the setting of the dragon"""
        self.rect.x = 60
        self.rect.y = 200
        self.image = self.image_normal

    def rotation(self, game):
        """management of the image compared with the statue"""
        if self.vitesse_descendante < 0 and game:
            self.image = self.image_up 
        elif self.vitesse_descendante > 0 and game:
            self.image = self.image_down
        else:
            self.image = self.image_normal