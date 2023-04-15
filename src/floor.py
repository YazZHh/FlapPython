import pygame

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/terre.jpg")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = 360 - self.width
        self.y = 600 - self.height
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.speed = -3
        self.sprite = pygame.sprite.Group()
        self.sprite.add(self)

    def move(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right < 0:
            self.rect.left = 360

    # def build(self):
    #     self.sprite = pygame.sprite.Group()
        