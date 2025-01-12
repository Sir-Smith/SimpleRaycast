import numpy as np
import settings
import pygame as pg

class State:
    def __init__(self):
        self.char_loc = (20,700)
        self.char_ori = 0
        self.vel = 0.7
        self.rot = 0.7
        
    def update_loc(self, direction):
        x1 = list(self.char_loc)
        
        x1[0] = x1[0] + direction * self.vel*np.cos(np.deg2rad(self.char_ori))
        x1[1] = x1[1] + direction * self.vel*np.sin(np.deg2rad(self.char_ori))
        self.char_loc = tuple(x1)
    
    
    def update_ori(self, rotation):
        self.char_ori = self.char_ori + rotation * self.rot
        


