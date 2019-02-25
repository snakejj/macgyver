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

obj1 = Obj(map.maincart)
obj2 = Obj(map.maincart)
obj3 = Obj(map.maincart)


obj1.random_obj()
obj2.random_obj()
obj3.random_obj()


win = False
los = False

"""
obj1_x, obj1_y = obj.random_obj()
obj2_x, obj2_y = obj.random_obj()
while map.maincart[obj2_x][obj2_y] != map.maincart[obj1_x][obj1_y]:
    obj2_x, obj2_y = obj.random_obj()

obj3_x, obj3_y = obj.random_obj()
while map.maincart[obj3_x][obj3_y] != map.maincart[obj2_x][obj2_y]\
and map.maincart[obj3_x][obj3_y] != map.maincart[obj1_x][obj1_y] :
    obj2_x, obj2_y = obj.random_obj()
"""
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

    if obj1.objpick == False :
        window.blit(obj1, (obj1.obj_y*20,obj1.obj_x*20+30))
    else:
        window.blit(obj1, (240,5))


    if obj2.objpick == False :
        window.blit(obj2, (obj2.obj_y*20,obj2.obj_x*20+30))
    else:
        window.blit(obj2, (260,5))
     
    if obj3.objpick == False :
        window.blit(obj3, (obj3.obj_y*20,obj3.obj_x*20+30))
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
                    print(obj1pick,obj2pick,obj2pick)
                if event.key == K_UP:
                    mac.mac_up()  
                    print(obj1pick,obj2pick,obj2pick)
                if event.key == K_LEFT:
                    mac.mac_left()
                    print(obj1pick,obj2pick,obj2pick)
                if event.key == K_RIGHT:
                    mac.mac_right() 
                    print(obj1pick,obj2pick,obj2pick)
        pick_obj()
        display_map(mac,obj)  
        
        pygame.display.flip()       #Display refresh



def pick_obj():

    global obj1, obj2, obj3

    if map.maincart[int(mac.mac_y /20)]\
    [int(mac.mac_x / 20)] == map.maincart\
    [int(obj1_y /20)][int(obj1_x / 20)] :
        
        obj.objcounter += 1
        obj1.objpick = True
        print(map.maincart[int(mac.mac_y /20)]\
        [int(mac.mac_x / 20)])
        print(map.maincart\
        [int(obj1_y /20)][int(obj1_x / 20)])
        
    
    if map.maincart[int(mac.mac_y /20)]\
    [int(mac.mac_x / 20)] == map.maincart\
    [int(obj2_y /20)][int(obj2_x / 20)] :
        
        obj.objcounter += 1
        obj2.objpick = True


    if map.maincart[int(mac.mac_y /20)]\
    [int(mac.mac_x / 20)] == map.maincart\
    [int(obj3_y /20)][int(obj3_x / 20)] :
        
        obj.objcounter += 1
        obj3.objpick = True

        
def winlose():

    if mac.front_g == True and obj.objcounter == 3 :
        win = True
    elif mac.front_g == True and obj.objcounter < 3 :
        los = True



# ##############################################################################

initpygame()

display_map(mac,obj)

loop()    


