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
    Quoi : Permet de se déplacer de plusieurs cases
"""
class Tunnel(Case):
    """
        Qui : Félix Engels
        Quand : 04/03/2024
        Quoi : Création de Constructeur
    """
    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, nom, numero):
        super().__init__(nom, numero)
        
    # ============================================================================#
    # = METHODE                                                                  =#
    # ============================================================================#
    
    """
        Qui : Félix Engels
        Quand : 04/03/2024
        Quoi : Demande au joueur  de combiens de cases veut-il sauter 
    """
    def transporter(self, joueur):
        while True:
            try:
                case_sauter = int(input("De combien de cases voulez-vous sauter (maximum 9) -> "))
                if 1 <= case_sauter <= 9:
                    break
                else:
                    print("Le nombre saisi doit être entre 1 et 9 inclus.")
            except ValueError:
                print("L'entrée doit être un nombre entier.")
        
        joueur.position += case_sauter
        print(f"Vous êtes maintenant sur la case N°{joueur.position + 1}")

        
