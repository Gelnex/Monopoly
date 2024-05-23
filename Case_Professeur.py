# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
import random
from ursina import *


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
"""
    Qui : Arriaga Diogo
    Quand : 08/03/2024
    Quoi : Case professeur qui donne des bonus 
"""
class Professeur (Case):
    """
    Qui : Arriaga Diogo
    Quand : 08/03/2024
    Quoi : Constructeur
    """
    
    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, position, nom: str, coordonee: int) -> None:
        super().__init__(position, nom, coordonee, couleur = color.white)    
    

    # ============================================================================#
    # = METHODE                                                                  =#
    # ============================================================================#
    
    """
        Qui : Arriaga Diogo
        Quand : 08/03/2024
        Quoi : Définir le bonus
    """
    def bonus(self, joueur, partie):
        
        match random.randint(1,3):
            case 1:
                joueur.position += 3
                print("Le professeur vous a avancer de 3 cases")
            case 2:
                joueur.donner_argent(100)
                print("Le professeur vous a donné 100€")
            case 3:
                partie.donner_argent_plateau(joueur)
            case _ :
                raise TypeError("Entrée invalide")


### Tests ###
if __name__ == "__main__":
    case = Professeur("Prof", 3)