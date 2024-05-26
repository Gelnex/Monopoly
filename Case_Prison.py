# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
from Joueur import *
from Des import *
from ursina import *


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
"""
    Qui : Engels Félix
    Quand : 06-03-24
    Quoi : Ajout de la case prison 
"""
class Prison(Case):
    """
    Qui : Engels Félix
    Quand : 06-03-24
    Quoi : Constructeur
    """

    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, position, nom: str, coordonee: int,visite_prisoncoo) -> None:
        super().__init__(
            position, nom, coordonee, texture = 'ressource\image\cases\prison.png'
        )  # la coordonée devrait etre fix a une case unique
        self.__visite_prisoncoo = visite_prisoncoo
    # ============================================================================#
    # = METHODES                                                                 =#
    # ============================================================================#

    """
    Qui : Engels Félix
    Quand : 06-03-24
    Quoi : Permet de bloquer le joueur quand il se trouve en prison
    """
    def bloquerMouvement(self, joueur, partie):
        # Condition pour sortir
        if joueur.mouvement == True:
            # Appel de la classe Des
            des = Des()
            somme_des, double = des.lancer_des()

            # Condition pour que le joueur puisse sortir
            if double:
                print(f"{joueur.nom} a fait un double et sort donc de prison")
                joueur.position = self.__visite_prisoncoo
                joueur.mouvement = False

            else:
                while True:
                    reponse = input("Vouler vous payer pour sortir (200€) ? O/N ")
                    if reponse == "o" or reponse == "O":
                        joueur.position = self.__visite_prisoncoo
                        joueur.mouvement = False
                        joueur.donner_argent(-200)
                        partie.argentPlateau += 200
                        print(f"{joueur.nom} a payer et sort donc de prison")
                        break
                    elif reponse == "n" or reponse == "N":
                        break
                    else:
                        print(f"{reponse} n'est pas une entrée valide, veuiller entrer O ou N")
        else:
            joueur.mouvement = True

    # ============================================================================#
    # = AFFICHAGE DE LA CLASSE                                                   =#
    # ============================================================================#
    def __str__(self):
        return f"Prison {super().__nom} et je suis situé en {super().__coordonee}"
    
### Tests ###
# pour faire les test il faut mettre en commentaire super().__init__()
if __name__ == "__main__":
    class faux():
        def __init__(self):
            self.argentPlateau = 100
            self.position = 0
            self.mouvement = True
            self.nom = "test"
            print(f" valeurs avant modifications : {self.argentPlateau,self.position,self.mouvement}")
        def donner_argent(self, prix):
            print("argent modifié !")

    partie= faux()
    prison = Prison((0,0,0),"test",10,20)
    prison.bloquerMouvement(partie,partie)
    print(f" valeurs après modifications : {partie.argentPlateau,partie.position,partie.mouvement}")
    
            
