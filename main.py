import pygame as pg
import random
from sys import exit
import pymunk as pm
from settings import *
import pymunk.pygame_util

from classes.player import Player
from classes.enemy import Enemy
from classes.background import Background
from classes.obstacle import Obstacle

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pg.display.set_caption('Narrative Disaster')
        self.draw_options = pm.pygame_util.DrawOptions(self.screen)
        self.running = True
        self.events_list = None
        self.space = pm.Space()
        self.space.gravity = (0, 250)
        self.space.damping = 0.7
        self.dt = 1 / FPS
        self.obstacles = pg.sprite.Group()
        self.handler = self.space.add_collision_handler(1, 2)
        self.handler.begin = self.collide

    def collide(self, arbiter, space, data):
        arbiter.shapes[1].body.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        print('hit')
        return True
    def new(self):
       # self.enemy = Enemy(self, (200, 300), (400, 400), points=[(10, 0), (380, 40), (355, 314), (154, 215)])
        self.background = Background(self)
        self.player = Player(self, (200, 80), (20, 50))
        #self.obstacle1 = Obstacle(self, (random.randrange(100,SCREEN_WIDTH - 100), random.randrange(100,SCREEN_HEIGHT - 100)), (400, 400), points=[(0, 0), (0, 40), (355, 314), (154, 215)])
        #self.obstacle2 = Obstacle(self, (500, 700), (300, 400), points=[(0, 0), (0, 40), (355, 314), (154, 215)])
    def events(self):
        self.events_list = pg.event.get()
        for event in self.events_list:
            if event.type == pg.QUIT:
                self.running = False

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.player.body.position = pm.Vec2d(self.player.body.position[0] - 5, self.player.body.position[1])
        if keys[pg.K_RIGHT] :
            self.player.body.position = pm.Vec2d(self.player.body.position[0] + 5, self.player.body.position[1])
        if keys[pg.K_UP]:
            self.player.body.position = pm.Vec2d(self.player.body.position[0], self.player.body.position[1] - 5)
        if keys[pg.K_DOWN]:
            self.player.body.position = pm.Vec2d(self.player.body.position[0], self.player.body.position[1] + 5)

        if self.player.body.position[0] < 0:
            self.player.body.position = pm.Vec2d(self.player.body.position[0] + 6, self.player.body.position[1])


        if self.player.body.position[1] > SCREEN_WIDTH:
            self.player.body.position = pm.Vec2d(self.player.body.position[0] - 10, self.player.body.position[1])
            print("far goone")

    def update(self):
        self.screen.fill(BLACK)
        self.clock.tick(FPS)

        self.player.update()
        self.space.debug_draw(self.draw_options)
        pg.display.update()

    def run(self):
        self.new()
        while self.running:
            for _ in range(10):
                self.space.step(self.dt / 10)
            self.events()
            self.update()

        # close pygame
        pg.quit()
        exit()




def main():
    g = Game()
    g.run()


if __name__ == '__main__': main()