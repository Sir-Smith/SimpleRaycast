import numpy as np
import pygame as pg
import obstacles


## RAY FORMING
class Rays:
    
    start_ang =  -170
    finis_ang =  170
    num_ang = 20
    ray_max = 300

    inc_ang = np.abs((finis_ang - start_ang) / (num_ang - 1))

    def __init__(self) -> None:
        pass
    

    def intersect(self,loc,ray_line,wall_line):
    
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

    def ray(self,loc, ang):
        char_xy = list(loc)
        x =  self.ray_max * np.cos(np.radians(ang)) + char_xy[0]  
        y =  self.ray_max * np.sin(np.radians(ang)) + char_xy[1] 
        # print((x,y))

        for obj in obstacles.obj_list:
            for n in range((len(obj)-1)):
                # print("loc:",char_xy," ray:",(x,y)," inter:",intersect(char_xy,(x,y),[obj[n],obj[n+1]]))
                inter = self.intersect(char_xy,(x,y),[obj[n],obj[n+1]])

                dist_int = np.sqrt((char_xy[0] - inter[0])** 2 + (char_xy[1] - inter[1])**2)
                if dist_int < self.ray_max:
                    x = inter[0]
                    y = inter[1]

        return (x,y)


    def update_rays(self,loc, ori):
        rays = []
        for n in range(self.num_ang):
            ang = self.start_ang + ori + self.inc_ang * n
            ray_item = self.ray(loc,ang)
            rays.append(ray_item)
        
        return rays 