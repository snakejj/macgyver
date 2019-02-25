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

obj1pick = False
obj2pick = False
obj3pick = False
win = False
los = False

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

        Error while loading PyGame

        """)

    else:
        print("""

        PyGame's loading : OK

        """)


def display_map(mac,obj):
        
    window = pygame.display.set_mode((300, 330)) #Size of 15 blocs of 20px each

    floors = pygame.image.load("ressources/floor.jpg").convert()  
    walls = pygame.image.load("ressources/wall.jpg").convert()  
    macg = pygame.image.load("ressources/mac.png").convert_alpha() 
    grdn = pygame.image.load("ressources/grd.png").convert_alpha() 
    obj1 = pygame.image.load("ressources/ether.png").convert_alpha()
    obj2 = pygame.image.load("ressources/syringe.png").convert_alpha()
    obj3 = pygame.image.load("ressources/tube.png").convert_alpha()
    wini = pygame.image.load("ressources/wini.png").convert_alpha()
    losi = pygame.image.load("ressources/losi.png").convert_alpha()
    topb = pygame.image.load("ressources/topbar.png").convert()


    # Loading map from the class Map
    carte = map.load_cart()
    

    
    
    for l in range(15):
        for e in range(15):
            window.blit(walls, (e*20,l*20+30))
            
            if map.maincart[l][e] == "@" or map.maincart[l][e] == "M" :
               
                window.blit(floors, (e*20,l*20+30))
             
            elif map.maincart[l][e] == "G":
               
                window.blit(floors, (e*20,l*20+30))
                window.blit(grdn, (e*20,l*20+30))
                
    
    window.blit(macg, (mac.mac_x,mac.mac_y+30))
    window.blit(topb, (0,0))

    if obj1pick == False :
        window.blit(obj1, (obj1_y*20,obj1_x*20+30))
    else:
        window.blit(obj1, (240,5))


    if obj2pick == False :
        window.blit(obj2, (obj2_y*20,obj2_x*20+30))
    else:
        window.blit(obj2, (260,5))
     
    if obj3pick == False :
        window.blit(obj3, (obj3_y*20,obj3_x*20+30))
    else:
        window.blit(obj3, (280,5))
    

    if win :
        window.blit(wini, (0,0))
    if los :
        window.blit(losi, (0,0))
        
        
        
def loop():

    #Infinite loop to let the window open
    continuer = 1

    while continuer:
        for event in pygame.event.get():  
            if event.type == QUIT:      
                continuer = 0       

    

    #loop to display the walls, floors, macgyver and the guardian
    #------------------------------------------------------------

            
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    mac.mac_down()
                    pick_obj(1,0)
                    winlose()
                    display_map(mac,obj)   
                if event.key == K_UP:
                    mac.mac_up()
                    pick_obj(-1,0)
                    winlose()
                    display_map(mac,obj)    
                if event.key == K_LEFT:
                    mac.mac_left()
                    pick_obj(0,-1)
                    winlose()
                    display_map(mac,obj) 
                if event.key == K_RIGHT:
                    mac.mac_right()
                    pick_obj(0,1)
                    winlose()
                    display_map(mac,obj) 


        pygame.display.flip()       #Display refresh



def pick_obj(plusorminusy,plusorminusx):

    if map.maincart[int(mac.mac_y /20-1+plusorminusy)]\
    [int(mac.mac_x / 20+plusorminusx)] == map.maincart\
    [int(obj1_y /20+plusorminusy)][int(obj1_x / 20+plusorminusx)] :
        
        obj.objcounter += 1
        obj1pick = True
    
    if map.maincart[int(mac.mac_y /20-1+plusorminusy)]\
    [int(mac.mac_x / 20+plusorminusx)] == map.maincart\
    [int(obj2_y /20+plusorminusy)][int(obj2_x / 20+plusorminusx)] :
        
        obj.objcounter += 1
        obj2pick = True

    if map.maincart[int(mac.mac_y /20-1+plusorminusy)]\
    [int(mac.mac_x / 20+plusorminusx)] == map.maincart\
    [int(obj3_y /20+plusorminusy)][int(obj3_x / 20+plusorminusx)] :
        
        obj.objcounter += 1
        obj3pick = True

def winlose():

    if mac.front_g == True and obj.objcounter == 3 :
        win = True
    elif mac.front_g == True and obj.objcounter < 3 :
        los = True



# ##############################################################################

initpygame()

display_map(mac,obj)

loop()    


