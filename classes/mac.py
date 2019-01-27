# -*-coding:utf-8 -*

from classes.map import Map

class Mac:
    """
    Docstring de la classe
    """

    pos_x = 0
    pos_y = 0


    def __init__(self):
        pass

    @staticmethod
    def move():
        Map.load_cart() # Chargement de la map depuis la classe Map
        carte = Map.load_cart()
        
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                pass
            if event.key == K_UP:
                pass
            if event.key == K_LEFT:
                pass
            if event.key == K_RIGHT:
                pass
        
