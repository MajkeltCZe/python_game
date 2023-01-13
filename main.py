import pygame as pg
import random
from sys import exit
from settings import *
from classes.player import Ghost
from classes.dino import Dinosaur
from classes.score import Score
from random import randint
from classes.enemy import Enemy
from classes.background import Background

class Game:
    def __init__(self):
        pg.mixer.init()
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pg.display.set_caption('Narrative Disaster')
        self.enemies = pg.sprite.Group()
        self.running = True
        self.events_list = None
        self.generate_enemy = pg.USEREVENT + 1
        self.change = pg.USEREVENT + 2
        pg.time.set_timer(self.generate_enemy, 250)
        pg.time.set_timer(self.change, randint(3000, 15000))
        self.music = pg.mixer.music.load("music/ghost.ogg")
        self.playerType = 0
        #pg.mixer.music.play(loops=-1)
        #pg.mixer.music.set_volume(1)

    def collide(self):
        if pg.sprite.spritecollideany(self.player, self.enemies):
            pass





    def new(self):
        self.score = Score(self)
        self.background = Background(self)
        self.player = Ghost(self, (200, 80), (40, 60))


    def events(self):
        self.events_list = pg.event.get()
        for event in self.events_list:
            if event.type == pg.QUIT:
                self.running = False
            if event.type == self.change:
                print("change")

                self.cords = self.player.rect.topleft

                if self.playerType == 0:
                    self.playerType = 1
                    self.player = Dinosaur(self, self.cords, (160, 100))
                    print("dino")


                if self.playerType == 1:
                    self.playerType = 0
                    self.player = Ghost(self, self.cords, (40, 60))


            if event.type == self.generate_enemy:

               self.new_enemy = Enemy(self)
               self.enemies.add(self.new_enemy)






    def update(self):
        self.screen.fill(BLACK)
        self.clock.tick(FPS)
        self.background.update()
        for e in self.enemies:
            e.update()
        self.score.update()
        self.player.update()
        pg.display.update()
        self.collide()


    def run(self):
        self.new()
        while self.running:
            self.events()
            self.update()

        # close pygame
        pg.quit()
        pg.mixer.quit()

        exit()



def main():
    g = Game()
    g.run()


if __name__ == '__main__': main()