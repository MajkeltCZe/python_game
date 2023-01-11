import os
import pygame as pg
import pymunk as pm
from pymunk.pygame_util import *
from settings import *
from random import randrange


class Enemy(pg.sprite.Sprite):

    def __init__(self, game, pos, size):
        super(Enemy, self).__init__()
        self.game = game
        self.pos = pos
        self.body = pm.Body(body_type=pm.Body.DYNAMIC)
        self.image = pg.image.load("img/cze.png")
        self.rect = self.image.get_rect()
        self.rect.topleft(pos)



    def update(self, events_list):
        super(Enemy, self).update()

