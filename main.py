import pygame as pg
from sys import exit
from settings import *
from classes.ghost import Ghost
from classes.dino import Dinosaur
from classes.enemy import Enemy
from classes.bolt import Bolt
from classes.background import Background
from classes.text import Text
from random import randint


class Game:
    def __init__(self):
        pg.mixer.init()
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pg.display.set_caption('Narrative Disaster')
        pg.mixer.music.load("music/music.ogg")
        pg.mixer.music.play(loops=-1)
        pg.mixer.music.set_volume(0.5)
        self.running = True
        self.score = None
        self.events_list = None
        self.end = False
        self.lives = 3
        self.playerType = 0
        self.generate_bolt = pg.USEREVENT + 1
        self.generate_enemy = pg.USEREVENT + 2
        self.change = pg.USEREVENT + 3
        self.enemies = pg.sprite.Group()
        self.bolts = pg.sprite.Group()
        self.allSprites = pg.sprite.Group()
        self.playerSprite = pg.sprite.GroupSingle()
        pg.time.set_timer(self.generate_bolt, 500)
        pg.time.set_timer(self.generate_enemy, randint(1000, 5000))
        pg.time.set_timer(self.change, randint(3000, 15000))

    def collide(self):
        if pg.sprite.groupcollide(self.playerSprite, self.enemies, False, True):
            self.lives -= 1
        if pg.sprite.groupcollide(self.playerSprite, self.bolts, False, True) and self.playerType == 0:
            self.lives -= 1
        if self.lives == 0:
            self.end = True

    def new(self):
        self.score = Text(self, (5, 5), 'score:', 0, BLACK)
        self.livesDisplay = Text(self, (5, 50), 'lives:', self.lives, BLACK)
        self.background = Background(self)
        self.player = Ghost(self, (50, 530))
        self.playerSprite.add(self.player)

    def events(self):
        self.events_list = pg.event.get()
        for event in self.events_list:
            if event.type == pg.QUIT:
                self.running = False
            if not self.end:
                if event.type == self.change:
                    self.cords = self.player.rect.topleft
                    if self.playerType == 1:
                        self.player = Ghost(self, self.cords)
                        self.playerSprite.add(self.player)
                        self.playerType = 0
                    elif self.playerType == 0:
                        self.player = Dinosaur(self, self.cords)
                        self.playerSprite.add(self.player)
                        self.playerType = 1
                    if self.playerType == 1 and self.cords[1] >= SCREEN_HEIGHT - GROUND:
                        self.end = True
                if event.type == self.generate_bolt:
                    self.new_enemy = Bolt(self)
                    self.bolts.add(self.new_enemy)
                    self.allSprites.add(self.new_enemy)
                if event.type == self.generate_enemy:
                    self.newEnemy = Enemy(self)
                    self.enemies.add(self.newEnemy)
                    self.allSprites.add(self.newEnemy)

    def update(self):
        self.screen.fill(BLACK)
        self.clock.tick(FPS)
        if not self.end:
            self.time = int(pg.time.get_ticks() / 1000)
            self.score.text2 = self.time
            self.livesDisplay.text2 = self.lives
            self.background.update()
            for e in self.allSprites:
                e.update()
            self.player.update()
            self.collide()
        else:
            self.allSprites.empty()
            self.score = Text(self, (SCREEN_WIDTH / 2 - 40, SCREEN_HEIGHT / 2), 'score:', self.time, WHITE)
            pg.mixer.quit()
        self.livesDisplay.update()
        self.score.update()
        pg.display.update()

    def run(self):
        self.new()
        while self.running:
            self.events()
            self.update()
        pg.quit()
        pg.mixer.quit()
        exit()


def main():
    g = Game()
    g.run()


if __name__ == '__main__':
    main()
