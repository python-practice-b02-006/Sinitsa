import pygame
import numpy as np
BLACK=(0,0,0)
BLUE=(0,0,255)
LSALMON=(255,160,122)
PEACH=(255, 218, 185)
LEMONE=(255, 250, 205)
SKYBLUE=(100, 149, 237)
TOMATO=(255, 99, 71)
CADET=(176, 196, 222)
SLATE=(106, 90, 205)
DARK=(72, 61, 109)                           
BROWN=(139, 69, 19)
WHITE=(255, 255, 255)
pygame.init()

def draw_bird(x,y,a,t,t_leaving):
    #X,Y-the size of the image, a-relative bird sizes, t - time
    surface = pygame.Surface([60 * a, 40 * a], pygame.SRCALPHA)
    pygame.draw.arc(surface, BROWN, (0, 0, 60*a, 40*a), 0, np.pi *5 / 8, 
                    int(max(5 - 5 / t_leaving * t, 1)))
    #pygame.draw.polygon(surface, BROWN, [(0, 0), (0, 40 * a),
    #                                     (60 * a, 40 * a,), (60 * a, 0)])
    T = 2  # A period of wings waving[s]
    fi = abs(45 * np.sin(2 * np.pi / T * t))
    surface_rot = pygame.transform.rotate(surface, -fi)
    screen.blit(surface_rot, [x - 20 * a * np.sin(fi * np.pi / 180) - 
                              60* a * np.cos(fi * np.pi / 180), y + 20 * a - 
                              60 * a * np.sin(fi * np.pi / 180) - 20 * a * 
                              np.cos(fi * np.pi / 180)])
    
    surface = pygame.Surface([60 * a, 40 * a], pygame.SRCALPHA)
    pygame.draw.arc(surface, BROWN, (0, 0, 60*a, 40*a), np.pi *3 / 8, 
                    1 * np.pi, int(max(5 - 5 / t_leaving * t, 1)))
    #pygame.draw.lines(screen,BROWN,False,[[x+23*a,y+3*a],
     #                                     [x+52*a,y+12*a],
      #                                    [x+78*a,y-a]],6)
    surface_rot = pygame.transform.rotate(surface, fi)
    screen.blit(surface_rot, [x - 20 * a * np.sin(fi * np.pi / 180),
                              y + 20 * a - 60 * a * np.sin(fi * np.pi / 180)
                              - 20 * a * np.cos(fi * np.pi / 180)])


x,y=640,480 #The size of the screen
#объект содерж экран
screen=pygame.display.set_mode([x,y])
pygame.display.set_caption('My first pygame app window caption')
done=False
#задержка
clock=pygame.time.Clock()

T = 0 #Global time[s]

while not done:
    clock.tick(10)
    T += 0.1
    for event in pygame.event.get():
        #все нажатия после гэт
        if event.type==pygame.QUIT:
            done=True

    #The colours of background
    screen.fill(LSALMON)
    pygame.draw.rect(screen,PEACH,(0, y/5, x, y/5))
    pygame.draw.rect(screen,LEMONE,(0, 2*y/5, x, y/5))
    pygame.draw.rect(screen,SKYBLUE,(0, 3*y/5, x, 2*y/5))

    #be like a sun, be happy!
    pygame.draw.circle(screen,TOMATO,[int(x/2),int(y/5)],40)
    
    
    #we can see mountains far away.
    pygame.draw.polygon(screen,CADET,[(640,144),(586,120),(510,160)])
    pygame.draw.polygon(screen,CADET,[(580,150),(510,110),(453,166)])
    pygame.draw.ellipse(screen,CADET,(503,107,30,30))
    pygame.draw.ellipse(screen,CADET,(525,124,30,30))
    pygame.draw.polygon(screen,CADET,[(527,111),(551,130),(510,160)])
    pygame.draw.polygon(screen,CADET,[(400,171),(480,86),(510,160)])
    pygame.draw.polygon(screen,CADET,[(400,171),(300,182),(346,153)])
    pygame.draw.polygon(screen,CADET,[(510,160),(330,176),(386,143)])
    pygame.draw.rect(screen,CADET,(386,130,60,20))
    pygame.draw.ellipse(screen,PEACH,(370,110,60,40))
    pygame.draw.ellipse(screen,CADET,(462,85,29,50))
    pygame.draw.polygon(screen,CADET,[(430,135),(465,94),(480,110)])
    pygame.draw.polygon(screen,PEACH,[(428,137),(465,94),(410,135)])
    pygame.draw.polygon(screen,CADET,[(133,92),(160,105),(160,160)])
    pygame.draw.polygon(screen,CADET,[(300,182),(100,205),(280,170)])
    pygame.draw.polygon(screen,CADET,[(300,182),(40,177),(0,217)])  
    pygame.draw.polygon(screen,CADET,[(250,188),(130,90),(64,210)]) 
    pygame.draw.rect(screen,CADET,(40,150,60,50))
    pygame.draw.ellipse(screen,PEACH,(20,130,70,50))
    pygame.draw.polygon(screen,PEACH,[(89,160),(70,155),(126,96)])
    
    
    #Mountains in the middle
    pygame.draw.ellipse(screen,SLATE,(5,190,90,208))
    pygame.draw.polygon(screen,SLATE,[(80,288),(250,288),(160,250)]) 
    pygame.draw.polygon(screen,SLATE,[(190,288),(300,288),(260,210)])
    pygame.draw.polygon(screen,SLATE,[(190,288),(210,200),(260,210)])
    pygame.draw.polygon(screen,SLATE,[(190,288),(440,288),(380,230)])
    pygame.draw.polygon(screen,SLATE,[(440,288),(570,205),(640,288)])
    pygame.draw.polygon(screen,SLATE,[(600,288),(640,288),(640,160)])
    pygame.draw.polygon(screen,SLATE,[(600,288),(615,210),(640,203)])
    pygame.draw.ellipse(screen,SLATE,(340,210,80,70))
    pygame.draw.ellipse(screen,SLATE,(354,210,70,40))
    pygame.draw.polygon(screen,SLATE,[(400,288),(640,288),(410,220)])
    pygame.draw.ellipse(screen,LEMONE,(433,215,80,40))
    pygame.draw.polygon(screen,LEMONE,[(433,238),(402,205),(450,220)])
    pygame.draw.polygon(screen,SLATE,[(317,268),(344,230),(370,280)])


    #mountains are in front of us.
    pygame.draw.polygon(screen,DARK,[(0,480),(0,250),(60,263)])
    pygame.draw.polygon(screen,DARK,[(0,480),(155,340),(60,263)])
    pygame.draw.polygon(screen,DARK,[(0,480),(155,340),(230,480)])
    pygame.draw.polygon(screen,DARK,[(270,480),(440,400),(500,480)])
    pygame.draw.rect(screen,DARK,(210,460,60,20))
    pygame.draw.ellipse(screen,SKYBLUE,(221,441,80,38))
    pygame.draw.polygon(screen,DARK,[(0,480),(155,340),(230,480)])
    pygame.draw.ellipse(screen,DARK,(540,280,200,400))
    pygame.draw.rect(screen,DARK,(470,400,80,108))
    pygame.draw.ellipse(screen,SKYBLUE,(221,441,80,38))
    pygame.draw.ellipse(screen,SKYBLUE,(459,347,89,110))
    
    
    #I HATE this STUff. Birds
    t_leaving = [3, 6, 9, 12, 15, 18, 21, 24]
    x_birds = [290*x/640, 320*x/640, 270*x/640, 260*x/640, 300*x/640,
               400*x/640, 350*x/640, 430*x/640]
    y_birds = [140*y/480, 160*y/480, 170*y/480, 220*y/480, 280*y/480,
               315*y/480, 330*y/480, 360*y/480]
    x0 = 0.5 * x    #Coordinates of finishing point of birds
    y0 = 0.22 * y   #
    birds=[
           (x_birds[4] + (x0 - x_birds[4]) / t_leaving[4] * T,
            y_birds[4] + (y0 - y_birds[4]) / t_leaving[4] * T,
            max(1 - 1 / t_leaving[4] * T, 0), T, t_leaving[4]), 
           (x_birds[7] + (x0 - x_birds[7]) / t_leaving[7] * T,
            y_birds[7] + (y0 - y_birds[7]) / t_leaving[7] * T,
            max(1 - 1 / t_leaving[7] * T, 0), T, t_leaving[7]),
           (x_birds[6] + (x0 - x_birds[6]) / t_leaving[6] * T,
            y_birds[6] + (y0 - y_birds[6]) / t_leaving[6] * T,
            max(0.7 - 0.7 / t_leaving[6] * T, 0), T, t_leaving[6]),
           (x_birds[5] + (x0 - x_birds[5]) / t_leaving[5] * T,
            y_birds[5] + (y0 - y_birds[5]) / t_leaving[5] * T,
            max(0.7 - 0.7 / t_leaving[5] * T, 0), T, t_leaving[5]),
           (x_birds[1] + (x0 - x_birds[1]) / t_leaving[1] * T,
            y_birds[1] + (y0 - y_birds[1]) / t_leaving[1] * T,
            max(0.5 - 0.5 / t_leaving[1] * T, 0), T, t_leaving[1]),
           (x_birds[0] + (x0 - x_birds[0]) / t_leaving[0] * T,
            y_birds[0] + (y0 - y_birds[0]) / t_leaving[0] * T,
            max(0.5 - 0.5 / t_leaving[0] * T, 0), T, t_leaving[0]),
           (x_birds[2] + (x0 - x_birds[2]) / t_leaving[2] * T,
            y_birds[2] + (y0 - y_birds[2]) / t_leaving[2] * T,
            max(0.5 - 0.5 / t_leaving[2] * T, 0), T, t_leaving[2]),
           (x_birds[3] + (x0 - x_birds[3]) / t_leaving[3] * T,
            y_birds[3] + (y0 - y_birds[3]) / t_leaving[3] * T,
            max(0.5 - 0.5 / t_leaving[3] * T, 0), T, t_leaving[3])]
    for i in range(len(birds)):
        if (birds[i][2] * 20 > 1):
            draw_bird(birds[i][0], birds[i][1], birds[i][2], birds[i][3], 
                      birds[i][4])  
    
    pygame.display.flip()
pygame.quit()


'''    #нарисуем линию 5-толщина
    pygame.draw.line(screen,BLUE,[100,50],[100,150],5)
    pygame.draw.line(screen,BLUE,[400,50],[400,150],5)
    pygame.draw.lines(screen,BLUE,False,[[270,150],[270,50],[320,50],[320,150]],5)
    pygame.draw.ellipse(screen,BLUE,[50,70,100,60],5)

    pygame.draw.ellipse(screen,BLUE,[350,70,100,60],5)
    pygame.draw.ellipse(screen,BLUE,[170,50,70,100],5)
'''
