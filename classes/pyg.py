# -*-coding:utf-8 -*

import pygame
from pygame.locals import *
from classes.map import Map

class Pyg:
    """
    Docstring de la classe Pygame
    """


    @staticmethod
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

    @staticmethod
    def display_map():
        
        
               
        fenetre = pygame.display.set_mode((300, 300)) #Taille pr 15 bloc de 20px

        sol = pygame.image.load("ressources/sol.jpg").convert() #Load background
        mur = pygame.image.load("ressources/mur.jpg").convert() #Load walls
        mac = pygame.image.load("ressources/mac.png").convert_alpha() 
        grd = pygame.image.load("ressources/grd.png").convert_alpha() 
        
        Map.load_cart() # Chargement de la map depuis la classe Map
        carte = Map.load_cart()

        for l in range(15):
            for e in range(15):
                if carte[l][e] == "X":
                    fenetre.blit(mur, (e*20,l*20))
                elif carte[l][e] == "M":
                    fenetre.blit(sol, (e*20,l*20))
                    fenetre.blit(mac, (e*20,l*20))
                elif carte[l][e] == "G":
                    fenetre.blit(sol, (e*20,l*20))
                    fenetre.blit(grd, (e*20,l*20))
                else  :
                    fenetre.blit(sol, (e*20,l*20))


    @staticmethod
    def loop():
        #Boucle infinie pour laisser la fenetre ouverte
        continuer = 1

        while continuer:
            for event in pygame.event.get(): #On parcours la liste de tt les event reçus
                if event.type == QUIT:     #Si un de ces événements est de type QUIT
                    continuer = 0      #On arrête la boucle

        #mise en place des deplacements de sorte a pouvoir switcher entre terminal et 
        #pygame , c a d changer la map stocker en variable

        #Boucle pour afficher les murs, sols, macgyver et le gardien
        #------------------------------------------------------------

                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        pass
                    if event.key == K_UP:
                        pass
                    if event.key == K_LEFT:
                        pass
                    if event.key == K_RIGHT:
                        pass

            pygame.display.flip()       #Rafraichissement de l'affichage
