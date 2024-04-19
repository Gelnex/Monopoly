# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
import random

# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
class Police(Case):
    """
    Qui : Arriaga Diogo
    Quand : 08/03/2024
    Quoi : Case police qui donne des malus 
    """
    
    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, nom: str, coordonee: int) -> None:
        super().__init__(nom, coordonee)

    # ============================================================================#
    # = METHODES                                                                 =#
    # ============================================================================#
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
    
