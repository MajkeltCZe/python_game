import os
import pygame as pg
from settings import *

class Score():
    def __init__(self, game):
        self.game = game
        self.score = 0




    def update(self):
        self.now = round(pg.time.get_ticks() / 1000, 0)
        self.time = pg.time.Clock().get_fps()

        if self.now:  self.score += 1

        #print(self.now)

        font = pg.font.Font('freesansbold.ttf', 30)
        txt = font.render(f'score: {self.score}', True, BLACK)
        self.game.screen.blit(txt, (5,5))
