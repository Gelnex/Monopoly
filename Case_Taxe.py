# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
"""
    Qui : Arriaga Diogo
    Quand : 08/03/2024
    Quoi : Case police qui donne des malus 
"""
class Taxe (Case):
    """
    Qui : Arriaga Diogo
    Quand : 08/03/2024
    Quoi : Constructeur et property
    """
    
    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, nom: str, coordonee: int, argent: int) -> None:
        super().__init__(nom, coordonee)
        self.__prix = argent

    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#
    @property
    def prix(self):
        return self.__prix
    
    # ============================================================================#
    # = METHODE                                                                  =#
    # ============================================================================#
    
    """
    Qui : Arriaga Diogo
    Quand : 08/03/2024
    Quoi : Définition du malus
    """
    def malus(self, joueur,partie):
            joueur.donner_argent(-self.__prix)
            print(f"Vous avez dû payer {self.__prix}€")
            partie.argentPlateau += self.__prix
            
        

### Tests ###
if __name__ == "__main__":
    
    from Joueur import *
    from Case_Police import *
    
    case = Police("Police", 3)
    monJoueur = Joueur("george")
    case.malus(monJoueur)
    
