import pygame as pg
from settings import *

class Dinosaur ():
    def __init__(self, game, pos, size):
        # pg.sprite.Sprite.__init__(self)
        self.game = game
        self.pos = pos
        self.size = size
        self.image = pg.image.load("img/dino.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos)
        self.gravity = 0



    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.bottom == SCREEN_HEIGHT- GROUND:
            self.gravity = -20

        if keys[pg.K_a]:
            self.rect.move_ip(-SPEED, 0)
        if keys[pg.K_d]:
            self.rect.move_ip(SPEED, 0)

        self.gravity += 1
        self.rect.move_ip(0, self.gravity)

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom >= SCREEN_HEIGHT- GROUND:
            self.rect.bottom = SCREEN_HEIGHT - GROUND



        self.game.screen.blit(self.image, (
        self.rect.centerx - self.image.get_width() / 2, self.rect.centery - self.image.get_height() / 2))


