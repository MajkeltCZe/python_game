import pygame as pg
from settings import *
from random import randint


class Enemy(pg.sprite.Sprite):
    def __init__(self, game):
        super(Enemy, self).__init__()
        self.game = game
        self.size = (40, 15)
        self.image =pg.image.load("img/bolt.png").convert()
        self.rect = self.image.get_rect(
            center=(randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 50), randint(0, SCREEN_HEIGHT)))
        self.speed = randint(3, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

        self.image = pg.transform.scale(self.image, self.size)
        self.game.screen.blit(self.image, (self.rect.centerx - self.image.get_width() / 2, self.rect.centery -
                                           self.image.get_height() / 2))
