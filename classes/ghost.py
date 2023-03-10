import pygame as pg
from settings import *

'''
Třídá vytváří hráčovu postavu, tentokrát se jedná o ducha, který se dokáže pohyb po celé hrací ploše
'''


class Ghost(pg.sprite.Sprite):
    def __init__(self, game, pos, size=(40, 60)):
        super(Ghost, self).__init__()
        self.game = game
        self.pos = pos
        self.size = size
        self.image = pg.image.load("img/ghost.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):

        # reakce na zmáčknutí kláves
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.move_ip(0, -SPEED)
        if keys[pg.K_s]:
            self.rect.move_ip(0, SPEED)
        if keys[pg.K_a]:
            self.rect.move_ip(-SPEED, 0)
        if keys[pg.K_d]:
            self.rect.move_ip(SPEED, 0)

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0

        # vykreslení
        self.game.screen.blit(self.image, (
            self.rect.centerx - self.image.get_width() / 2, self.rect.centery - self.image.get_height() / 2))
