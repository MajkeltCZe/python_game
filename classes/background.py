import pygame as pg
import pymunk as pm
from pymunk.pygame_util import *
from settings import *


class Background:
    def __init__(self, game, pos=(0, 0), width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
        self.game = game
        self.width = width
        self.height = height
        self.pos = pos
        self.create_boundaries()

    def create_boundaries(self):
        rects = [
            [(self.width / 2 + self.pos[0], self.height - 25 + self.pos[1]), (self.width, 50)],
            [(self.width / 2 + self.pos[0], 25 + self.pos[1]), (self.width, 50)],

        ]

        for pos, size in rects:
            body = pm.Body(body_type=pm.Body.STATIC)
            body.position = pos
            shape = pm.Poly.create_box(body, size)
            shape.elasticity = 0.4
            shape.friction = 0.5
            self.game.space.add(body, shape)