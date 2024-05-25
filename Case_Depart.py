# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
from Joueur import *
from ursina import *


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
"""
Qui : Arriaga Diogo
Quand : 05-03-24
Quoi : Case départ qui donne de l'argent
"""
class Depart(Case):
    """
    Qui : Arriaga Diogo
    Quand : 05-03-24
    Quoi : Constructeur et accesseur
    """

    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, position, nom: str, coordonee: int) -> None:

        ### Lister et initialiser les attributs
        super().__init__(position, nom, coordonee,texture = 'ressource\image\cases\départ.png')
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
    
    """
    Qui : Arriaga Diogo
    Quand : 05-03-24
    Quoi : Donner l'argent de la case de départ
    """
    def donner_argent(self, joueur):
        print(f"{joueur.nom} est arrivé sur la case Départ. Il reçoit 200 euros.")
        joueur.argent += 200

    # ============================================================================#
    # = AFFICHAGE DE LA CLASSE                                                   =#
    # ============================================================================#
    def __str__(self):
        return f"Case_depart[Argent à donner{self.__argent_a_donner}]"
