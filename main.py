import pygame as pg
import random
from sys import exit
from settings import *
from classes.ghost import Ghost
from classes.dino import Dinosaur
from classes.score import Score
from random import randint
from classes.enemy import Enemy
from classes.background import Background
from classes.endscreen import EndScreen
from classes.bolt import Bolt



class Game:
    def __init__(self):
        pg.mixer.init()
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pg.display.set_caption('Narrative Disaster')
        self.bolts = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.running = True
        self.events_list = None
        self.generate_bolt = pg.USEREVENT + 1
        self.generate_enemy = pg.USEREVENT + 1
        self.change = pg.USEREVENT + 2
        pg.time.set_timer(self.generate_bolt, 250)
        pg.time.set_timer(self.change, randint(3000, 15000))
        pg.time.set_timer(self.generate_enemy, randint(500, 3000))
        self.music = pg.mixer.music.load("music/ghost.ogg")
        self.playerType = 0
        self.end = False
        #pg.mixer.music.play(loops=-1)
        #pg.mixer.music.set_volume(1)

    def collide(self):
        if pg.sprite.spritecollideany(self.player, self.enemies):
            pass





    def new(self):
        self.score = Score(self)
        self.background = Background(self)
        self.player = Ghost(self, (200, 80), (40, 60))
        self.endscreen = EndScreen(self)


    def events(self):
        self.events_list = pg.event.get()
        for event in self.events_list:
            if event.type == pg.QUIT:
                self.running = False
            if self.end == False:
                if event.type == self.change:
                    self.cords = self.player.rect.topleft

                    if self.playerType == 1:
                        self.playerType = 0
                        self.player = Ghost(self, self.cords)

                    elif self.playerType == 0:
                        self.player = Dinosaur(self, self.cords)
                        self.playerType = 1

                    if self.playerType == 1 and self.cords[1] >= SCREEN_HEIGHT - GROUND:
                        #self.end = True
                        pass

                if event.type == self.generate_bolt:
                   self.new_enemy = Bolt(self)
                   self.bolts.add(self.new_enemy)

                if event.type == self.generate_enemy:
                    self.new_enemy = Enemy(self)
                    self.enemies.add(self.new_enemy)







    def update(self):
        self.screen.fill(BLACK)
        self.clock.tick(FPS)
        if self.end == False:
            self.background.update()
            for e in self.enemies:
                e.update()
            self.score.update()
            self.player.update()
            self.collide()
        else:
            self.endscreen.update()
            self.enemies.empty()
            self.player = None

        pg.display.update()

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