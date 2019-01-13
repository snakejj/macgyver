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

def checkpygame():

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


checkpygame()

print(carte)













#*******************************************************************************
# BROUILLON
"""

fichier_carte = open("map.txt","r")     #Ouverture du fichier map.txt
carte = fichier_carte.read()            #Capture du contenu dans la var *carte*
fichier_carte.close()                   #Fermeture du fichier map.txt
print(carte)                            #Affichage de la carte

"""


