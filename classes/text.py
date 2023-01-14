import pygame as pg
from settings import *


class Text:
    def __init__(self, game, pos, text1, text2, color):
        self.game = game
        self.pos = pos
        self.text1 = text1
        self.text2 = text2
        self.color = color


    def update(self):
        font = pg.font.Font('freesansbold.ttf', 30)

        self.game.screen.blit(font.render(f'{self.text1} {self.text2}', True, self.color), self.pos)
