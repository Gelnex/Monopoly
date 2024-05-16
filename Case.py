# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
class Case:
    """
    Qui : Engels Félix
    Quand : 28/02/2024
    Quoi : Permet de gérer toute les autres classe, Attribut et accesseurs
    """

    def __init__(self, nom: str, coordonee: int) -> None:
        self.__nom = nom
        self.__coordonee = coordonee

    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def coordonee(self) -> int:
        return self.__coordonee
