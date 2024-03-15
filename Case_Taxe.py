"""
Arriaga Diogo 
08-03-2024
Case police qui donne des malus 
"""
### Imports nécessaires ###
from Case import *

### Définition de la classe ###
class Taxe (Case):
    def __init__(self, nom: str, coordonee: int) -> None:
        super().__init__(nom, coordonee)

    ### Action que la case peut faire ###
    def malus(self, joueur,partie , argent):
            joueur.donner_argent(-argent)
            print(f"La police vous a retirer {argent}€")
            partie.argentPlateau += argent
            
        


### Tests ###
if __name__ == "__main__":
    
    from Joueur import *
    
    case = Case_Police("Police", 3)
    monJoueur = Joueur("george")
    case.malus(monJoueur)
    
