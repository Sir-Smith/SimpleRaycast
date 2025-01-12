import numpy as np
import pygame as pg
import settings as s
import character
import mapping

class path_plan:
    def __init__(self) -> None:
        pass

    def branch(self,point,branch_num):
        x_mu = s.WIDTH * np.random.rand()
        y_mu = s.HEIGHT * np.random.rand()
        sigma = 3
        for n in range(branch_num):
            sigma * np.random.randn() + x_mu,sigma * np.random.randn() + y_mu

