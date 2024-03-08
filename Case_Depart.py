# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
from Joueur import *


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
class Depart(Case):
    """
    Qui : Arriaga Diogo
    Quand : 05-03-24
    Quoi : Case départ qui donne de l'argent
    """

    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, nom: str, coordonee: int) -> None:
        """
        Qui : Arriaga Diogo
        Quand : 05-03-24
        Quoi : Constructeur
        """

        ### Lister et initialiser les attributs
        super().__init__(nom, coordonee)
        self.__type = "depart"

    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#
    @property
    def type(self):
        return self.__type

    # ============================================================================#
    # = METHODE                                                                  =#
    # ============================================================================#
    def donner_argent(self, joueur):
        print(f"{joueur.nom} est arrivé sur la case Départ. Il reçoit 200 euros.")
        joueur.argent += 200

    # ============================================================================#
    # = AFFICHAGE DE LA CLASSE                                                   =#
    # ============================================================================#
    def __str__(self):
        return f"Case_depart[Argent à donner{self.__argent_a_donner}]"
