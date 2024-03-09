"""
Arriaga Diogo 
08-03-2024
Case professeur qui donne des bonus 
"""
### Imports nécessaires ###
from Case import *
import random

### Définition de la classe ###
class Case_Professeur (Case):
    def __init__(self, nom: str, coordonee: int) -> None:
        super().__init__(nom, coordonee)

    ### Action que la case peut faire ###
    def bonus(self, joueur):
        
        match random.randint(1,2):
            case 1:
                joueur.position += 3
                print("La police vous a descendu de trois cases")
            case 2:
                joueur.donner_argent(100)
                print("La police vous a descendu de trois cases")
            case _ :
                raise TypeError("entrée invalide")


### Tests ###
if __name__ == "__main__":
    case = Case_Professeur("Prof", 3)