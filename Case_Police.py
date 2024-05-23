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
Quoi : Case police qui donne des malus 
"""
class Police(Case):
    """
    Qui : Arriaga Diogo
    Quand : 08/03/2024
    Quoi : Constructeur
    """
    
    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, position, nom: str, coordonee: int) -> None:
        super().__init__(position, nom, coordonee , color.gray)

    # ============================================================================#
    # = METHODES                                                                 =#
    # ============================================================================#
    """
    Qui : Arriaga Diogo
    Quand : 08/03/2024
    Quoi : Définire les malus
    """
    def malus(self, joueur, partie):
        match random.randint(1,2):
            case 1:
                joueur.position -= 3
                print("La police vous a reculer de trois cases")
            case 2:
                joueur.donner_argent(-100)
                print("La police vous a retirer 100€")
                partie.argentPlateau += 100
            case _ :
                raise TypeError("Entrée invalide")
        


### Tests ###
if __name__ == "__main__":
    
    from Joueur import *
    
    case = Police("Police", 3)
    monJoueur = Joueur("george")
    case.malus(monJoueur)
    
