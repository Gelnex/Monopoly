"""
Arriaga Diogo / Noa Haye
17/05/2024
Interface graphique pour jouer au jeu
"""
# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
import threading
from Partie import *
from ursina import *

# ============================================================================#
# = DEFINITION DE LA CLASSE ACCUEIL                                          =#
# ============================================================================#
class Accueil(Entity):
    def __init__(self):
        super().__init__()
        self.image = Entity(
            parent=camera.ui,
            model='quad',
            texture='ressource/image/accueil.png', 
            scale=(1.6, 0.9)
        )

        self.button = Button(
            parent=camera.ui,
            model='quad',
            texture='white_cube',
            color=color.red,
            scale=(.4, .1),
            position=(0, -.3),
            text='Jouer',  # Texte à afficher à l'intérieur du bouton
            text_origin=(0, 0),  # Position du texte (centre du bouton)
            text_color=color.white,  # Couleur du texte
            text_font='font/test.otf',
            text_size=3,
            on_click=self.switch_jeu
        )

    def switch_jeu(self):
        self.enabled = False  # Supprimer l'entité "Accueil" et tous ses enfants
        self.button.enabled = False
        self.image.enabled = False
        camera = EditorCamera()
        Sky()
        interface = Jeu()
        interface.start_game()

        # Initialiser la scène "Jeu"
        scene = Jeu()

# ============================================================================#
# = DEFINITION DE LA CLASSE JEU (PRINCIPALE)                                 =#
# ============================================================================#
class Jeu(Entity):
    def __init__(self):
        self.__passer_au_tour_suivant = False
        super().__init__(
            model = 'cube',
            texture = 'ressource/image/planche.jfif',
            scale = (15, 0.3, 15),
            position = (5, -0.25, 5)
        )
        centre_plateau = Entity(
            model = 'cube',
            texture = 'ressource/image/plateau.png',
            scale = (9, 0.1, 9),
            position = (5, 0, 5)
        )

        self.button = Button(
            parent=camera.ui,
            model='quad',
            texture='white_cube',
            color=color.red,
            scale=(.4, .1),
            position=(0.6, -0.4),
            text='Lancer les dés',  # Texte à afficher à l'intérieur du bouton
            text_origin=(0, 0),  # Position du texte (centre du bouton)
            text_color=color.white,  # Couleur du texte
            text_font='font/test.otf',
            text_size=2,
            on_click = self.passer_tour_suivant,
            enabled = False
        )

    def passer_tour_suivant (self):
        self.__passer_au_tour_suivant = True


    # Fonction pour démarrer le jeu
    def start_game(self):
        # Lancer le thread pour le jeu
        code_thread = threading.Thread(target=self.thread)
        code_thread.start()



    # Fonction pour initialiser le jeu
    def thread(self):

        # Début du jeu
        self.button.enabled = True
        while True:
            if self.__passer_au_tour_suivant == True:
                self.button.enabled = False
                self.__passer_au_tour_suivant = False
                break

        while len(jeu.joueurs) > 1:
            jeu.jouer()
            self.button.enabled = True
            while True:
                if self.__passer_au_tour_suivant == True:
                    self.button.enabled = False
                    self.__passer_au_tour_suivant = False
                    break


### Définition d'un boutton pour quitter ###
def input(key):
    if key == "escape":
        quit()


### Création de ursina ###
app = Ursina()

### Entrer les données des joueurs ###
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
jeu = Partie(joueurs)
print("Ce pouvoir s'activera quand le joueur fera un double !")


# Initialisation de l'interface graphique dans le thread principal
scene = Accueil()
app.run()