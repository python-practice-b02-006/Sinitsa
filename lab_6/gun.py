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
    '''
    The ball class. Creates a ball, controls it's movement and implement it's rendering.
    '''
    pass
        
class Target():
    pass


class Gun():
    def __init__(self, coord=[30, SCREEN_SIZE[1]//2], max_pow=50, min_pow=10, color=RED):
        self.coord = coord
        self.angle = 0
        self.max_pow = max_pow
        self.min_pow = min_pow
        self.color = color
        self.active = False
        self.pow = min_pow
        
    def draw(self, screen):
        gun_shape = []
        vec_1 = np.array([int(5*np.cos(self.angle - np.pi/2)), int(5*np.sin(self.angle - np.pi/2))])
        vec_2 = np.array([int(self.pow*np.cos(self.angle)), int(self.pow*np.sin(self.angle))])
        gun_pos = np.array(self.coord)
        gun_shape.append((gun_pos + vec_1).tolist())
        gun_shape.append((gun_pos + vec_1 + vec_2).tolist())
        gun_shape.append((gun_pos + vec_2 - vec_1).tolist())
        gun_shape.append((gun_pos - vec_1).tolist())
        pg.draw.polygon(screen, self.color, gun_shape)
    
    def move(self, inc):
        if (self.coord[1] > 30 or inc > 0) and (self.coord[1] < SCREEN_SIZE[1] - 30 or inc < 0):
            self.coord[1] += inc
            
    def set_angle(self, target_pos):
        self.angle = np.arctan2(target_pos[1] - self.coord[1], target_pos[0] - self.coord[0])
            
    def strike(self):
        pass

class Table():
    pass


class Manager():
    def __init__(self):
        self.gun = Gun()
        self.table = Table()

    def process(self, events, screen):
        done = self.handle_events(events)
        
        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)
            
        self.draw(screen)
        return done
    
    def draw(self, screen):
        screen.fill(BLACK)
        self.gun.draw(screen)

    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.gun.move(-5)
                elif event.key == pg.K_DOWN:
                    self.gun.move(5)
            
            
        return done



screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("The gun of Khiryanov")

done = False
clock = pg.time.Clock()

mgr = Manager()

while not done:
    clock.tick(15)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()


pg.quit()
