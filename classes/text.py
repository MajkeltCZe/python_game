import pygame as pg


class Text:
    def __init__(self, game, pos, text1, text2, color):
        self.game = game
        self.pos = pos
        self.text1 = text1
        self.text2 = text2
        self.color = color

    def update(self):
        font = pg.font.SysFont('Ariel', 50)
        self.game.screen.blit(font.render(f'{self.text1} {self.text2}', True, self.color), self.pos)
