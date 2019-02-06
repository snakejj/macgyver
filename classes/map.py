# -*-coding:utf-8 -*

import pygame

from pygame.locals import *
from classes.mac import Mac

mac = Mac()

class Map:
    """
    Docstring de la classe Map
    """

    def __init__(self):
        pass
    

    def load_cart(self):
        with open("map.txt", "r") as fichier_carte :    #Ouverture du fichier map.txt dans var fichier_carte         
            carte = []
            for line in fichier_carte:  
                carte_l = []                
                for character in line:
                    if character != "\n":
                        carte_l.append(character)
                
                if carte_l:
                    carte.append(carte_l)     
        return carte


        

    
    def display_map(self):
        
        
               
        fenetre = pygame.display.set_mode((300, 300)) #Taille pr 15 bloc de 20px

        sol = pygame.image.load("ressources/sol.jpg").convert() #Load background
        mur = pygame.image.load("ressources/mur.jpg").convert() #Load walls
        mac = pygame.image.load("ressources/mac.png").convert_alpha() 
        grd = pygame.image.load("ressources/grd.png").convert_alpha() 
        
        # Chargement de la map depuis la classe Map
        self.load_cart() # Chargement de la map depuis la classe Map
        carte = self.load_cart()

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

    
    def loop(self):
        #Boucle infinie pour laisser la fenetre ouverte
        continuer = 1
        mac_y = 0
        mac_x = 0

        while continuer:
            for event in pygame.event.get(): #On parcours la liste de tt les event reçus
                if event.type == QUIT:     #Si un de ces événements est de type QUIT
                    continuer = 0      #On arrête la boucle

        

        #Boucle pour afficher les murs, sols, macgyver et le gardien
        #------------------------------------------------------------

               
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        if mac_y < 280 :
                            mac_y = mac.mac_down(mac_y, mac_x)
                        else:
                            self.display_map()                            
                    if event.key == K_UP:
                        pass
                    if event.key == K_LEFT:
                        pass
                    if event.key == K_RIGHT:
                        pass


            pygame.display.flip()       #Rafraichissement de l'affichage
