import pygame as pg
from settings import *


class Background:
    def __init__(self, game, pos=(0, 0), width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
        self.game = game
        self.width = width
        self.height = height
        self.pos = pos
        self.image = pg.image.load("img/background.jpg").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos)




    def update(self):
        self.game.screen.blit(self.image, (self.rect.centerx - self.image.get_width() / 2, self.rect.centery - self.image.get_height() / 2))
