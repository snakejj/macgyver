# -*-coding:utf-8 -*

import pygame

from pygame.locals import *


class Map:
    """
    Docstring de la classe Map
    """

    def __init__(self):
        self.maincart = []
    

    def load_cart(self):
        with open("map.txt", "r") as fichier_carte :    #Ouverture du fichier map.txt dans var fichier_carte         
            carte = []
            for line in fichier_carte:  
                carte_l = []                
                for character in line:
                    if character != "\n":
                        carte_l.append(character)
                
                if carte_l:
                    carte.append(carte_l)     
        self.maincart = carte


        

    
    
