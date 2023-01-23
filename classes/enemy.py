import pygame as pg
from settings import *
from random import randint

'''
Třída vytváří nepřátelé, kteří se pohybujou po zemi
'''


class Enemy(pg.sprite.Sprite):
    def __init__(self, game):
        super(Enemy, self).__init__()
        self.game = game
        self.size = (20, 40)
        self.image = pg.image.load("img/alien.png").convert_alpha()
        self.rect = self.image.get_rect(
            center=(SCREEN_WIDTH, SCREEN_HEIGHT - GROUND - 20))
        self.speed = randint(3, 10)

    def update(self):
        # pohyb
        self.rect.move_ip(-self.speed, 0)

        # odstranění nepřítele, když zmizí z hrací plochy
        if self.rect.right < 0:
            self.kill()

        self.image = pg.transform.scale(self.image, self.size)
        self.game.screen.blit(self.image, (self.rect.centerx - self.image.get_width() / 2, self.rect.centery -
                                           self.image.get_height() / 2))
