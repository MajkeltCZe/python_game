import pygame as p
from sys import exit


p.init()
screen = p.display.set_mode((800,400))
p.display.set_caption('Narrative Disaster')
clock = p.time.Clock()

while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            exit()
    p.display.update()
    clock.tick(60)