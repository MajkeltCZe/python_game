import pygame as pg
import random
from sys import exit
from settings import *
from classes.player import Player
from classes.enemy import Enemy
from classes.background import Background

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pg.display.set_caption('Narrative Disaster')
        self.enemies = pg.sprite.Group()
        self.running = True
        self.events_list = None
        self.generate_enemy = pg.USEREVENT +1
        self.lives = 3
        pg.time.set_timer(self.generate_enemy, 250)


    def collide(self):
        if pg.sprite.spritecollideany(self.player, self.enemies):
            print("hit")

    def new(self):
        self.player = Player(self, (200, 80), (40, 60))
        self.enemy = Enemy(self)
    def events(self):
        self.events_list = pg.event.get()
        for event in self.events_list:
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == self.generate_enemy:
                self.new_enemy = Enemy(self)
                self.enemies.add(self.new_enemy)






    def update(self):
        self.screen.fill(BLACK)
        self.clock.tick(FPS)
        self.player.update()
        for e in self.enemies:
            e.update()
        pg.display.update()
        self.collide()
           # self.running = False


    def run(self):
        self.new()
        while self.running:
            self.events()
            self.update()

        # close pygame
        pg.quit()
        exit()



def main():
    g = Game()
    g.run()


if __name__ == '__main__': main()