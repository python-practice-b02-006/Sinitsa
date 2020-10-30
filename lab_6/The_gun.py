import numpy as np
import pygame as pg
from random import randint, gauss

pg.init()
pg.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_SIZE = (800, 600)


def rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


class Ball():
    pass

        
class Target():
    pass


class Gun():
    pass


class ScoreTable():
    pass


class Manager():
    def __init__(self):
        pass

    def process(self, events, screen):
        done = self.handle_events(events)
        return done

    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
        return done

    def draw(self, screen):
        pass


screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("The gun of Khiryanov")

done = False
clock = pg.time.Clock()

mgr = Manager()

while not done:
    clock.tick(15)
    screen.fill(BLACK)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()


pg.quit()
