# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
from Partie import *
from ursina import *


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
"""
    Qui : Noa Haye
    Quand : 05/03/2024
    Quoi : Visiter la prison (Ne Fait Rien)
"""
class Visite_Prison(Case):
    """
    Qui : Noa Haye
    Quand : 05/03/2024
    Quoi : Création de constructeur et Accesseur
    """

    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    
    def __init__(self, position, nom, coordonnee):
        super().__init__(position, nom, coordonnee)


    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#
                 
    @property
    def type(self):
        return self.__type

    # ============================================================================#
    # = METHODE                                                               =#
    # ============================================================================#
    """
    Qui : Noa Haye
    Quand : 05/03/2024
    Quoi : Permet de visiter la prison
    """
    def visite(self, joueur, joueurs):
        print(f"{joueur.nom} est en visite à la prison.")
        for joueur in joueurs:
            if joueur.mouvement:
                # si nimporte quelle joueur est emprisonnée, il sera libéré.
                joueur.mouvement = False
                print(f"Vous avez libéré {joueur.nom} de prison.")