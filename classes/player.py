import pygame as pg
from settings import *

class Ghost():
    def __init__(self, game, pos, size):
        # pg.sprite.Sprite.__init__(self)
        self.game = game
        self.pos = pos
        self.size = size
        self.image =pg.image.load("img/ghost.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos)


    def update(self):
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




        self.game.screen.blit(self.image, (self.rect.centerx - self.image.get_width() / 2, self.rect.centery - self.image.get_height() / 2))







