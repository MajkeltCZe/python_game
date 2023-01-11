import os
import pygame as pg
import pymunk as pm
from pymunk.pygame_util import *
from settings import *
from random import randrange


class Obstacle(pg.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, game, pos, size, points):
        super(Obstacle, self).__init__()
        self.game = game
        self.pos = pos
        self.image = pg.Surface(size)
        self.rect = self.image.get_rect()
        moment = pm.moment_for_poly(1, points)
        body = pm.Body(20, moment, pm.Body.STATIC)
        body.position = pos
        shape = pm.Poly(body, points)
        shape.elasticity = 0.5
        shape.color = (255, 0, 0, 0)
        shape.collision_type = 2
        self.game.space.add(body, shape)

    def update(self):
        pass

    def update(self, events_list):
        self.pos += (10,10)
        super(Obstacle, self).update()