# -*-coding:utf-8 -*

import pygame

from pygame.locals import *
from classes.map import Map

map = Map()

class Mac:
    """
    Docstring de la classe
    """

    
    

    def __init__(self):
        self.mac_x = int() 
        self.mac_y = int()
        self.obstacle = []

    def mac_down(self):
        
        if self.mac_y < 280:
            self.mac_y += 20
            self.mac_x += 0
            print("mac_y =",self.mac_y)
            return self.mac_x, self.mac_y
        else:
            pass

    def mac_up(self):

        if self.mac_y > 0:
            self.mac_y -= 20
            self.mac_x += 0
            print("mac_y =", self.mac_y)
            return self.mac_x, self.mac_y
        else:
            pass

    def mac_right(self):
        
        if self.mac_x < 280:
            self.mac_x += 20
            self.mac_y -= 0
            print("mac_x =",self.mac_x)
            return self.mac_x, self.mac_y
        
        else:
            pass


    def mac_left(self):

        if self.mac_x > 0:
            self.mac_x -= 20
            self.mac_y -= 0
            print("mac_x =",self.mac_x)
            return self.mac_x, self.mac_y
        else:
            pass


