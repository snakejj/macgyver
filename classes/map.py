# -*-coding:utf-8 -*

import pygame

from pygame.locals import *


class Map:
    """
    Map Class docstring
    """

    def __init__(self):
        self.maincart = []
    

    def load_cart(self):
        with open("map.txt", "r") as cart_file :    #Ouverture du fichier map.txt dans var cart_file         
            cart = []
            for line in cart_file:  
                cart_l = []                
                for character in line:
                    if character != "\n":
                        cart_l.append(character)
                
                if cart_l:
                    cart.append(cart_l)     
        self.maincart = cart


        

    
    
