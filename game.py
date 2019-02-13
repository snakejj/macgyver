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

mac = Mac()
map = Map()

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


def display_map(mac_x,mac_y):
        
    fenetre = pygame.display.set_mode((300, 300)) #Taille pr 15 bloc de 20px

    sols = pygame.image.load("ressources/sol.jpg").convert() #Load background
    murs = pygame.image.load("ressources/mur.jpg").convert() #Load walls
    macg = pygame.image.load("ressources/mac.png").convert_alpha() 
    grdn = pygame.image.load("ressources/grd.png").convert_alpha() 
    
    # Chargement de la map depuis la classe Map
    map.load_cart() # Chargement de la map depuis la classe Map
    carte = map.load_cart()

    
    
    for l in range(15):
        for e in range(15):
            fenetre.blit(murs, (e*20,l*20))
            
            if map.maincart[l][e] == "@" or map.maincart[l][e] == "M" :
                mac.obstacle = True
                fenetre.blit(sols, (e*20,l*20))
            elif map.maincart[l][e] == "G":
                mac.obstacle = True
                fenetre.blit(sols, (e*20,l*20))
                fenetre.blit(grdn, (e*20,l*20))
                
    
    fenetre.blit(macg, (mac_x,mac_y))
    
def loop():

    #Boucle infinie pour laisser la fenetre ouverte
    continuer = 1
    mac_x = mac.mac_x
    mac_y = mac.mac_y

    while continuer:
        for event in pygame.event.get(): #On parcours la liste de tt les event reçus
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                continuer = 0      #On arrête la boucle

    

    #Boucle pour afficher les murs, sols, macgyver et le gardien
    #------------------------------------------------------------

           
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    mac_x, mac_y = mac.mac_down()
                    display_map(mac_x,mac_y)    
                if event.key == K_UP:
                    mac_x, mac_y = mac.mac_up()
                    display_map(mac_x,mac_y)    
                if event.key == K_LEFT:
                    mac_x, mac_y = mac.mac_left()
                    display_map(mac_x,mac_y)    
                if event.key == K_RIGHT:
                    mac_x, mac_y = mac.mac_right()
                    display_map(mac_x,mac_y)    


        pygame.display.flip()       #Rafraichissement de l'affichage



# ##############################################################################

initpygame()

display_map(mac.mac_x,mac.mac_y)

loop()    


