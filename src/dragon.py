import pygame

class Dragon(pygame.sprite.Sprite):

    def __init__(self, Game):
        self.game = Game
        self.speed = -8
        
        # management of the image for the dragon
        self.curent_image = 1
        self.image = pygame.image.load("img/dragon.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 60
        self.rect.y = 200

        self.all_image = {
            1 : "img/dragon.png",
            2 : "img/dragon2.png",
            3 : "img/dragon3.png"
        }
        

        # image for the different position
        self.image_normal = self.image
        self.image_up = pygame.transform.rotate(self.image, 30)
        self.image_down = pygame.transform.rotate(self.image, -20)

        self.point = 0 # score of the player

    
    def change_image(self):
        if not self.game.ready:
            self.curent_image += 1
            if self.curent_image == 4:
                self.curent_image = 1
            self.image = pygame.image.load(self.all_image[self.curent_image])
            self.image = pygame.transform.scale(self.image, (60, 60))

        
    def gravite(self):
        """move the dragon on the axe y"""
        if self.game.ready:
            if self.rect.y < 470:
                self.rect.y += self.speed
                self.speed += 0.5
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
        if self.speed < 0 and game:
            self.image = self.image_up 
        elif self.speed > 0 and game:
            self.image = self.image_down
        else:
            self.image = self.image_normal