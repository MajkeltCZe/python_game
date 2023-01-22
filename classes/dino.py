import pygame as pg
from settings import *


class Dinosaur(pg.sprite.Sprite):
    def __init__(self, game, pos, size=(160, 100)):
        super(Dinosaur, self).__init__()
        self.game = game
        self.pos = pos
        self.size = size
        self.images = ["img/dino.png", "img/dino_jump.png"]
        self.right = ["img/dino_right1.png", "img/dino_right2.png"]
        self.left = ["img/dino_left1.png", "img/dino_left2.png"]
        self.image = pg.image.load(self.images[0]).convert_alpha()
        self.index = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.gravity = 0
        self.speed = SPEED - 2

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.bottom == SCREEN_HEIGHT - GROUND:
            self.image = pg.image.load(self.images[1]).convert_alpha()
            self.gravity = -20

        if keys[pg.K_d]:
            self.rect.move_ip(self.speed, 0)
            self.index += 0.1
            if self.index >= len(self.right):
                self.index = 0
            if self.rect.bottom == SCREEN_HEIGHT - GROUND:
                self.image = pg.image.load(self.right[int(self.index)]).convert_alpha()

        if keys[pg.K_a]:
            self.rect.move_ip(-self.speed, 0)
            self.index += 0.1
            if self.index >= len(self.left):
                self.index = 0
            if self.rect.bottom == SCREEN_HEIGHT - GROUND:
                self.image = pg.image.load(self.left[int(self.index)]).convert_alpha()

        if not keys[pg.K_d] and not keys[pg.K_w] and not keys[pg.K_a]:
            self.image = pg.image.load(self.images[0]).convert_alpha()

        self.gravity += 1
        self.rect.move_ip(0, self.gravity)

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom >= SCREEN_HEIGHT - GROUND:
            self.rect.bottom = SCREEN_HEIGHT - GROUND

        self.game.screen.blit(self.image, (
            self.rect.centerx - self.image.get_width() / 2, self.rect.centery - self.image.get_height() / 2))
