# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
from Joueur import *


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
"""
    Qui : Félix Engels
    Quand : 04/03/2024
    Quoi : tests
"""


class Tunnel(Case):

    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, nom, numero):
        super().__init__(nom, numero)
        

    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#
    

    # ============================================================================#
    # = MUTATEURS                                                                =#
    # ============================================================================#

   
    # ============================================================================#
    # = METHODE                                                                  =#
    # ============================================================================#
    
    def transporter(self, joueur):
        while True:
            try:
                ipt = int(input("De combien de cases voulez-vous sauter (maximum 9) -> "))
                if 1 <= ipt <= 9:
                    break
                else:
                    print("Le nombre saisi doit être entre 1 et 9 inclus.")
            except ValueError:
                print("L'entrée doit être un nombre entier.")
        
        joueur.position += ipt
        print(f"Vous êtes maintenant sur la case N°{joueur.position + 1}")

        
