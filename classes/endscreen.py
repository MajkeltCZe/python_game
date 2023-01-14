import pygame as pg
from settings import *
from classes.background import Background


class EndScreen(Background):
    def __init__(self, game, pos=(0, 0), width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
        super(EndScreen, self).__init__(game, pos=(0, 0), width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.image = pg.image.load("img/endscreen.jpg").convert()
        self.score = 10



