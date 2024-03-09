# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
from Joueur import *
import random


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
"""
    Qui : Félix Engels
    Quand : 04/03/2024
    Quoi : tests
"""


class Propriete(Case):

    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, nom, numero, couleur, prix, loyer):
        super().__init__(nom, numero)
        self.__type = "propriete"
        self.__couleur = couleur
        self.__prix = prix
        self.__loyer = loyer
        self.__proprietaire = None
        self.__carte_or = random.choice(["argent", "position", "vol"])

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

    def payer_loyer(self, joueur) -> None:
        joueur.argent -= self.__loyer
        print(
            f"La propriété {self.nom} appartient déjà à {self.proprietaire.nom}. {joueur.nom} a donc payé {self.__loyer} euros de loyer à {self.proprietaire.nom}."
        )

    def acheter(self, joueur):
        if self.proprietaire is not None:
            self.payer_loyer(joueur)
        else:
            joueur.propriete.append(self)
            joueur.argent -= self.__prix
            self.proprietaire = joueur
            print(
                f"{joueur.nom} a acheté la propriété {self.nom} pour {self.__prix} euros."
            )
            
    def actionOr(self, joueur, listeJoueurs):
        if self.__carte_or != None :
            print("######## carte or ########")
            match self.__carte_or:
                case "argent":
                    joueur.donner_argent(200)
                    print(f"vous avez grace a la carte or {joueur.argent} €")
                case "position":
                    posPouvoir = int(input("combien de case voulez vous sauter ? (max 5) -> "))
                    while True:
                        if 0 < posPouvoir <= 5:
                            joueur.position += posPouvoir
                            break
                        else:
                            posPouvoir = int(input(f"l'entrée {posPouvoir} est incorrect. entrer un nombre entre 1 et 5 -> "))
                case "vol":
                    iptVol = input("rentrer le nom du joueur au quel vous vouler voler 150€ -> ")
                    vrf = True
                    while vrf:
                        for iJoueur in listeJoueurs:
                            if iJoueur.nom == iptVol:                          
                                iJoueur.argent -= 150
                                joueur.argent += 150
                                vrf = False
                                break
                        if vrf:
                            iptVol = input("le joueur n'a pas été trouver, verifier le nom et réentrer le -> ")
                case _ :
                    raise TypeError("case n'existe pas, veuiller verfier le constructeur")
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
