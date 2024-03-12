"""
Arriaga Diogo 
08-03-2024
Case police qui donne des malus 
"""
### Imports nécessaires ###
from Case import *
import random

### Définition de la classe ###
class Case_Police (Case):
    def __init__(self, nom: str, coordonee: int) -> None:
        super().__init__(nom, coordonee)

    ### Action que la case peut faire ###
    def malus(self, joueur,partie):
        
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
    
    case = Case_Police("Police", 3)
    monJoueur = Joueur("george")
    case.malus(monJoueur)
    
