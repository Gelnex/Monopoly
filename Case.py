# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from ursina import *

# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
class Case (Entity):
    """
    Qui : Engels Félix
    Quand : 28/02/2024
    Quoi : Permet de gérer toute les autres classe, Attribut et accesseurs
    """

    def __init__(self, nom: str, coordonee: int) -> None:
        self.__nom = nom
        self.__coordonee = coordonee

        ### Initialisation des attributs graphiques ###
        super().__init__(
            model = "cube",
            color = 'red',
            position = position
        )

    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def coordonee(self) -> int:
        return self.__coordonee
