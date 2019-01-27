# -*-coding:utf-8 -*


"""
Game docstring
"""


# ##############################################################################
# Importation of modules

import os
import pygame
from pygame.locals import *

from random import randrange
from classes.mac import Mac
from classes.map import Map

# ##############################################################################
# Definition des fonctions
  

# ##############################################################################
# Definition des variables de depart

#La carte
#--------
                        
Map.load_cart() # Chargement de la map depuis la classe Map


# ##############################################################################
# Le jeu


Map.initpygame()   # Appel de la fonction pygame to check if tt est OK
Map.load_cart() 
Map.display_map()
Map.loop()    # Boucle which is une methode de la classe Pyg









        


