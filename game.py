# -*-coding:utf-8 -*


"""
Game docstring
"""


# ##############################################################################
# Importation of modules

import os
import pygame
from pygame.locals import *


from classes.mac import Mac
from classes.map import Map
from classes.obj import Obj

# ##############################################################################
# Definition of fonctions and start variables


map = Map()
map.load_cart()
mac = Mac(map.maincart)
obj = Obj(map.maincart)

obj1_x, obj1_y = obj.random_obj()
obj2_x, obj2_y = obj.random_obj()
while map.maincart[obj2_x][obj2_y] != map.maincart[obj1_x][obj1_y]:
    obj2_x, obj2_y = obj.random_obj()

obj3_x, obj3_y = obj.random_obj()
while map.maincart[obj3_x][obj3_y] != map.maincart[obj2_x][obj2_y]\
and map.maincart[obj3_x][obj3_y] != map.maincart[obj1_x][obj1_y] :
    obj2_x, obj2_y = obj.random_obj()

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


def display_map(mac,obj):
        
    fenetre = pygame.display.set_mode((300, 300)) #Taille pr 15 bloc de 20px

    sols = pygame.image.load("ressources/sol.jpg").convert() #Load background
    murs = pygame.image.load("ressources/mur.jpg").convert() #Load walls
    macg = pygame.image.load("ressources/mac.png").convert_alpha() 
    grdn = pygame.image.load("ressources/grd.png").convert_alpha() 
    obj1 = pygame.image.load("ressources/ether.png").convert_alpha()
    obj2 = pygame.image.load("ressources/coffre.png").convert_alpha()
    obj3 = pygame.image.load("ressources/potion.png").convert_alpha()



    # Chargement de la map depuis la classe Map
    carte = map.load_cart()
    

    
    
    for l in range(15):
        for e in range(15):
            fenetre.blit(murs, (e*20,l*20))
            
            if map.maincart[l][e] == "@" or map.maincart[l][e] == "M" :
               
                fenetre.blit(sols, (e*20,l*20))
             
            elif map.maincart[l][e] == "G":
               
                fenetre.blit(sols, (e*20,l*20))
                fenetre.blit(grdn, (e*20,l*20))
                
    
    fenetre.blit(macg, (mac.mac_x,mac.mac_y))

    
    fenetre.blit(obj1, (obj1_y*20,obj1_x*20))
    fenetre.blit(obj2, (obj2_y*20,obj2_x*20))
    fenetre.blit(obj3, (obj3_y*20,obj3_x*20))
    
def loop():

    #Boucle infinie pour laisser la fenetre ouverte
    continuer = 1

    while continuer:
        for event in pygame.event.get(): #On parcours la liste de tt les event reçus
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                continuer = 0      #On arrête la boucle

    

    #Boucle pour afficher les murs, sols, macgyver et le gardien
    #------------------------------------------------------------

            
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    mac.mac_down()
                    display_map(mac,obj)    
                if event.key == K_UP:
                    mac.mac_up()
                    display_map(mac,obj)   
                if event.key == K_LEFT:
                    mac.mac_left()
                    display_map(mac,obj)  
                if event.key == K_RIGHT:
                    mac.mac_right()
                    display_map(mac,obj)   


        pygame.display.flip()       #Rafraichissement de l'affichage



# ##############################################################################

initpygame()

display_map(mac,obj)


loop()    


