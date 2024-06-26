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

    def __init__(self, position, nom: str, coordonee: int,  texture = 'white_cube' ,couleur = color.white,) -> None:
        self.__nom = nom
        self.__coordonee = coordonee
        

        ### Initialisation des attributs graphiques ###
        super().__init__(
            model = "cube",
            texture = texture,
            color = couleur,
            position = position,
            scale = (1, 0.1, 1)
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
