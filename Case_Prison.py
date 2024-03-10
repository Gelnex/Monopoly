# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
from Joueur import *
from Des import *


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
class Prison(Case):
    """
    Qui : Engels Félix
    Quand : 06-03-24
    Quoi :
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

    def bloquerMouvement(self, joueur, argentPlateau):
        # Condition pour sortir
        if joueur.bloquerMouvement == True:
            # Appel de la classe Des
            des = Des()
            somme_des, double = des.lancer_des()

            if double:
                print(f"{joueur.nom} a fait un double et sort donc de prison")
                joueur.bloquerMouvement = False

            else:
                while True:
                    reponse = input("vouler vous payer pour sortir (200€) ? O/N ")
                    if reponse == "O":
                        joueur.bloquerMouvement = False
                        joueur.donner_argent(-200)
                        argentPlateau += 200
                        print(f"{joueur.nom} a payer et sort donc de prison")
                        break
                    elif reponse == "N":
                        break
                    else:
                        print(f"{reponse} n'est pas une entrée valide, veuiller entrer O ou N")
        else:
            joueur.bloquerMouvement = True

    # ============================================================================#
    # = AFFICHAGE DE LA CLASSE                                                   =#
    # ============================================================================#
    def __str__(self):
        return f"Prison {super().__nom} et je suis situé en {super().__coordonee}"
