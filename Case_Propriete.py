# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
from Joueur import *
import random


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
class Propriete(Case):
    """
    Qui : Félix Engels
    Quand : 04/03/2024
    Quoi : tests
    """
    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, nom, numero, couleur, prix):
        super().__init__(nom, numero)
        self.__type = "propriete"
        self.__couleur = couleur
        self.__prix = prix
        self.__loyer = prix / 2
        self.__proprietaire = None
        self.__carte_or = random.choice(["argent", "parc", "vol"])

    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#
    @property
    def type(self):
        return self.__type

    @property
    def type(self):
        return self.__couleur

    @property
    def prix(self):
        return self.__prix

    @property
    def proprietaire(self):
        return self.__proprietaire

    # ============================================================================#
    # = MUTATEURS                                                                =#
    # ============================================================================#

    @proprietaire.setter
    def proprietaire(self, joueur):
        self.__proprietaire = joueur

    # ============================================================================#
    # = METHODE                                                                  =#
    # ============================================================================#

    # Retire l'argent du joueur quand il tombe sur la case d'un autre joueur
    def payer_loyer(self, joueur) -> None:
        joueur.argent -= self.__loyer
        print(
            f"La propriété {self.nom} appartient déjà à {self.proprietaire.nom}. {joueur.nom} a donc payé {self.__loyer} euros de loyer à {self.proprietaire.nom}."
        )

    # Achat de la case par un joueur
    def acheter(self, joueur):
        joueur.propriete.append(self)
        joueur.argent -= self.__prix
        self.proprietaire = joueur
        print(
            f"{joueur.nom} a acheté la propriété {self.nom} pour {self.__prix}€ "
        )
        
    def acheter_enchere(self, joueur, prix):
        joueur.propriete.append(self)
        joueur.argent -= prix
        self.proprietaire = joueur
        print(
            f"{joueur.nom} a acheté la propriété {self.nom} pour {prix}€ "
        )
    
    # Action de la carte or
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
            print("##########################")
        
        

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
