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
        self.__pouvoir = ""
        self.__bloquerMouvement = False
        
        self.set_pouvoir()

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
    
    @property
    def pouvoir(self):
        return self.__pouvoir

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
            if propriete.proprietaire is not None:
                propriete.payer_loyer(self)
            else:
                while True:
                    reponse = input(f"Voulez vous acheter cette propriété pour {propriete.prix}€ ? O/N ")
                    if reponse == "O" or "o":
                        propriete.acheter(self)
                        break
                    elif reponse == "N" or "n":
                        print(f"{self.nom} n'a pas acheté {propriete.nom}")
                        break
                    else:
                        print(f"{reponse} n'est pas une entrée valide, veuiller entrer O ou N")
                    
    def pouvoir(self, partie) -> None:
        match self.__pouvoir:
            case "argent":
                self.donner_argent(200)
                print(f"Vous avez grace a votre pouvoir {self.__argent} €")
            case "position":
                posPouvoir = int(input(f"Vous etes sur la case N°{self.__position} de combien de case voulez vous sauter ? (max 5) -> "))
                while True:
                    if 0 < posPouvoir <= 5:
                        self.__position += posPouvoir
                        break
                    else:
                        posPouvoir = int(input(f"L'entrée {posPouvoir} est incorrect. entrer un nombre entre 1 et 5 -> "))
            case "parc":
                partie.donner_argent_plateau(self)
            case _ :
                raise TypeError("Case n'existe pas, veuiller verfier le constructeur")
        
    def set_pouvoir(self):
        setIn = input(f"{self.nom} choisis un pouvoir :\n 1. Voleur pro (+200€) \n 2. Roi de l'evasion \n 3. voleur de l'etat \n rentrer une valeur -> ")

        while True:
                
            match setIn:
                case '1':
                    self.__pouvoir = "argent"
                    break
                case '2':
                    self.__pouvoir = "position"
                    break
                case '3':
                    self.__pouvoir = "parc"
                    break
                case _ :
                    setIn = input(f"L'entrée {setIn} est incorrect, réessayer avec 1, 2 ou 3 -> ")
                    
                    

    def incrementer_nombre_tours(self):
        self.nombre_tours += 1

    def donner_argent(self, argent):
        self.argent += argent   