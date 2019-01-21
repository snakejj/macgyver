# -*-coding:utf-8 -*
################################################################################
#   PSEUDO CODE
#-------------------------------------------------------------------------------
#
#
################################################################################

"""
Docstring du jeu
"""

################################################################################
# Importation des modules necessaire

import os
import pygame
from pygame.locals import *

from random import randrange

################################################################################
# Definition des fonctions

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

def allmap():
    for l in range(15):
        for e in range(15):
            if carte[l][e] == "X":
                fenetre.blit(mur, (e*20,l*20))
            elif carte[l][e] == "M":
                fenetre.blit(mac, (e*20,l*20))
            elif carte[l][e] == "G":
                fenetre.blit(grd, (e*20,l*20))
            else  :
                fenetre.blit(sol, (e*20,l*20))


################################################################################
# Definition des variables de depart

#La carte
#--------
                     
with open("map.txt", "r") as fichier_carte :    #Ouverture du fichier map.txt dans var fichier_carte
    carte = []
    for line in fichier_carte:  
        carte_l = []
        for character in line:
            if character != "\n":
                carte_l.append(character)
        
        if carte_l:
            carte.append(carte_l)       












################################################################################
# Le jeu


initpygame()   #Appel de la fonction pygame to check if tt est OK

fenetre = pygame.display.set_mode((300, 300))   #Taille pour 15 bloc de 20px

sol = pygame.image.load("ressources/sol.jpg").convert()    #Load background
mur = pygame.image.load("ressources/mur.jpg").convert()
mac = pygame.image.load("ressources/mac.png").convert()
grd = pygame.image.load("ressources/grd.png").convert()

#Boucle pour afficher les murs, sols, macgyver et le gardien
#------------------------------------------------------------



allmap()



#Boucle infinie pour laisser la fenetre ouverte
continuer = 1

while continuer:
    for event in pygame.event.get(): #On parcours la liste de tt les event reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0      #On arrête la boucle

#mise en place des deplacements de sorte a pouvoir switcher entre terminal et 
#pygame , c a d changer la map stocker en variable


        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                idx = sum(carte,[]).index("M")
                idx = idx/3,idx%3
                print(idx)
                allmap()
            if event.key == K_UP:
                for l in range(15):
                    for e in range(15):        
                        if carte[l][e] == "M":
                            carte[l][e] = "@"
                            carte[l+1][e] = "M"
                            allmap()
            if event.key == K_LEFT:
                for l in range(15):
                    for e in range(15):        
                        if carte[l][e] == "M":
                            carte[l][e] = "@"
                            carte[l][e-1] = "M"
                            allmap()
            if event.key == K_RIGHT:
                for l in range(15):
                    for e in range(15):        
                        if carte[l][e] == "M":
                            carte[l][e] = "@"
                            carte[l][e+1] = "M"
                            allmap()


    pygame.display.flip()       #Rafraichissement de l'affichage





        

"""
#####################
#####################
#####################


while i_x < 300:
    fenetre.blit(fond, (i_x,0))
    i_x +=20
while i_y <300 :
    i_x = 0
    i_y +=20
    while i_x < 300:
        fenetre.blit(fond, (i_x,i_y))
        i_x +=20
    



#Afficher MacGyver

macgyver = pygame.image.load("ressources/MacGyver.png").convert_alpha()

m_x = 60
m_y = 60
fenetre.blit(macgyver,(m_x,m_y))
    
    
#mise en place des deplacements (CA BLOQUE JE NE SAIS PAS POURQUOI !!!!!!!!!!!!)

if event.type == KEYDOWN:
    if event.key == K_DOWN:
        m_y+=20
        fenetre.blit(macgyver,(m_x,m_y))
    if event.key == K_UP:
        fenetre.blit(macgyver,(m_x,m_y))
        m_x+=20

pygame.display.flip()       #Rafraichissement de l'affichage


#Boucle infinie pour laisser la fenetre ouverte
continuer = 1

while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle





#Changement des "X" par une image

with open("ressources/sol.jpg", "r") as image_sol :
    sol = image_sol.read()

carte_ac_sol = carte.replace("X", sol)













#*******************************************************************************
# BROUILLON

fichier_carte = open("map.txt","r")     #Ouverture du fichier map.txt
carte = fichier_carte.read()            #Capture du contenu dans la var *carte*
fichier_carte.close()                   #Fermeture du fichier map.txt
print(carte)                            #Affichage de la carte


"""
'''
l = 0
e = 0


while l < 15 : 
    
    while e < 15 :
        if carte[l][e] == "X":
            fenetre.blit(mur, (e*20,l*20))
        else :
            fenetre.blit(sol, (e*20,l*20))
        
        e += 1
    l +=1
    e = 0
'''

