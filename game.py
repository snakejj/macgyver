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
# Definition of fonctions and start variables

def initpygame():

        check = pygame.init()
        if check[1] != 0:
            print("""

            Erreur lors du chargement de PyGame

            """)

        else:
            print("""

            Chargement de PyGame : OK

            """)


map = Map()

# ##############################################################################

# Pygame initiation
# --------

initpygame()


# La carte
# --------
              
map.load_cart() # Chargement de la map depuis la classe Map


# ##############################################################################
# Le jeu


  # Appel de la fonction pygame to check if tt est OK
map.display_map()
map.loop()    
