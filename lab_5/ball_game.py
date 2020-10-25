import pygame
import numpy as np
from pygame.draw import *
from pygame.mouse import *
from random import *
pygame.init()
pygame.font.init()

FPS = 10
dT = 1 / FPS
screen_width = 1000
screen_hight = 800
screen_diagonal = np.sqrt(screen_width**2 + screen_hight**2)
screen = pygame.display.set_mode((screen_width, screen_hight))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SILVER = (109, 143, 146)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def main():
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    T = 0 #Global time[seconds]
    score = 0
    show_starting_screen()
    balls_list = []
    file = open("Best_scores.txt", "a")
    file = open("Best_scores.txt", "r")
    best_scores_list = file.readlines()
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ((event.button < 4) and (event.pos[0] > 0.5 * screen_width 
                                            - 2.5 * 0.1 * screen_hight)
                    and (event.pos[0] < 0.5 * screen_width + 2.5 * 0.1 
                         * screen_hight) and 
                    (event.pos[1] > 0.45 * screen_hight) and
                    (event.pos[1] < 0.55 * screen_hight)):
                    while not finished:
                        clock.tick(FPS)
                        screen.fill(BLACK)
                        if T >= 60:
                            finished = True
                        else:
                            T += dT
                            update_time(60 - T)
                            update_score(score)
                            update_best_scores(score, best_scores_list)
                            update_balls_list(balls_list, dt = dT)
                            if(int(10 * T) % 10 == 0):
                                add_ball_in_list(balls_list)
                            draw_balls(balls_list)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    finished = True
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pop_list = []  #The list of balls indexes
                                                   #to pop after clicking.
                                    for i in range(len(balls_list)):
                                        if((event.button < 4) and 
                                           ((event.pos[0] - 
                                             balls_list[i][1])**2 + 
                                            (event.pos[1] - 
                                             balls_list[i][2])**2 <=
                                            balls_list[i][3]**2)):
                                            pop_list.append(i)
                                            score += balls_list[i][4]
                                    update_score(score)
                                    update_best_scores(score, best_scores_list
                                                       )
                                    update_balls_list(balls_list, pop_list = 
                                                      pop_list)
    show_ending_screen(score)
    update_best_scores(score, best_scores_list)
    save_new_score(score, best_scores_list)
    file.close()
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    pygame.quit()


def show_starting_screen():
    """
    Offers you to click "START"; Shows brief rules. 

    Returns
    -------
    None.

    """
    rect(screen, WHITE, [0.5 * screen_width - 2.5 * 0.1 * screen_hight, 0.45 *
                         screen_hight, 5 * 0.1 * screen_hight,
                         0.1 * screen_hight])
    
    font = pygame.font.SysFont("TimesViewRoman", int(0.1 * screen_hight / 0.57
                                                     ))
    surface = font.render("START", False, GREEN)
    screen.blit(surface, (0.5 * screen_width - 2 * 0.1 * screen_hight,
                          0.45 * screen_hight))
    
    font = pygame.font.SysFont("TimesViewRoman", int(0.03 * screen_hight /
                                                     0.57))
    surface = font.render("You have 1 minute to click as many" , False, RED)
    surface1 = font.render("balls as possible. Red balls are", False, RED)
    surface2 = font.render("bad. Stars are good.", False, RED)
    screen.blit(surface, (0.5 * screen_width - 3 * 0.1 * screen_hight,
                          0.6 * screen_hight))
    screen.blit(surface1, (0.5 * screen_width - 2.5 * 0.1 * screen_hight,
                           0.65 * screen_hight))
    screen.blit(surface2, (0.5 * screen_width - 1.5 * 0.1 * screen_hight,
                           0.7 * screen_hight))
    
    pygame.display.update()
    
    
def show_ending_screen(score):
    """
    Shows ending screen.

    Parameters
    ----------
    score : TYPE float 
            DESCRIPTION. Your finishing score.

    Returns
    -------
    None.

    """
    rect(screen, WHITE, [0.5 * screen_width - 4 * 0.1 * screen_hight, 0.45 *
                         screen_hight, 8 * 0.1 * screen_hight,
                         0.1 * screen_hight])
    
    font = pygame.font.SysFont("TimesViewRoman", int(0.1 * screen_hight / 0.57
                                                     ))
    surface = font.render("GAME OVER", False, GREEN)
    screen.blit(surface, (0.5 * screen_width - 3.75 * 0.1 * screen_hight,
                          0.45 * screen_hight))
    font = pygame.font.SysFont("TimesViewRoman", int(0.05 * screen_hight
                                                     / 0.57))
    surface = font.render("YOUR SCORE: " + str(score), False, RED)
    screen.blit(surface, (0.5 * screen_width - 3.75 * 0.1 * screen_hight,
                          0.6 * screen_hight))
    pygame.display.update()


def update_time(t):
    """
    Shows left time.

    Parameters
    ----------
    t : TYPE float
        DESCRIPTION. The rest time you have.

    Returns
    -------
    None.

    """
    font = pygame.font.SysFont("TimesViewRoman", int(0.03 * screen_hight
                                                     / 0.57))
    if (t <= 5):
        surface = font.render("Time: " + str(t), False, RED)
    elif (t <= 20):
        surface = font.render("Time: " + str(t), False, YELLOW)
    else:
        surface = font.render("Time: " + str(t), False, GREEN)
    screen.blit(surface, (0, 0))
    pygame.display.update()


def update_score(score):
    """
    Shows your actual score.

    Parameters
    ----------
    score : TYPE float
        DESCRIPTION. Your actual score.

    Returns
    -------
    None.

    """
    font = pygame.font.SysFont("TimesViewRoman", int(0.03 * screen_hight 
                                                     / 0.57))
    surface = font.render("Score: " + str(score), False, BLUE)
    screen.blit(surface, (0, 0.05 * screen_hight))
    pygame.display.update()


def update_best_scores(score, best_scores_list):
    """
    Updates the list of best scores.

    Parameters
    ----------
    score : TYPE float
        DESCRIPTION. Your actual score.
    
    best_scores_list : TYPE a list of strings
        DESCRIPTION. The list of the best scores.
        
    Returns
    -------
    None.

    """
    l = best_scores_list.copy()
    l.append(str(score))
    l = list(map(int, l))
    l.sort(reverse=True)   
    font = pygame.font.SysFont("TimesViewRoman", int(0.03 * screen_hight 
                                                     / 0.57))
    surface = font.render("Best scores:", False, SILVER)
    screen.blit(surface, (screen_width - 8 * 0.03 * screen_hight, 0))
    for i in range(len(l)):
        if i < 3:
            if (i == 0) and (l[i] == score):
                surface = font.render(str(l[i]), False, GREEN)
                screen.blit(surface, (screen_width - 8 * 0.03 * screen_hight,
                                      (i + 1) * 0.05 * screen_hight))
            elif (i > 0) and (l[i] == score) and (l[i - 1] > score):
                surface = font.render(str(l[i]), False, GREEN)
                screen.blit(surface, (screen_width - 8 * 0.03 * screen_hight,
                                      (i + 1) * 0.05 * screen_hight))
            else:
                surface = font.render(str(l[i]), False, SILVER)
                screen.blit(surface, (screen_width - 8 * 0.03 * screen_hight,
                                      (i + 1) * 0.05 * screen_hight))
    pygame.display.update()
    

def save_new_score(score, best_scores_list):
    """
    Saves your score in the file if it's one of the best 10.

    Parameters
    ----------
    score : TYPE float
        DESCRIPTION. Your final score.
        
    best_scores_list : TYPE a list of strings
        DESCRIPTION. The list of the best scores.
        
    Returns
    -------
    None.

    """
    l = best_scores_list
    l.append(str(score))
    l = list(map(int, l))
    l.sort(reverse=True)
    file = open("Best_scores.txt", "w")
    for i in range(len(l)):
        if i < 10:
            print(str(l[i]), file=file)
    

def update_balls_list(balls_list, dt = 0, pop_list = []):
    """
    Update the list of balls. 

    Parameters
    ----------
    balls_list : TYPE the list of lists:[string, float, float, float, float,
        float, tuple:(int, int, int), float, float, float, float]
        DESCRIPTION. The balls_list consists of the list of balls that're
        alive. Each ball is a list:[type of a ball, x coordinate of ball's
        center, y coordinate of ball's center, radius, score a ball gives, the
        rest time of a ball's life, a color of a ball, x component of ball's
        velocity, y component of ball's velocity, x component of ball's 
        acceleration, y component of ball's acceleration]
    dt : TYPE float, optional
        DESCRIPTION. The default is 0. The time of program sleeping.
    pop_list : TYPE the list of int, optional
        DESCRIPTION. The default is []. The list of balls indexes to pop after
        clicking.

    Returns
    -------
    None.

    """
    for i in range(len(pop_list)):
        balls_list.pop(pop_list[len(pop_list) - i - 1])
    
    if (len(balls_list) > 0):
        for i in range(len(balls_list)):
            x = balls_list[len(balls_list) - i - 1][1]
            y = balls_list[len(balls_list) - i - 1][2] 
            r = balls_list[len(balls_list) - i - 1][3]
            dx = balls_list[len(balls_list) - i - 1][1] - get_pos()[0]
            dy = balls_list[len(balls_list) - i - 1][2] - get_pos()[1]
            k = 1 * 10**6 # Kulon coefficient
            
            balls_list[len(balls_list) - i - 1][5] -= dt
            if balls_list[len(balls_list) - i - 1][5] <= 0:
                balls_list.pop(len(balls_list) - i - 1)
            else:
                if balls_list[len(balls_list) - i - 1][0] == "STAR":
                    balls_list[len(balls_list) - i - 1][9] = k * dx / (
                        dx**2 + dy**2)**1.5
                    balls_list[len(balls_list) - i - 1][10] = k * dy / (
                        dx**2 + dy**2)**1.5
                ax = balls_list[len(balls_list) - i - 1][9]
                ay = balls_list[len(balls_list) - i - 1][10]
                balls_list[len(balls_list) - i - 1][7] += ax * dt
                balls_list[len(balls_list) - i - 1][8] += ay * dt
                
                vx = balls_list[len(balls_list) - i - 1][7]
                vy = balls_list[len(balls_list) - i - 1][8]
                if (x + vx * dt > screen_width - r):
                    balls_list[len(balls_list) - i - 1][1] = (
                        screen_width - r) * 2 - vx * dt - x
                    balls_list[len(balls_list) - i - 1][7] = -vx
                elif (x + vx * dt < r):
                    balls_list[len(balls_list) - i - 1][1] = -vx * dt - x 
                    + 2 * r
                    balls_list[len(balls_list) - i - 1][7] = -vx
                else:
                    balls_list[len(balls_list) - i - 1][1] = x + vx * dt
                
                if (y + vy * dt > screen_hight - r):
                    balls_list[len(balls_list) - i - 1][2] = (
                        screen_hight - r) * 2 - vy * dt - y
                    balls_list[len(balls_list) - i - 1][8] = -vy
                elif (y + vy * dt < r):
                    balls_list[len(balls_list) - i - 1][2] = -vy * dt - y
                    + 2 * r
                    balls_list[len(balls_list) - i - 1][8] = -vy
                else:
                    balls_list[len(balls_list) - i - 1][2] = y + vy * dt
            

def add_ball_in_list(balls_list):
    """
    Adds a new ball in the list of balls.

    Parameters
    ----------
    balls_list : TYPE the list of lists:[string, float, float, float, float,
        float, tuple:(int, int, int), float, float, float, float]
        DESCRIPTION. The balls_list consists of the list of balls that're
        alive. Each ball is a list:[type of a ball, x coordinate of ball's
        center, y coordinate of ball's center, radius, score a ball gives, the
        rest time of a ball's life, a color of a ball, x component of ball's
        velocity, y component of ball's velocity, x component of ball's 
        acceleration, y component of ball's acceleration]

    Returns
    -------
    None.

    """
    balls_types = ["STAT", "MOVE", "STAR"]
    ball_type = balls_types[randint(0, 2)]
    if ball_type == "STAR":
        r = int(0.02 * screen_diagonal)
    else:
        r = randint(int(0.05 * screen_diagonal), int(0.1 * screen_diagonal))
    x = randint(r, screen_width - r)
    y = randint(r, screen_hight - r)
    if ball_type == "STAR":
        color = SILVER
    else:
        color = COLORS[randint(0, 5)]
    if ball_type == "STAT":
        t = 1
    if ball_type == "MOVE":
        t = 3
    if ball_type == "STAR":
        t = 5
    if ball_type == "STAR":
        score = 500
    elif color == RED:
        score = - int(1000 * r / screen_diagonal)
    else:
        score = int(1000 * (0.15 - r / screen_diagonal))
    ax = 0
    ay = 0
    v = screen_diagonal / t * 4 * random()
    if ball_type != "MOVE":
        v = 0
    fi = 2 * np.pi * random()
    vx = v * np.cos(fi)
    vy = v * np.sin(fi)
    balls_list.append([ball_type, x, y, r, score, t, color, vx, vy, ax, ay])
        

def draw_balls(balls_list):
    """
    Draws all objects from balls_list.

    Parameters
    ----------
    balls_list : TYPE the list of lists:[string, float, float, float, float,
        float, tuple:(int, int, int), float, float, float, float]
        DESCRIPTION. The balls_list consists of the list of balls that're
        alive. Each ball is a list:[type of a ball, x coordinate of ball's
        center, y coordinate of ball's center, radius, score a ball gives, the
        rest time of a ball's life, a color of a ball, x component of ball's
        velocity, y component of ball's velocity, x component of ball's 
        acceleration, y component of ball's acceleration]

    Returns
    -------
    None.

    """
    for i in range(len(balls_list)):
        if balls_list[i][0] == "STAR":
            draw_star(balls_list[i][1], balls_list[i][2], balls_list[i][3])
        else:
            circle(screen, balls_list[i][6], (int(balls_list[i][1]), 
                                              int(balls_list[i][2])),
                   balls_list[i][3])
    pygame.display.update()


def draw_star(x, y, outr):
    """
    Draws a star.

    Parameters
    ----------
    x : TYPE float
        DESCRIPTION. x coordinate of star's center.
    y : TYPE float
        DESCRIPTION. y coordinate of star's center.
    outr : TYPE int
        DESCRIPTION. An outer radius of the star.

    Returns
    -------
    None.

    """
    inr = 0.5 * outr    #An inner radius of the star.
    n = 8    #A number of star's rays.
    fi = 2 * np.pi / n    #An angular size of one ray.
    l = []    #A list of star's vertexes.
    for i in range(n):
        l.append((x + outr * np.cos(i * fi), y + outr * np.sin(i * fi)))
        l.append((x + inr * np.cos((i + 0.5) * fi), y + inr * np.sin((i + 0.5)
                                                                     * fi)))
    polygon(screen, SILVER, l)
    
main()