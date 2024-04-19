import threading
from Partie import *


def thread():
    # Création d'une instance de la classe Partie avec une liste de joueurs vide
    partie = Partie([])
    
    # Demande du nombre de joueurs à l'utilisateur et récupération de la valeur
    nJoueur = partie.nombre_joueur()
    print("")

    # Initialisation des variables nécessaires 
    joueur_noms = []

    # Demande des noms des joueurs à l'utilisateur et stockage dans une liste
    joueur_noms = partie.identifier_joueur(nJoueur)
    print("")

    # Création d'instances de la classe Joueur à partir des noms fournis par l'utilisateur
    joueurs = [Joueur(nom) for nom in joueur_noms]

    # Création d'une nouvelle instance de la classe Partie avec les joueurs créés
    jeu = partie(joueurs)
    print("Ce pouvoir s'activera quand le joueur fera un double !")

    # Début du jeu
    jeu.jouer()

    
code_thread = threading.Thread(target=thread)
code_thread.start()