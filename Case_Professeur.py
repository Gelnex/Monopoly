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
        super().__init__(position, nom, coordonee, texture = 'ressource\image\cases\professeur.png')

    # ============================================================================#
    # = METHODE                                                                  =#
    # ============================================================================#
    
    """
        Qui : Arriaga Diogo
        Quand : 08/03/2024
        Quoi : Définir le bonus
    """
    def bonus(self,joueur, partie):
        
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
# pour faire le test il faut mettre en commentaire super().__init__()

if __name__ == "__main__":
    class fauxjoueur():
        def __init__(self) -> None:
            self.position = 0
        def donner_argent(self,argent):
            print("argent donné")
    class fauxpartie():
        def donner_argent_plateau(self,joueur):
            print("argent donnée")
            
    prof = Professeur(1,"1",1)
    partie = fauxpartie()
    joueur = fauxjoueur()
    for i in range(5):
        prof.bonus(joueur,partie)
        
            