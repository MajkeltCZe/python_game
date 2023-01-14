import pygame as pg
from settings import *


class Score:
    def __init__(self, game):
        self.game = game
        self.now = pg.time.get_ticks()

    def update(self):
        self.now = int(pg.time.get_ticks() / 1000)
        font = pg.font.Font('freesansbold.ttf', 30)
        txt = font.render(f'score: {self.now}', True, BLACK)
        self.game.screen.blit(txt, (5, 5))
