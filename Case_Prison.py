# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
from Joueur import *
from Des import *


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
"""
    Qui : Engels Félix
    Quand : 06-03-24
    Quoi : Ajout de la case prison 
"""
class Prison(Case):
    """
    Qui : Engels Félix
    Quand : 06-03-24
    Quoi : Constructeur
    """

    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, nom: str, coordonee: int) -> None:
        super().__init__(
            nom, coordonee
        )  # la coordonée devrait etre fix a une case unique

    # ============================================================================#
    # = METHODES                                                                 =#
    # ============================================================================#

    """
    Qui : Engels Félix
    Quand : 06-03-24
    Quoi : Permet de bloquer le joueur quand il se trouve en prison
    """
    def bloquerMouvement(self, joueur, partie):
        # Condition pour sortir
        if joueur.mouvement == True:
            # Appel de la classe Des
            des = Des()
            somme_des, double = des.lancer_des()

            # Condition pour que le joueur puisse sortir
            if double:
                print(f"{joueur.nom} a fait un double et sort donc de prison")
                joueur.position = 10
                joueur.mouvement = False

            else:
                while True:
                    reponse = input("Vouler vous payer pour sortir (200€) ? O/N ")
                    if reponse.lower == "o":
                        joueur.position = 10
                        joueur.mouvement = False
                        joueur.donner_argent(-200)
                        partie.argentPlateau += 200
                        print(f"{joueur.nom} a payer et sort donc de prison")
                        break
                    elif reponse.lower == "n":
                        break
                    else:
                        print(f"{reponse} n'est pas une entrée valide, veuiller entrer O ou N")
        else:
            joueur.mouvement = True

    # ============================================================================#
    # = AFFICHAGE DE LA CLASSE                                                   =#
    # ============================================================================#
    def __str__(self):
        return f"Prison {super().__nom} et je suis situé en {super().__coordonee}"
