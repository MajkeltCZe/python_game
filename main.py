import pygame as pg
import random
from sys import exit
import pymunk
from settings import *
import pymunk.pygame_util

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pg.display.set_caption('Narrative Disaster')
        self.running = True

    def new(self):
        pass
    def events(self):
        self.events_list = pg.event.get()
        for event in self.events_list:
            if event.type == pg.QUIT:
                self.running = False


    def update(self):
        self.screen.fill("red")
        self.clock.tick(FPS)


    def run(self):
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