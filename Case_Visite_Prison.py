# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
from Partie import *
from ursina import *


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
"""
    Qui : Noa Haye
    Quand : 05/03/2024
    Quoi : Visiter la prison (Ne Fait Rien)
"""
class Visite_Prison(Case):
    """
    Qui : Noa Haye
    Quand : 05/03/2024
    Quoi : Création de constructeur et Accesseur
    """

    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    
    def __init__(self, position, nom, coordonnee):
        """super().__init__(position, nom, coordonnee,couleur=color.dark_gray)


    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#
                 


    # ============================================================================#
    # = METHODE                                                               =#
    # ============================================================================#
    
    Qui : Noa Haye
    Quand : 05/03/2024
    Quoi : Permet de visiter la prison
    """
    def visite(self, joueur, joueurs):
        print(f"{joueur.nom} est en visite à la prison.")
        for joueur in joueurs:
            if joueur.mouvement:
                # si nimporte quelle joueur est emprisonnée, il sera libéré.
                joueur.mouvement = False
                joueur.position = 4
                print(f"Vous avez libéré {joueur.nom} de prison.")

### test ###
# pour faire le test il faut mettre en commentaire super().__init__()
if __name__ == "__main__":
    class fauxjoueur():
        def __init__(self):
            self.mouvement = True
            self.position = 20
            self.nom = "test"

    joueur = fauxjoueur()
    joueurs= [fauxjoueur() for i in range(2)]

    print(f"valeurs avant test : {joueur.position,joueur.mouvement,joueur.nom,joueurs[0].position,joueurs[0].mouvement,joueurs[0].nom,joueurs[1].position,joueurs[1].mouvement,joueurs[1].nom}")

    test = Visite_Prison(1,"2",3)

    test.visite(joueur,joueurs)

    print(f"valeurs avant test : {joueur.position,joueur.mouvement,joueur.nom,joueurs[0].position,joueurs[0].mouvement,joueurs[0].nom,joueurs[1].position,joueurs[1].mouvement,joueurs[1].nom}")
