import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


def main():
    rect(screen, WHITE, [0, 0, 400, 400])  # Makes screen white.
    circle(screen, YELLOW, (200, 200), 100)  # Draws main face in fixed coordinates.
    rect(screen, BLACK, [150, 250, 100, 20]) # Draws mouth in fixed coordinates.
    draw_left_eye()
    draw_right_eye()
    draw_left_eyebrow(50, 100)
    draw_right_eyebrow(220, 65)
    
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True


def draw_left_eye():
    """
    Draws left eye in fixed coordinates.

    Returns
    -------
    None.

    """
    circle(screen, RED, (150, 160), 20)
    circle(screen, BLACK, (150, 160), 10)
    

def draw_right_eye():
    """
    Draws right eye in fixed coordinates.

    Returns
    -------
    None.

    """
    circle(screen, RED, (250, 160), 15)
    circle(screen, BLACK, (250, 160), 8)


def draw_left_eyebrow(x, y):
    """
    Draws left eyebrow in fixed coordinates.

    Parameters
    ----------
    x : TYPE int
        DESCRIPTION. x coordinate of top left corner of minimum rectangle(
        sides are parallel to coordinate axes) that consists the rectangle
        of eyebrow.
    y : TYPE int
        DESCRIPTION. y coordinate of top left corner of minimum rectangle(
        sides are parallel to coordinate axes) that consists the rectangle
        of eyebrow.

    Returns
    -------
    None.

    """
    surface = pygame.Surface([200, 100], pygame.SRCALPHA)
    rect(surface, BLACK, [0, 0, 100, 10])
    surface_rot = pygame.transform.rotate(surface, -30)
    screen.blit(surface_rot, [x, y])


def draw_right_eyebrow(x, y):
    """
    Draws right eyebrow in fixed coordinates.

    Parameters
    ----------
    x : TYPE int
        DESCRIPTION. x coordinate of top left corner of minimum rectangle(
        sides are parallel to coordinate axes) that consists the rectangle
        of eyebrow.
    y : TYPE int
        DESCRIPTION. y coordinate of top left corner of minimum rectangle(
        sides are parallel to coordinate axes) that consists the rectangle
        of eyebrow.

    Returns
    -------
    None.

    """
    surface = pygame.Surface([200, 100], pygame.SRCALPHA)
    rect(surface, BLACK, [0, 0, 90, 10])
    surface_rot = pygame.transform.rotate(surface, 25)
    screen.blit(surface_rot, [x, y])


main()
pygame.quit()
































