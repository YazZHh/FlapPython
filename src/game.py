import pygame
import random
from src.dragon import Dragon
from src.tower import towers
from src.score import *

class Game:

    def __init__(self):
        self.dragon = Dragon(self)

        # make a tuple of tower
        self.all_towers1 = pygame.sprite.Group()
        self.all_towers2 = pygame.sprite.Group()

        # settings for the first group
        self.size_tower = random.randint(50, 325)
        self.tower1 = towers(self, self.size_tower, 370, 0, False)
        self.tower2 = towers(self, 375-self.size_tower, 370, self.size_tower + 175)
        self.all_towers1.add(self.tower1)
        self.all_towers1.add(self.tower2)

        # settings for the second group
        self.size_tower = random.randint(50, 325)
        self.tower3 = towers(self, self.size_tower, 370, 0, False)
        self.tower4 = towers(self, 375-self.size_tower, 370, self.size_tower + 175)
        self.all_towers2.add(self.tower3)
        self.all_towers2.add(self.tower4)

        # The game is playing
        self.ready = False
        self.stop = False
        self.go = False

        # firts loose
        self.loose = True

    def make_tower(self):
        """Do appears the towers"""
        self.tower1.rect.x = 330
        self.tower2.rect.x = 330
        self.tower1.rect.y = 0
        self.tower2.rect.y = self.size_tower + 175
        self.tower1.image = pygame.transform.scale(self.tower1.image_normal, (80, self.size_tower))
        self.tower2.image = pygame.transform.scale(self.tower2.image_normal, (80, 375 - self.size_tower))

        self.size_tower = random.randint(50, 325)
        self.tower3.rect.x = 560
        self.tower4.rect.x = 560
        self.tower3.rect.y = 0
        self.tower4.rect.y = self.size_tower + 175
        self.tower3.image = pygame.transform.scale(self.tower3.image_normal, (80, self.size_tower))
        self.tower4.image = pygame.transform.scale(self.tower4.image_normal, (80, 375 - self.size_tower))
        

    def start(self):
        """settings to start the game and management the jump"""
        self.loose = False
        if not self.ready:
            self.make_tower()
            self.dragon.point = 0
            self.go = True

    def jump(self):
        if self.dragon.rect.y > 10 and self.ready and not self.stop:
            self.dragon.speed = -8
            self.dragon.image = self.dragon.image_up

    def respawn(self, pseudo):
        """move and change the size of the towers"""
        if pseudo == 1:
            self.size_tower = random.randint(50, 325)
            self.tower1.rect.x = 360
            self.tower2.rect.x = 360
            self.tower1.rect.y = 0
            self.tower2.rect.y = self.size_tower + 175
            self.tower1.image = pygame.transform.scale(self.tower1.image_normal, (80, self.size_tower))
            self.tower2.image = pygame.transform.scale(self.tower2.image_normal, (80, 375 - self.size_tower))
        else:
            self.size_tower = random.randint(50, 325)
            self.tower3.rect.x = 360
            self.tower4.rect.x = 360
            self.tower3.rect.y = 0
            self.tower4.rect.y = self.size_tower + 175
            self.tower3.image = pygame.transform.scale(self.tower3.image_normal, (80, self.size_tower))
            self.tower4.image = pygame.transform.scale(self.tower4.image_normal, (80, 375 - self.size_tower))
            
    def add_point(self):
        """"management of the points"""
        if self.tower1.rect.x == 81 or (self.tower3.rect.x == 81 or self.tower3.rect.x == 80):
            self.dragon.point += 1

    def game_over(self, window):
        """mangement of the settings for the game lost"""

        if self.dragon.rect.y >= 463 or self.dragon.check_collision(self.all_towers1) or self.dragon.check_collision(self.all_towers2):
            save_score(self.dragon.point)
            self.ready = False
            self.dragon.speed = -8
            self.dragon.image = self.dragon.image_normal
            self.tower1.rect.x = 370
            self.tower2.rect.x = 370
            self.tower3.rect.x = 370
            self.tower4.rect.x = 370
            self.blink_screen(window)
            self.dragon.reset()
            self.loose = True
            self.go = False


    def blink_screen(self, window):
        blank = pygame.Surface((360, 600))
        alpha_value = 125
        while alpha_value >= 0:
            blank.set_alpha(alpha_value)
            blank.fill((255, 255, 255))
            window.blit(blank, (0, 0))
            alpha_value -= 10
            pygame.display.flip()