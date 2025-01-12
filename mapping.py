import numpy as np
import character
import ray

char_state = character.State()
ray_state = ray.Rays()

class data_points:
    def __init__(self):
        self.point_cloud = []
        pass

    def data_collect(self,char_loc,data):
        
        points = []
        char_xy = list(char_loc)

        for ray_beam in data:
            # print(ray_beam)
            ray_xy = list(ray_beam)
            dist_point = np.sqrt((char_xy[0] - ray_xy[0])** 2 + (char_xy[1] - ray_xy[1])**2)
            if dist_point < ray_state.ray_max-0.01:
                points.append((ray_xy[0],ray_xy[1]))
            
        return points
    
    def update_mapping_points(self,char_loc,data):
        
        new_data = self.data_collect(char_loc,data)
        # print(new_data)
        for nd in new_data:
            if not(nd == None):
                self.point_cloud.append(nd)
                # print(self.point_cloud)
        return self.point_cloud
    
    def gridify(self,grid_unit,point_cloud):
        xy_grid_points = [(0,0)]
        factor = 1/grid_unit
        for xy in point_cloud:
            xy_list = list(xy)
            xy_list[0] = (np.floor(xy_list[0] * factor ))/factor
            xy_list[1] = (np.floor(xy_list[1] * factor ))/factor

            xy_grid_points.append((xy_list[0],xy_list[1]))
            
        return xy_grid_points
    

    def remove_repeated(self,xy_grid_points):
        new_list = [(0,0)]

        for n in range(len(new_list)):
            for m in range(len(xy_grid_points)):
                
                point1 = list(xy_grid_points[m])
                point2 = list(new_list[n])
                if point1[0] == point2[0]:
                    if point1[1] == point2[1]:
                        pass
                    else:
                        new_list.append((point1[0],point1[1]))
                else:
                    new_list.append((point1[0],point1[1]))
        del new_list[0]
        return new_list

    def group_points(self,point_cloud):

        return self.point_cloud
    
if __name__ == "__main__":
    points = []
    data_p = data_points()
    for n in range(2000):
        points.append((10 * np.random.random(),10 * np.random.random()))
    # print(points)
    # points = [(0.0, 0.0), (8.0, 5.0), (2.0, 0.0), (2.0, 3.0), (1.0, 3.0), (7.0, 0.0), (9.0, 5.0), (1.0, 4.0), (4.0, 5.0), (6.0, 0.0), (4.0, 6.0), (8.0, 5.0), (6.0, 0.0), (2.0, 6.0), (6.0, 3.0), (8.0, 1.0), (4.0, 7.0), (8.0, 5.0), (0.0, 8.0), (0.0, 8.0), (0.0, 5.0)]
    grid_dp = data_p.gridify(2,points)
    # print(grid_dp)
    print(len(grid_dp))
    # data_points.remove_repeated()
    new_dp = data_p.remove_repeated(grid_dp)
    # print(new_dp)
    print(len(new_dp))