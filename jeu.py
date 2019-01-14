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




################################################################################
# Definition des variables de depart

#La carte
#--------
                     
with open("map.txt", "r") as fichier_carte :    #Ouverture du fichier map.txt dans var fichier_carte
    carte = fichier_carte.read()                #Stockage de la map dans la variable carte

################################################################################
# Le jeu


initpygame()   #Appel de la fonction pygame to check if tt est OK

fenetre = pygame.display.set_mode((300, 300))   #Taille pour 15 bloc de 20px

fond = pygame.image.load("ressources/sol.jpg").convert()    #Load background

#Boucle pour afficher le fond (un peu brouillon peut etre)

i_x = 0
i_y = 0

while i_x < 300:
    fenetre.blit(fond, (i_x,0))
    i_x +=20
while i_y <300 :
    i_x = 0
    i_y +=20
    while i_x < 300:
        fenetre.blit(fond, (i_x,i_y))
        i_x +=20
    

    
    
    

pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
    continuer = int(input())




#Changement des "X" par une image

with open("ressources/sol.jpg", "r") as image_sol :
    sol = image_sol.read()

carte_ac_sol = carte.replace("X", sol)













#*******************************************************************************
# BROUILLON
"""

fichier_carte = open("map.txt","r")     #Ouverture du fichier map.txt
carte = fichier_carte.read()            #Capture du contenu dans la var *carte*
fichier_carte.close()                   #Fermeture du fichier map.txt
print(carte)                            #Affichage de la carte

"""


