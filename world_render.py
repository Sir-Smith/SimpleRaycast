import numpy as np
import pygame as pg
import settings
import character
import obstacles
import ray
import mapping

from timeit import default_timer as timer


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)






pg.init()

##      PRESETS  
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

##      WINDOW SETTINGS
window = pg.display.set_mode((settings.WIDTH,settings.HEIGHT))
pg.display.set_caption("raycast")
window.fill((0,0,0))
Fr_ps = 100





##INIT
#OBJECTS
char_state = character.State()
ray_list = ray.Rays()
mapping_data = mapping.data_points()

# INIT VARIABLES
m = 0
boundry_points = []
obst_num = 20
obst_points = 4
obstacles.populate_objects(obst_num,obst_points)

run = True
## GAME OPERATION

iter = 0
iter_acc = 0
while run:
    
    start = timer()

    # run = False
    for   obj in obstacles.obj_list:
        pg.draw.lines(window,WHITE,False,obj,1)

    rays = ray_list.update_rays(char_state.char_loc, char_state.char_ori)

    if m == 100:
        boundry_points = mapping_data.update_mapping_points(char_state.char_loc,rays)
        # print(boundry_points)
        boundry_points = mapping_data.gridify(5,boundry_points)
        # print(boundry_points)
        boundry_points = mapping_data.remove_repeated(boundry_points)
        m = 0
    else:
        m = m+1




    for ray_beams in rays:
        # print(ray_beams)
        pg.draw.line(window,WHITE,char_state.char_loc,ray_beams,1)
        
    pg.draw.circle(window,WHITE,char_state.char_loc,5,2)

    for data in boundry_points:
        pg.draw.circle(window,BLUE,data,2,1)




    pg.display.update()
    window.fill((0,0,0))
    
    key_input = pg.key.get_pressed()
    if key_input[pg.K_UP]:
        char_state.update_loc(1)

    if key_input[pg.K_DOWN]:
        char_state.update_loc(-1)

    if key_input[pg.K_RIGHT]:
        char_state.update_ori(1)
    
    if key_input[pg.K_LEFT]:
        char_state.update_ori(-1)

    
    #EVENT HANDLING
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_c:
            obstacles.obj_list = []
            mapping_data.point_cloud = []
            obstacles.populate_objects(obst_num,obst_points)
            
    
    end = timer()

    if iter == 20:
        iter_avg = iter_acc/iter
        iter = 0
        iter_acc = 0
        print(iter_avg) # Time in seconds
    else:
        one_iter = end - start
        iter_acc = iter_acc + one_iter
        iter = iter + 1

    


        # elif event.type == pg.MOUSEMOTION:
        #     mouse_pressed = pg.mouse.get_pressed()
        #     if mouse_pressed[0] == True:
        #         char_loc = pg.mouse.get_pos()

