import math
import os

import pygame as pg
import pymunk as pm
from pymunk.pygame_util import *


class Player():
    def __init__(self, game, pos, size):
        # pg.sprite.Sprite.__init__(self)
        self.game = game
        self.body = pm.Body(body_type=pm.Body.DYNAMIC)
        self.body.position = pos
        self.size = size
        self.shape = pm.Poly.create_box(self.body, self.size)
        self.shape.mass = 10
        self.shape.elasticity = 0.1
        self.shape.friction = 0.1
        self.shape.color = (150, 255, 25, 0)
        self.game.space.add(self.body, self.shape)
        self.image =pg.Surface((size))
        self.shape.collision_type = 1
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos)


    def update(self):

        self.image = pg.transform.scale(self.image, self.size)
        self.image = pg.transform.rotate(self.image, -math.degrees(self.body.angle))
        self.rect.center = self.body.position
        self.game.screen.blit(self.image, (self.rect.centerx - self.image.get_width() / 2, self.rect.centery - self.image.get_height() / 2))







