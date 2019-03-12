# -*-coding:utf-8 -*


"""
Game docstring
"""

# ##############################################################################
# Importation of modules


import pygame
from pygame.locals import *

from classes.mac import Mac
from classes.map import Map
from classes.obj import Obj


# ##############################################################################
# Definition of functions and start variables


def check_superposition():
    while obj_2.obj_x == obj_1.obj_x and obj_2.obj_y == obj_1.obj_y:
        obj_2.random_obj()

    while obj_3.obj_x == obj_2.obj_x and obj_3.obj_y == obj_2.obj_y \
            or obj_3.obj_x == obj_1.obj_x and obj_3.obj_y == obj_1.obj_y:
        obj_3.random_obj()


def init_pygame():
    check = pygame.init()
    if check[1] != 0:
        print("""

        Error while loading PyGame

        """)

    else:
        print("""

        PyGame's loading : OK

        """)


def display_obj():
    obj1 = pygame.image.load("resources/ether.png").convert_alpha()
    obj2 = pygame.image.load("resources/syringe.png").convert_alpha()
    obj3 = pygame.image.load("resources/tube.png").convert_alpha()

    if obj_1.objpick is False:
        window.blit(obj1, (obj_1.obj_y * 20, obj_1.obj_x * 20 + 30))
    else:
        window.blit(obj1, (240, 5))

    if obj_2.objpick is False:
        window.blit(obj2, (obj_2.obj_y * 20, obj_2.obj_x * 20 + 30))
    else:
        window.blit(obj2, (260, 5))

    if obj_3.objpick is False:
        window.blit(obj3, (obj_3.obj_y * 20, obj_3.obj_x * 20 + 30))
    else:
        window.blit(obj3, (280, 5))

def display_win_lose():
    wini = pygame.image.load("resources/wini.png").convert()
    losi = pygame.image.load("resources/losi.png").convert()
    if win:
        window.blit(wini, (0, 30))
    if los:
        window.blit(losi, (0, 30))


def display_map(macinstance):
    # Size of 15 blocs of 20px each
    global window

    window = pygame.display.set_mode((300, 330))
    floors = pygame.image.load("resources/floor.jpg").convert()
    walls = pygame.image.load("resources/wall.jpg").convert()
    macg = pygame.image.load("resources/mac.png").convert_alpha()
    grdn = pygame.image.load("resources/grd.png").convert_alpha()


    topb = pygame.image.load("resources/topbar.png").convert()

    # Loading map from the class Map
    

    for l in range(15):
        for e in range(15):
            window.blit(walls, (e * 20, l * 20 + 30))

            if mapy.mainmap[l][e] == "@" or mapy.mainmap[l][e] == "M":

                window.blit(floors, (e * 20, l * 20 + 30))

            elif mapy.mainmap[l][e] == "G":

                window.blit(floors, (e * 20, l * 20 + 30))
                window.blit(grdn, (e * 20, l * 20 + 30))

    window.blit(macg, (macinstance.mac_x * 20, macinstance.mac_y * 20 + 30))
    window.blit(topb, (0, 0))

    display_obj()
    display_win_lose()



def loop():
    global restart, endgame

    # Infinite loop to let the window open
    tocontinue = 1
    pygame.display.flip()
    
    while tocontinue:
        for event in pygame.event.get():
            if event.type == QUIT:
                tocontinue = 0
                endgame = True

            # loop to display the walls, floors, macgyver and the guardian
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    mac.mac_down()
                if event.key == K_UP:
                    mac.mac_up()
                if event.key == K_LEFT:
                    mac.mac_left()
                if event.key == K_RIGHT:
                    mac.mac_right()
                if event.key == K_SPACE:
                    restart = True
                    tocontinue = 0

                pick_obj()
                win_lose()
                display_map(mac)

        pygame.display.flip()  # Display refresh
    return restart, endgame


def pick_obj():
    global objcounter

    if mac.mac_x == obj_1.obj_y and mac.mac_y == obj_1.obj_x:
        objcounter += 1
        obj_1.objpick = True

    if mac.mac_x == obj_2.obj_y and mac.mac_y == obj_2.obj_x:
        objcounter += 1
        obj_2.objpick = True

    if mac.mac_x == obj_3.obj_y and mac.mac_y == obj_3.obj_x:
        objcounter += 1
        obj_3.objpick = True


def win_lose():
    global win, los

    if mac.front_g and objcounter >= 3:
        win = True
    elif mac.front_g and objcounter < 3:
        los = True

# ##############################################################################
# Definition of start variables

restart = False
endgame = False

# ##############################################################################
# ************************************GAME**************************************

init_pygame()

while restart is False and endgame is False:
    objcounter = 0
    win = False
    los = False    

    mapy = Map()
    mapy.load_cart()

    mac = Mac(mapy.mainmap)

    obj_1 = Obj(mapy.mainmap)
    obj_1.random_obj()
    obj_2 = Obj(mapy.mainmap)
    obj_2.random_obj()
    obj_3 = Obj(mapy.mainmap)
    obj_3.random_obj()
    check_superposition()

    display_map(mac)

    loop()
    restart = False

    continue
