"""
Arriaga Diogo 
08-03-2024
Case professeur qui donne des bonus 
"""
### Imports nécessaires ###
from Case import *

### Définition de la classe ###
class Case_Professeur (Case):
    def __init__(self, nom: str, coordonee: int) -> None:
        super().__init__(nom, coordonee)

    ### Action que la case peut faire ###
    def Action01 (self, joueur):
        joueur.bouger(3)
        print (joueur.position)

    def Action02 (self, joueur):
        joueur.donner_argent(100)
        print (joueur.argent)


### Tests ###
case = Case_Professeur("Prof", 3)