# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
from Partie import *


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
class Visite_Prison(Case):
    """
    Qui : Noa Haye
    Quand : 05/03/2024
    Quoi : Création de la classe, def__init__ et def visite
    """

    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    
    def __init__(self, nom, coordonnee):
        super().__init__(nom, coordonnee)

    def visite(self, joueur, joueurs):
        print(f"{joueur.nom} est en visite à la prison.")
        for joueur in joueurs:
            if joueur.mouvement:
                # si nimporte quelle joueur est emprisonnée, il sera libéré.
                joueur.mouvement = False
                print(f"Vous avez libéré {joueur.nom} de prison.")


    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#
                
    @property
    def type(self):
        return self.__type
