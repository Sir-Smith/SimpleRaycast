
import numpy as np
import settings as s

# shape1 = [(176,139),
#           (352,117),
#           (470,200),
#           (538,289),
#           (532,395),
#           (422,469)
#           ]
# shape2 = [(546,687),
#           (522,602),
#           (575,543),
#           (687,573),
#           (683,656)
#           ]

import numpy as np
import settings as s

shape = []
obj_list = []

# object_points = 3
# object_num = 3

def populate_objects(object_num,object_points):

    for n in range(object_num):
        shape = []
        x_mu = s.WIDTH * np.random.rand()
        y_mu = s.HEIGHT * np.random.rand()
        sigma = 100
        for m in range(object_points):
            shape.append((sigma * np.random.randn() + x_mu,sigma * np.random.randn() + y_mu))
            # print("n:",n," m:",m," shape:",shape)

        obj_list.append(shape)
