# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
class Case:
    """
    Qui : Engels Félix
    Quand : 28/02/2024
    Quoi : codage de la classe, la classe au paravant possedait une list(range(40)), elle sera deplacer dans plateau car cette classe seras utiliser pour generer toutes les autres cases
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
