
import pygame as pg
import numpy as np
import settings as s

object_num = 5
object_points = 5

obj_list = []
for n in range(object_num):
    shape = []
    
    x_mu = s.WIDTH * np.random.rand()
    y_mu = s.HEIGHT * np.random.rand()
    sigma = 20
    for m in range(object_points):
        shape.append((sigma * np.random.randn() + x_mu,sigma * np.random.randn() + y_mu))

    obj_list.append(shape)



def sort_points(cluster):

    for n in range(len(cluster) - 1):
        for m in range(n+1,len(cluster)):
            print("p1:",cluster[m]," p2:",cluster[n]," dist:",distance(cluster[m],cluster[n]))
            
    # return cluster

def distance(x1y1,x2y2):
    x1y1_li = list(x1y1)
    x2y2_li = list(x2y2)
    
    dist = np.sqrt((x1y1_li[0] -  x2y2_li[0])**2 + (x1y1_li[1] -  x2y2_li[1])**2)
    return dist    



pg.init()
window = pg.display.set_mode((s.WIDTH,s.HEIGHT))
pg.display.set_caption("raycast")
window.fill((0,0,0))
Fr_ps = 100

cluster_pts = []
for obj in obj_list:
    for pts in obj:
        # print(pts)
        cluster_pts.append(pts)
# print(cluster_pts)


sort_points(cluster_pts)
run = True
while run:
    
    
    for obj in obj_list:
        for pts in obj:
            pg.draw.circle(window,(255, 255, 255),pts,2,1)
    
    
        
    pg.display.update()
    window.fill((0,0,0))

    #EVENT HANDLING
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    

