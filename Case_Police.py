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
        super().__init__(position, nom, coordonee , texture = 'ressource\image\cases\police.png')
        pass

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
# pour faire le test il faut mettre en commentaire super().__init__()

if __name__ == "__main__":
    class fauxjoueur():
        def __init__(self) -> None:
            self.position = 0
        def donner_argent(self,argent):
            print("argent donné")
    class fauxpartie():
        def __init__(self):
            self.argentPlateau = 100
        def donner_argent_plateau(self,joueur):
            print("argent donnée")
            
    prof = Police(1,"1",1)
    partie = fauxpartie()
    joueur = fauxjoueur()
    for i in range(5):
        prof.malus(joueur,partie)
        
