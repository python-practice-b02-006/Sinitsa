import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
screen_width = 1000
screen_hight = 600
screen = pygame.display.set_mode((screen_width, screen_hight))

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (0, 128, 255)
DARK_BLUE = (0, 0, 255)
BROWN = (128, 64, 0)
GRAY = (128, 128, 128)
PINK = (255, 128, 255)


def main():
    clock = pygame.time.Clock()
    finished = False
    
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        sky_hight = 0.4 * screen_hight
        draw_sky(sky_hight)
        
        sea_hight = 0.3 * screen_hight
        draw_sea(sky_hight, sea_hight)
        
        beach_hight = 0.3 * screen_hight
        draw_beach(beach_hight)
        
        xsun = 0.9 * screen_width
        ysun = sky_hight / 3
        rsun = sky_hight / 6
        draw_sun(xsun, ysun, rsun)
        
        xcloud = 0.25 * screen_width
        ycloud = sky_hight / 3
        cloud_width = 0.125 * screen_width
        draw_cloud(xcloud, ycloud, cloud_width)
        
        xship = 0.5 * screen_width
        yship = sky_hight + sea_hight / 2
        ship_hight = 0.3 * screen_hight
        ship_width = 0.4 * screen_width
        draw_ship(xship, yship, ship_width, ship_hight)
        
        xumbrella = 0.05 * screen_width
        yumbrella = sky_hight + sea_hight + beach_hight * 0.8
        umbrella_hight = 5 / 12 * screen_hight
        umbrella_width = 0.2 * screen_width
        draw_umbrella(xumbrella, yumbrella, umbrella_width, umbrella_hight)
        
        pygame.display.update()


def draw_sky(h):    
    """
    Draws LIGHT_BLUE sky.

    Parameters
    ----------
    x : TYPE float
        DESCRIPTION. The hight of the sky.

    Returns
    -------
    None.

    """    
    rect(screen, LIGHT_BLUE, [0, 0, screen_width, h])


def draw_sea(y, h):
    """
    Draws DARK_BLUE sea.

    Parameters
    ----------
    y : TYPE float
        DESCRIPTION. y coordinate of top left coner of the sea.
    h : TYPE float
        DESCRIPTION. The hight of the sea.

    Returns
    -------
    None.

    """
    rect(screen, DARK_BLUE, [0, y, screen_width, h])


def draw_beach(h):
    """
    Draws YELLOW beach.

    Parameters
    ----------
    h : TYPE float
        DESCRIPTION. The hight of the beach.

    Returns
    -------
    None.

    """    
    rect(screen, YELLOW, [0, screen_hight - h, screen_width, h])


def draw_sun(x, y, r):
    """
    Draws sun on the sky.

    Parameters
    ----------
    x : TYPE float
        DESCRIPTION. x coordinate of sun's center.
    y : TYPE float
        DESCRIPTION. y coordinate of sun's center.
    r : TYPE float
        DESCRIPTION. Radius of the sun.

    Returns
    -------
    None.

    """
    circle(screen, YELLOW, [int(x), int(y)], int(r))


def draw_cloud(x, y, w):
    """
    Draws cloud on the sky.

    Parameters
    ----------
    x : TYPE float
        DESCRIPTION. Bottom left x coordinate of a rectangle in which the 
        cloud is inscribed.
    y : TYPE float
        DESCRIPTION. Bottom left y coordinate of a rectangle in which the 
        cloud is inscribed.
    w : TYPE float
        DESCRIPTION. A width of a rectangle in which the cloud is inscribed
        (along x coordinate axix). A hight equals 6/13 * w. 

    Returns
    -------
    None.

    """
    fragment_radius = int(w / 6.5)
    circle(screen, WHITE, [int(x + 7/4 * fragment_radius),
                           int(y + 2 * fragment_radius)], fragment_radius)
    circle(screen, GRAY, [int(x + 7/4 * fragment_radius),
                           int(y + 2 * fragment_radius)], fragment_radius, 1)
    circle(screen, WHITE, [int(x + 13/4 * fragment_radius), 
                           int(y + 2 * fragment_radius)], fragment_radius)
    circle(screen, GRAY, [int(x + 13/4 * fragment_radius), 
                           int(y + 2 * fragment_radius)], fragment_radius, 1)
    circle(screen, WHITE, [int(x + fragment_radius), 
                           int(y + 3/2 * fragment_radius)], fragment_radius)
    circle(screen, GRAY, [int(x + fragment_radius), 
                           int(y + 3/2 * fragment_radius)], fragment_radius,
                                                                            1)
    circle(screen, WHITE, [int(x + 2.5 * fragment_radius), 
                           int(y + fragment_radius)], fragment_radius)
    circle(screen, GRAY, [int(x + 2.5 * fragment_radius), 
                           int(y + fragment_radius)], fragment_radius, 1)
    circle(screen, WHITE, [int(x + 4 * fragment_radius),
                           int(y + fragment_radius)], fragment_radius)
    circle(screen, GRAY, [int(x + 4 * fragment_radius),
                           int(y + fragment_radius)], fragment_radius, 1)
    circle(screen, WHITE, [int(x + 19/4 * fragment_radius), 
                           int(y + 2 * fragment_radius)], fragment_radius)
    circle(screen, GRAY, [int(x + 19/4 * fragment_radius), 
                           int(y + 2 * fragment_radius)], fragment_radius, 1)
    circle(screen, WHITE, [int(x + 5.5 * fragment_radius), 
                           int(y + fragment_radius)], fragment_radius)
    circle(screen, GRAY, [int(x + 5.5 * fragment_radius), 
                           int(y + fragment_radius)], fragment_radius, 1)


def draw_ship(x, y, w, h):
    """
    Draws ship in the sea.

    Parameters
    ----------
    x : TYPE float
        DESCRIPTION. Bottom left x coordinate of a rectangle in which the ship
        is inscribed.
    y : TYPE float
        DESCRIPTION. Bottom left y coordinate of a rectangle in which the ship
        is inscribed.
    w : TYPE float
        DESCRIPTION. A width of a rectangle in which the ship is inscribed
        (along x coordinate axix).
    h : TYPE float
        DESCRIPTION. A hight of a rectangle in which the ship is inscribed
        (along y coordinate axix).

    Returns
    -------
    None.

    """
    draw_deck(x, y, w, 0.3*h)
    draw_sails(x + 0.4*w, y - 0.3*h, 0.25 * w, 0.7 * h)
    
    
def draw_deck(x, y, w, h):
    """
    Draws ship's deck.

    Parameters
    ----------
    x : TYPE float
        DESCRIPTION. Bottom left x coordinate of a rectangle in which the 
        ship's deck is inscribed.
    y : TYPE float
        DESCRIPTION. Bottom left y coordinate of a rectangle in which the 
        ship's deck is inscribed.
    w : TYPE float
        DESCRIPTION. A width of a rectangle in which the ship's deck is
        inscribed(along x coordinate axix).
    h : TYPE float
        DESCRIPTION. A hight of a rectangle in which the ship's deck is
        inscribed(along y coordinate axix).

    Returns
    -------
    None.

    """
    #circle(screen, BROWN, [int(x + h), int(y - h)], int(h), 0, False, False,
    #       True, False)  Why doesn't it work???
    arc(screen, BROWN, [x, y - 2*h, 2*h, 2*h], np.pi, 3/2 * np.pi, int(h))
    rect(screen, BROWN, [x + h, y - h, 0.6 * w, h])
    polygon(screen, BROWN, [(x + 0.6*w + h, y - h), (x + w, y - h), 
                            (x + 0.6*w + h, y)])
    line(screen, BLACK, (x + 0.6*w + h, y - h), (x + 0.6*w + h, y))
    line(screen, BLACK, (x + h, y - h), (x + h, y))
    incircle_radius = 1/2 * (0.4*w - np.sqrt((0.4*w - h)**2 + h**2)) #A radius 
  # of circle inscribed in right triangle of ship's deck.
    circle(screen, BLACK, (int(x + h + 0.6*w + incircle_radius), int(y - h + 
                           incircle_radius)), int(0.8 * incircle_radius))
    circle(screen, WHITE, (int(x + h + 0.6*w + incircle_radius), int(y - h + 
                           incircle_radius)), int(0.6 * incircle_radius))
    
    
def draw_sails(x, y, w, h):
    """
    Draws ship's sails.

    Parameters
    ----------
    x : TYPE float
        DESCRIPTION. Bottom left x coordinate of a rectangle in which the 
        ship's sails are inscribed.
    y : TYPE float
        DESCRIPTION. Bottom left y coordinate of a rectangle in which the 
        ship's sails are inscribed.
    w : TYPE float
        DESCRIPTION. A width of a rectangle in which the ship's sails are
        inscribed(along x coordinate axix).
    h : TYPE float
        DESCRIPTION. A hight of a rectangle in which the ship's sails are
        inscribed(along y coordinate axix).

    Returns
    -------
    None.

    """
    rect(screen, BLACK, [x, y - h, 0.05 * w, h])
    polygon(screen, GRAY, [(x + 0.05*w, y), (x + w, y - h/2), 
                           (x + 0.05*w, y - h), (x + w/3, y - h/2)])
    line(screen, BLACK, (x + w/3, y - h/2), (x + w, y - h/2))


def draw_umbrella(x, y, w, h):
    """
    Draws umbrella on the beach.

    Parameters
    ----------
    x : TYPE float
        DESCRIPTION. Bottom left x coordinate of a rectangle in which the 
        umbrella is inscribed.
    y : TYPE float
        DESCRIPTION. Bottom left y coordinate of a rectangle in which the 
        umbrella is inscribed.
    w : TYPE float
        DESCRIPTION. A width of the umbrella(along x coordinate axix).
    h : TYPE float
        DESCRIPTION. A hight of the umbrella(along y coordinate axix).

    Returns
    -------
    None.

    """
    rect(screen, BROWN, [x + 0.475*w, y - h, 0.05 * w, h])
    polygon(screen, PINK, [(x, y - 0.8*h), (x + 0.475*w, y - h), 
                           (x + 0.525*w, y - h), (x + w, y - 0.8*h)])
    for i in range(4):
        line(screen, BLACK, (x + 0.475*w, y - h), (x + (i + 1)/4 * 0.475*w,
                                                   y - 0.8*h))
    for i in range(4):
        line(screen, BLACK, (x + 0.525*w, y - h), (x + 0.525*w + i/4 *
                                                   0.475*w, y - 0.8*h))
    

main()
pygame.quit()
