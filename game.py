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


def nonsup():
    while obj_2.obj_x == obj_1.obj_x and obj_2.obj_y == obj_1.obj_y:
        obj_2.random_obj()

    while obj_3.obj_x == obj_2.obj_x and obj_3.obj_y == obj_2.obj_y \
            or obj_3.obj_x == obj_1.obj_x and obj_3.obj_y == obj_1.obj_y:
        obj_3.random_obj()


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


def display_map(macinstance):
    window = pygame.display.set_mode((300, 330))  # Size of 15 blocs of 20px each

    floors = pygame.image.load("resources/floor.jpg").convert()
    walls = pygame.image.load("resources/wall.jpg").convert()
    macg = pygame.image.load("resources/mac.png").convert_alpha()
    grdn = pygame.image.load("resources/grd.png").convert_alpha()
    obj1 = pygame.image.load("resources/ether.png").convert_alpha()
    obj2 = pygame.image.load("resources/syringe.png").convert_alpha()
    obj3 = pygame.image.load("resources/tube.png").convert_alpha()
    wini = pygame.image.load("resources/wini.png").convert_alpha()
    losi = pygame.image.load("resources/losi.png").convert_alpha()
    topb = pygame.image.load("resources/topbar.png").convert()

    # Loading map from the class Map
    mapy.load_cart()

    for l in range(15):
        for e in range(15):
            window.blit(walls, (e * 20, l * 20 + 30))

            if mapy.maincart[l][e] == "@" or mapy.maincart[l][e] == "M":

                window.blit(floors, (e * 20, l * 20 + 30))

            elif mapy.maincart[l][e] == "G":

                window.blit(floors, (e * 20, l * 20 + 30))
                window.blit(grdn, (e * 20, l * 20 + 30))

    window.blit(macg, (macinstance.mac_x * 20, macinstance.mac_y * 20 + 30))
    window.blit(topb, (0, 0))

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

    if win:
        window.blit(wini, (0, 0))
    if los:
        window.blit(losi, (0, 0))


def loop():
    # Infinite loop to let the window open
    tocontinue = 1

    pygame.display.flip()
    global restart, endgame
    while tocontinue:
        for event in pygame.event.get():
            if event.type == QUIT:
                tocontinue = 0
                endgame = True

            # loop to display the walls, floors, macgyver and the guardian
            # ------------------------------------------------------------

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
                winlose()
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


def winlose():
    global win, los

    if mac.front_g and objcounter >= 3:
        win = True
    elif mac.front_g and objcounter < 3:
        los = True


# ##############################################################################


restart = False
endgame = False
initpygame()

while not restart and not endgame:
    mapy = Map()
    mapy.load_cart()

    mac = Mac(mapy.maincart)

    objcounter = 0

    obj_1 = Obj(mapy.maincart)
    obj_1.random_obj()

    obj_2 = Obj(mapy.maincart)
    obj_2.random_obj()

    obj_3 = Obj(mapy.maincart)
    obj_3.random_obj()

    win = False
    los = False

    nonsup()

    display_map(mac)

    loop()

    restart = False
    continue
