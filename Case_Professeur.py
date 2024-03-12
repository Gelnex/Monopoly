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
    def bonus(self, joueur, partie):
        
        match random.randint(1,2):
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
    case = Case_Professeur("Prof", 3)