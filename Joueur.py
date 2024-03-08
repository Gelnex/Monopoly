# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
class Joueur:
    """
    Qui : Engels Félix
    Quand : 15/02/2024
    Quoi : setter argent + privatisation
    """

    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, nvnom="invité") -> None:
        """
        Qui : Arriaga Diogo
        Quand : 15/02/2024
        Quoi : Constructeur
        """

        self.__nom = nvnom
        self.__argent = 1500
        self.__position = 0
        self.__propriete = []
        self.__nombre_tours = 0
        self.__bloquerMouvement = False

    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#
    @property
    def nom(self):
        return self.__nom

    @property
    def argent(self):
        return self.__argent

    @property
    def position(self):
        return self.__position

    @property
    def propriete(self):
        return self.__propriete

    @property
    def nombre_tours(self):
        return self.__nombre_tours

    @property
    def bloquerMouvement(self):
        return self.__bloquerMouvement

    # ============================================================================#
    # = MUTATEURS                                                                =#
    # ============================================================================#

    @nom.setter
    def nom(self, nvNom):
        self.__nom = nvNom

    @argent.setter
    def argent(self, nvArgent):
        self.__argent = nvArgent

    @position.setter
    def position(self, nvPosition):
        self.__position = nvPosition

    @nombre_tours.setter
    def nombre_tours(self, nvTour):
        self.__nombre_tours = nvTour

    @bloquerMouvement.setter
    def bloquerMouvement(self, nvbm):
        self.__bloquerMouvement = nvbm

    # ============================================================================#
    # = METHODE                                                                  =#
    # ============================================================================#

    def peut_acheter(self, propriete):
        return self.argent >= propriete.prix

    def acheter_propriete(self, propriete):
        if propriete in self.__propriete:
            print("Vous possédez déjà cette propriété.")
        else:
            while True:
                reponse = input("Voulez vous acheter cette propriété ? O/N ")
                if reponse == "O":
                    propriete.acheter(self)
                    break
                elif reponse == "N":
                    print(f"{self.nom} n'a pas acheté {propriete.nom}")
                    break
                else:
                    print(f"{reponse} n'est pas une entrée valide, veuiller entrer O ou N")
                    

    def incrementer_nombre_tours(self):
        self.nombre_tours += 1

    def donner_argent(self, argent):
        self.argent += argent
