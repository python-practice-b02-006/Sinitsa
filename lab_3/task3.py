import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30

screen_width = 1000
screen_hight = 680
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
        sky_hight = 0.5 * screen_hight
        sea_hight = 0.225 * screen_hight
        beach_hight = 0.275 * screen_hight
        
        #Sea
        draw_sea(sky_hight, sea_hight)
        
        #Beach
        draw_beach(beach_hight)
        
        #Waves
        waves_number = 14
        wave_angle = 90
        draw_waves(screen_hight - beach_hight, waves_number, wave_angle)
        
        #Sky
        draw_sky(sky_hight)  #The sky is drawn after waves, because if waves 
        #are too big, there may be problems.
        
        #Sun
        xsun = 0.9 * screen_width
        ysun = sky_hight / 3
        inside_sun_radius = sky_hight / 5
        outside_sun_radius = sky_hight / 4
        rays_number = 50
        draw_sun(xsun, ysun, inside_sun_radius, outside_sun_radius, 
                 rays_number)
        
        #Clouds:
        #Cloud1
        xcloud1 = 0.2 * screen_width
        ycloud1 = 0.33 * sky_hight
        cloud_width1 = 0.15 * screen_width
        cloud_fragment_oblateness1 = 1
        draw_cloud(xcloud1, ycloud1, cloud_width1, cloud_fragment_oblateness1)
        
        #Cloud2
        xcloud2 = 0.4 * screen_width
        ycloud2 = 0.45 * sky_hight
        cloud_width2 = 0.25 * screen_width
        cloud_fragment_oblateness2 = 0.85
        draw_cloud(xcloud2, ycloud2, cloud_width2, cloud_fragment_oblateness2)
        
        #Cloud3
        xcloud3 = 0.1 * screen_width
        ycloud3 = 0.7 * sky_hight
        cloud_width3 = 0.2 * screen_width
        cloud_fragment_oblateness3 = 1.5
        draw_cloud(xcloud3, ycloud3, cloud_width3, cloud_fragment_oblateness3)
        
        #Ships:
        #Ship1
        xship1 = 0.5 * screen_width
        yship1 = sky_hight + 0.5 * sea_hight
        ship_hight1 = 0.3 * screen_hight
        ship_width1 = 0.4 * screen_width
        draw_ship(xship1, yship1, ship_width1, ship_hight1)
        
        #Ship2
        xship2 = 0.25 * screen_width
        yship2 = sky_hight + 0.2 * sea_hight
        ship_hight2 = 0.125 * screen_hight
        ship_width2 = 0.2 * screen_width
        draw_ship(xship2, yship2, ship_width2, ship_hight2)
        
        #Umbrellas:
        #Umbrella1
        xumbrella1 = 0.05 * screen_width
        yumbrella1 = sky_hight + sea_hight + 0.85 * beach_hight
        umbrella_hight1 = 0.4 * screen_hight
        umbrella_width1 = 0.2 * screen_width
        draw_umbrella(xumbrella1, yumbrella1, umbrella_width1,
                      umbrella_hight1)
        
        #Umbrella2
        xumbrella2 = 0.3 * screen_width
        yumbrella2 = sky_hight + sea_hight + 0.7 * beach_hight
        umbrella_hight2 = 0.25 * screen_hight
        umbrella_width2 = 0.1 * screen_width
        draw_umbrella(xumbrella2, yumbrella2, umbrella_width2,
                      umbrella_hight2)
        
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


def draw_waves(y, n, fi):
    """
    Draws waves between beach and sea.

    Parameters
    ----------
    y : TYPE float
        DESCRIPTION. y coordinate of the level of waves.
    n : TYPE float(int is preferable)
        DESCRIPTION. A number of waves.
    fi : TYPE float
        DESCRIPTION. An angular measure of one wave. The less it is, the 
        narrower the wave is.

    Returns
    -------
    None.

    """
    l = screen_width / n # A length of one wave.
    R = l / (2 * np.sin(fi/2 * np.pi/180))
    for i in range(int(n) + 1):
        if i % 2 == 0:
            circle(screen, YELLOW, 
                   [int(i * l + l/2), int(y + R * np.cos(fi/2 * np.pi/180))],
                   int(R))
        else:
            circle(screen, DARK_BLUE,
                   [int(i * l + l/2), int(y - R * np.cos(fi/2 * np.pi/180))],
                   int(R))
            
            
def draw_sun(x, y, inr, outr, n):
    """
    Draws sun on the sky.

    Parameters
    ----------
    x : TYPE float
        DESCRIPTION. x coordinate of sun's center.
    y : TYPE float
        DESCRIPTION. y coordinate of sun's center.
    inr : TYPE float
        DESCRIPTION. Radius of the sun on the internal border of rays.
    outr : TYPE float
        DESCRIPTION. Radius of the sun on the external border of rays.
    n : TYPE int
        DESCRIPTION. A number of rays.    

    Returns
    -------
    None.

    """
    pointlist = []    #List of vertices of rays.
    a = 2*np.pi / n   #An angular size of one ray.
    for i in range(n):
        pointlist.append((x + inr * np.cos(a * i), y - inr * np.sin(a * i)))
        pointlist.append((x + outr * np.cos(a * (i + 0.5)), y - outr * 
                          np.sin(a * (i + 0.5))))
    polygon(screen, YELLOW, pointlist)
        
        
def draw_cloud(x, y, w, oblateness):
    """
    Draws cloud on the sky. A fragment of the cloud is an ellipse. 'a' is a 
    half-axis of the ellipse along x coordinate axix. 'b' is a half-axis of
    the ellipse along y coordinate axix. 

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
        (along x coordinate axix). A hight equals 6/13 * w / oblateness.
    oblateness : TYPE float
        DESCRIPTION. oblateness = a / b. 

    Returns
    -------
    None.

    """
    a = 2/13 * w        #Read documentation to know what the 'a' and 'b' is.
    b = a / oblateness
    ellipse(screen, WHITE, [x + 3/4 * a, y - 3 * b, 2 * a, 2 * b])
    ellipse(screen, GRAY, [x + 3/4 * a, y - 3 * b, 2 * a, 2 * b], 1)
    ellipse(screen, WHITE, [x + 9/4 * a, y - 3 * b, 2 * a, 2 * b])
    ellipse(screen, GRAY, [x + 9/4 * a, y - 3 * b, 2 * a, 2 * b], 1)
    ellipse(screen, WHITE, [x, y - 2.3 * b, 2 * a, 2 * b])
    ellipse(screen, GRAY, [x, y - 2.3 * b, 2 * a, 2 * b], 1)
    ellipse(screen, WHITE, [x + 1.5 * a, y - 2 * b, 2 * a, 2 * b])
    ellipse(screen, GRAY, [x + 1.5 * a, y - 2 * b, 2 * a, 2 * b], 1)
    ellipse(screen, WHITE, [x + 3 * a, y - 2 * b, 2 * a, 2 * b])
    ellipse(screen, GRAY, [x + 3 * a, y - 2 * b, 2 * a, 2 * b], 1)
    ellipse(screen, WHITE, [x + 15/4 * a, y - 3 * b, 2 * a, 2 * b])
    ellipse(screen, GRAY, [x + 15/4 * a, y - 3 * b, 2 * a, 2 * b], 1)
    ellipse(screen, WHITE, [x + 4.5 * a, y - 2 * b, 2 * a, 2 * b])
    ellipse(screen, GRAY, [x + 4.5 * a, y - 2 * b, 2 * a, 2 * b], 1)


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
    draw_deck(x, y, w, 0.2*h)
    draw_sails(x + 0.35*w, y - 0.2*h, 0.25 * w, 0.8 * h)
    
    
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
    for i in range(5):
        line(screen, BLACK, (x + 0.475*w, y - h), (x + i/4 * 0.475*w,
                                                   y - 0.8*h))
    for i in range(5):
        line(screen, BLACK, (x + 0.525*w, y - h), (x + 0.525*w + i/4 *
                                                   0.475*w, y - 0.8*h))
    

main()
pygame.quit()
