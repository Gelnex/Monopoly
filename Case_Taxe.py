"""
Arriaga Diogo 
08-03-2024
Case police qui donne des malus 
"""
### Imports nécessaires ###
from Case import *

### Définition de la classe ###
class Taxe (Case):
    def __init__(self, nom: str, coordonee: int, argent: int) -> None:
        super().__init__(nom, coordonee)
        self.__prix = argent

    ### Action que la case peut faire ###
    def malus(self, joueur,partie):
            joueur.donner_argent(-self.__prix)
            print(f"Vous avez dû payer {self.__prix}€")
            partie.argentPlateau += self.__prix
            
    
    @property
    def prix(self):
        return self.__prix
    
    @prix.setter
    def prix(self, nvArgent):
        self.__prix = nvArgent
        

### Tests ###
if __name__ == "__main__":
    
    from Joueur import *
    from Case_Police import *
    
    case = Police("Police", 3)
    monJoueur = Joueur("george")
    case.malus(monJoueur)
    
