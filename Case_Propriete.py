# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
from Joueur import *
import random
from ursina import *

"""
Qui : Félix Engels
Quand : 04/03/2024
Quoi : Case qui contient les proprietés (maison)
"""
# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
class Propriete(Case):
    """
    Qui : Félix Engels
    Quand : 04/03/2024
    Quoi : Constructeur, accesseurs et mutateur
    """
    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, positioninit, nom, numero, famille, prix):
        super().__init__(positioninit, nom, numero, texture = 'ressource\image\cases\propriete.png')
        famille_cube = Entity(
            model = 'sphere',
            color = self.matchFamille(input = famille),
            scale = (.1, .1, .1),
            position = positioninit + (0, 0.25, 0),
            alpha = .2
        )
        
        
        self.__type = "propriete"
        self.__famille = famille
        self.__prix = prix
        self.__loyer = prix / 2
        self.__proprietaire = None
        self.__carte_or = random.choice(["argent", "parc", "vol"])
        self.lingot_or = Lingot_or(positioninit)

    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#
    @property
    def type(self):
        return self.__type
        
    @property
    def prix(self):
        return self.__prix
    
    @property
    def loyer(self):
        return self.__loyer

    @property
    def proprietaire(self):
        return self.__proprietaire
    
    @property
    def famille(self):
        return self.__famille


    # ============================================================================#
    # = MUTATEURS                                                                =#
    # ============================================================================#

    @proprietaire.setter
    def proprietaire(self, joueur):
        self.__proprietaire = joueur

    # ============================================================================#
    # = METHODE                                                                  =#
    # ============================================================================#
    """
    Qui : Félix Engels
    Quand : 04/03/2024
    Quoi : Retire l'argent du joueur quand il tombe sur la case d'un autre joueur
    """
    def payer_loyer(self, joueur, joueurs) -> None:
        loyer = self.loyer
        for itterateurJoueurs in joueurs:
            if self.famille in itterateurJoueurs.famille:
                loyer *= 2
                break
        joueur.argent -= loyer
        print(
            f"La propriété {self.nom} appartient déjà à {self.proprietaire.nom}. {joueur.nom} a donc payé {loyer} euros de loyer à {self.proprietaire.nom}."
        )

    """
    Qui : Félix Engels
    Quand : 04/03/2024
    Quoi : Achat de la case par un joueur
    """
    def acheter(self, joueur):
        joueur.propriete.append(self)
        joueur.argent -= self.__prix
        self.proprietaire = joueur
        print(
            f"{joueur.nom} a acheté la propriété {self.nom} pour {self.__prix}€ "
        )
    
    """
    Qui : Félix Engels
    Quand : 04/03/2024
    Quoi : Achat de la case enchere par un joueur
    """
    def acheter_enchere(self, joueur, prix):
        joueur.propriete.append(self)
        joueur.argent -= prix
        self.proprietaire = joueur
        print(
            f"{joueur.nom} a acheté la propriété {self.nom} pour {prix}€ "
        )
    
    """
    Qui : Félix Engels
    Quand : 04/03/2024
    Quoi : Définit l'action de la carte or
    """
    def actionOr(self, joueur, partie):
        # Vérifier si il y a une carte or
        if self.__carte_or != None :
            print("######## carte or ########")
            match self.__carte_or:
                case "argent":
                    joueur.donner_argent(200)
                    print(f"Vous avez grace a la carte or gagné 200€")
                case "parc":
                   partie.donner_argent_plateau(joueur)
                case "vol":
                    iptVol = input("Rentrer le nom du joueur au quel vous vouler voler 150€ -> ")
                    vrf = True
                    while vrf:
                        for iJoueur in partie.joueurs:
                            if iJoueur.nom == iptVol  and iptVol != joueur.nom:
                                print(f"{joueur.nom} a volé 150€ à {iptVol} !")                          
                                iJoueur.argent -= 150
                                joueur.argent += 150
                                vrf = False
                                break
                        if vrf:
                            iptVol = input("Le joueur n'a pas été trouvé ou il s'agit de vous-même, verifier le nom et réentrer le -> ")
                case _ :
                    raise TypeError("Case n'existe pas, veuiller verfier le constructeur")
            # Enleve la carte or de la case
            self.__carte_or = None
            self.lingot_or.enabled = False
            print("##########################")


            
    def matchFamille(self,input):
        match input:
            case "brune":
                return color.brown
            case "blanche":
                return color.white
            case "violet":
                return color.violet
            case "outil":
                return color.black
            case "orange":
                return color.orange
            case "rouge":
                return color.red
            case "jaune":
                return color.yellow
            case "vert":
                return color.green
            case "bleu":
                return color.blue
            case _ :
                raise TypeError("couleur non trouvé")
            

class Lingot_or(Entity):
    def __init__(self, positioninit):
        super().__init__(
            model = 'cube',
            name = 'lingot_or',
            texture = 'white_cube',
            color = color.yellow,
            scale = (.2, .1, .1),
            position = positioninit + (0, 0.1, 0),
            alpha = .5,
            enabled = True
        )

# ============================================================================#
# = test                                                                     =#
# ============================================================================#

if __name__ == "__main__":
    case01 = Propriete("george", 4, "bleu clair", 250)
    try:
        case01.prix = 2
    except:
        print("test réussi")
    else:
        print("test raté")

    try:
        case01.coordonee = 2
    except:
        print("test réussi")
    else:
        print("test raté")

    try:
        case01.nom = 2
    except:
        print("test réussi")
    else:
        print("test raté")

    print("test acheter")

    joueur01 = Joueur()
    print(f"l'argent du joueur est {joueur01.argent}")
    case01.acheter(joueur01)
    print(f"l'argent du joueur est {joueur01.argent}")

    print("test loyer")

    print(f"l'argent du joueur est {joueur01.argent}")
    case01.payer_loyer(joueur01)
    print(f"l'argent du joueur est {joueur01.argent}")

    print("test carte or")

    case01.generer_carte_or()
    print(case01.carte_or)
