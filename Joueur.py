from ursina import *

# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
"""
    Qui : Engels Félix
    Quand : 15/02/2024
    Quoi : Création classe joueur
"""
class Joueur:

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
        self.__famille = []
        self.__nombre_tours = 0
        self.__pouvoir = ""
        self.__mouvement = False
        self.pion = Pion()
        
        self.set_pouvoir()

    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#
    """
    Qui : Engels Félix
    Quand : 15/02/2024
    Quoi : setter argent + privatisation
    """
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
    def mouvement(self):
        return self.__mouvement
    
    @property
    def pouvoir(self):
        return self.__pouvoir
    
    @property
    def famille(self):
        return self.__famille

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

    @mouvement.setter
    def mouvement(self, nvbm):
        self.__mouvement = nvbm
        
    @famille.setter
    def famille(self, nvlfamille):
        self.__famille = nvlfamille
        
    # ============================================================================#
    # = METHODE                                                                  =#
    # ============================================================================#
    
    """
    Qui : Engels Félix
    Quand : 15/02/2024
    Quoi : Vérifie si le joueur peut acheter
    """
    def peut_acheter(self, propriete):
        # Retouner un booleén vrai ou faux si l'agent nécessaire est disponible
        return self.argent >= propriete.prix

    """
    Qui : Haye Noa
    Quand : 05/03/2024
    Quoi : Achter la propriete
    """
    def acheter_propriete(self, propriete, partie):
        # Vérifie si la propriété appartient deja au joueur
        if propriete in self.__propriete:
            print("Vous possédez déjà cette propriété.")
        else:
            # Vérifie que la propriétée est libre ou non, si elle est prise, le joueur paye le loyer au propriétaire
            if propriete.proprietaire is not None:
                propriete.payer_loyer(self,partie.joueurs)
            else:
                while True:
                    reponse = input(f"Voulez vous acheter cette propriété pour {propriete.prix}€ ? O/N ")   
                    reponse = reponse.lower()
                    if reponse == "o":
                        propriete.acheter(self)
                        break
                    elif reponse == "n":
                        print(f"{self.nom} n'a pas acheté {propriete.nom}")
                        partie.mettre_aux_encheres(propriete = propriete)
                        break
                    else:
                        print(f"{reponse} n'est pas une entrée valide, veuiller entrer O ou N")
    
    """
    Qui : Engles Felix
    Quand : 20/04/2024
    Quoi : Active les pouvoirs joueurs
    """
    def pouvoir(self, partie,case_actuelle_pos) -> None:
        # regarder pour la valeur correspondante du pouvoir et l'executer
        match self.__pouvoir:
            case "argent":
                self.donner_argent(200)
                print(f"Vous avez grace a votre pouvoir gagner {self.__argent} €")
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
    
    """
    Qui : Engles Felix
    Quand : 20/04/2024
    Quoi : Permet de choisir les poivoir
    """
    def set_pouvoir(self):
        setIn = input(f"{self.nom} choisis un pouvoir :\n 1. Voleur pro : Commencer le jeu avec 200€ en plus \n 2. Roi de l'evasion : Pouvoir sauter des cases max. 5\n 3. Voleur de l'etat : Voler l'argent qui est déposé au milieu de plateau \n Rentrer une valeur (entre 1 et 3) -> ")

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
                    
    """
    Qui : Engels Felix
    Quand : 20/04/2024
    Quoi : Permet de donner l'argent a un joueur
    """
    def donner_argent(self, argent):
        self.argent += argent   



class Pion (Entity):
    def __init__(self):
        super().__init__(
            model = "ressource\pawn.obj",
            scale = (0.2, 0.2, 0.2),
            position = (0, 0.1, 0),
            color = color.random_color(),
            alpha = .6
        )
        