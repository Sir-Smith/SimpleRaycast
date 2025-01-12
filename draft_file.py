import numpy as np
import pygame as pg
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

shape1 = [(176,139),
          (352,117),
          (470,200),
          (538,289),
          (532,395),
          (422,469)
          ]
shape2 = [(546,687),
          (522,602),
          (575,543),
          (687,573),
          (683,656)
          ]


obj_list = (shape1,shape2)


pg.init()

##      PRESETS  
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)




##      WINDOW SETTINGS
WIDTH = 900
HEIGHT = 750
window = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("raycast")
window.fill((0,0,0))
Fr_ps = 100


##  CHARACTER
char_loc = (np.floor(900/2) ,np.floor(750/2))
char_ori = 0
vel = 0.1


## RAY FORMING
start_ang =  -40
finis_ang =  40
num_ang = 10
ray_max = 100

inc_ang = np.abs((finis_ang - start_ang) / (num_ang - 1))


def intersect(loc,ray_line,wall_line):
   
   locxy_list = list(loc)
   rayxy_list = list(ray_line)
   wall_p1 = wall_line[0]
   wall_p2 = wall_line[1]

   wall1xy = list(wall_p1)
   wall2xy = list(wall_p2)

   x1 = locxy_list[0]
   y1 = locxy_list[1]
   x2 = rayxy_list[0]
   y2 = rayxy_list[1]
   x3 = wall1xy[0]
   y3 = wall1xy[1]
   x4 = wall2xy[0]
   y4 = wall2xy[1]

   z1 = ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
   z2 = ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))

#    print("z1:",z1,"  z2:",z2)

   if ((z1 != 0) and (z2 != 0)):
      t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4)) /((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
      u = ((x1 - x3)*(y1 - y2) - (y1 - y3)*(x1 - x2)) /((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
      
    #   if ((t > 0) and (t < 1)):
    #      xt = x1 + t*(x2-x1)
    #      yt = y1 + t*(y2-y1)
    #      return [xt,yt]
      if ((u > 0) and (u < 1)):
         xu = x3 + u*(x4-x3)
         yu = y3 + u*(y4-y3)
         
        #  print("t:",t,"  u:",u)

         if ((t > 0) and (t < 1)):
            return [xu,yu]
         else:
          return [rayxy_list[0],rayxy_list[1]]
          
         

      else:
         return [rayxy_list[0],rayxy_list[1]]
   else:
      return [rayxy_list[0],rayxy_list[1]]

def ray(loc, ang):
    char_xy = list(loc)
    x = ray_max * np.cos(np.radians(ang)) + char_xy[0]  
    y = ray_max * np.sin(np.radians(ang)) + char_xy[1] 
    # print((x,y))



    for obj in obj_list:
        for n in range((len(obj)-1)):
            # print("loc:",char_xy," ray:",(x,y)," inter:",intersect(char_xy,(x,y),[obj[n],obj[n+1]]))
            inter = intersect(char_xy,(x,y),[obj[n],obj[n+1]])

            dist_int = np.sqrt((char_xy[0] - inter[0])** 2 + (char_xy[1] - inter[1])**2)
            if dist_int < ray_max:
                x = inter[0]
                y = inter[1]



    return (x,y)


def update_rays(loc, ori):
    rays = []
    for n in range(num_ang):
        rays.append(ray(loc, start_ang + ori + inc_ang * n))
    return rays 


## GAME OPERATION

run = True
while run:
    # run = False
    for   obj in obj_list:
        pg.draw.lines(window,WHITE,False,obj,1)
        
    rays = update_rays(char_loc, char_ori)

    for ray_beams in rays:
        pg.draw.line(window,WHITE,char_loc,ray_beams,1)
        
    pg.draw.circle(window,WHITE,char_loc,5,2)

    pg.display.update()
    window.fill((0,0,0))
    
    key_input = pg.key.get_pressed()
    if key_input[pg.K_UP]:
        x1 = list(char_loc)
        x1[0] = x1[0] + vel*np.cos(np.deg2rad(char_ori))
        x1[1] = x1[1] + vel*np.sin(np.deg2rad(char_ori))
        char_loc = tuple(x1)

    if key_input[pg.K_DOWN]:
        x1 = list(char_loc)
        x1[0] = x1[0] - vel*np.cos(np.deg2rad(char_ori))
        x1[1] = x1[1] - vel*np.sin(np.deg2rad(char_ori))
        char_loc = tuple(x1)

    if key_input[pg.K_LEFT]:
        char_ori = char_ori - 0.1

    if key_input[pg.K_RIGHT]:
        char_ori = char_ori + 0.1

    
    #EVENT HANDLING
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            run = False


        # elif event.type == pg.MOUSEMOTION:
        #     mouse_pressed = pg.mouse.get_pressed()
        #     if mouse_pressed[0] == True:
        #         char_loc = pg.mouse.get_pos()



        # elif event.type == pg.KEYDOWN:
        #     if event.key == pg.K_RIGHT:
        #         char_ori = char_ori - 15
        #     elif event.key == pg.K_LEFT:
        #         char_ori = char_ori + 15
        #     elif event.key == pg.K_RIGHT:
        #         x1 = list(char_loc)
        #         x1[0] = x1[0] + 1
        #         char_loc = tuple(x1)
        #     elif event.key == pg.K_LEFT:
        #         x2 = list(char_loc)
        #         x2[0] = x2[0] - 1
        #         char_loc = tuple(x2)


        
pg.quit()
