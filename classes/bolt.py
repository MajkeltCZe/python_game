import pygame as pg
from settings import *
from random import randint
from classes. enemy import Enemy


class Bolt(Enemy):
    def __init__(self, game):
        super(Bolt, self).__init__(game)
        self.size = (40, 15)
        self.number = randint(0,2)
        self.images = ["img/bolt.png", "img/yellow_bolt.png", "img/green_bolt.png"]
        self.image =pg.image.load(self.images[self.number]).convert_alpha()
        self.rect = self.image.get_rect(
            center=(randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 50), randint(0, SCREEN_HEIGHT - GROUND - 5)))
        self.speed = randint(3, 20)


