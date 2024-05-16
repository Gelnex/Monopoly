import threading
from Partie import *
from ursina import *

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
            on_click=self.switch_nbrJoueur
        )

    def switch_nbrJoueur(self):
        self.enabled = False  # Supprimer l'entité "Accueil" et tous ses enfants
        self.button.enabled = False
        self.image.enabled = False
        # Initialiser la scène "NbrJoueur"
        scene = Jeu()

class Jeu(Entity):
    def __init__(self):
        super().__init__(
            model = "cube",
            scale = (50, 0.01 ,50),
            texture = 'ressource/image/plateau.jpg',
        )
        self.image = Entity(
            parent=camera.ui,
            model='quad',
            texture='ressource/image/console.png', 
            scale=(1.6, 0.9)
        )
        
        self.button1 = Button(
            parent=camera.ui,
            model='quad',
            texture='white_cube',
            color=color.red,
            scale=(.4, .1),
            position=(0, -.3),
            text='Test',  # Texte à afficher à l'intérieur du bouton
            text_origin=(0, 0),  # Position du texte (centre du bouton)
            text_color=color.white,  # Couleur du texte
            text_font='font/test.otf',
            text_size=3,
            on_click=self.switch_game
        )

        self.button2 = Button(
            parent=camera.ui,
            model='quad',
            texture='white_cube',
            color=color.red,
            scale=(.4, .1),
            position=(0, -.3),
            text='Tour suivant',  # Texte à afficher à l'intérieur du bouton
            text_origin=(0, 0),  # Position du texte (centre du bouton)
            text_color=color.white,  # Couleur du texte
            text_font='font/test.otf',
            text_size=3,
            on_click=self.passer_au_tour_suivant(),
            enabled = False
        )

    def passer_au_tour_suivant (self):
        


    def switch_game(self):
        self.button1.enabled = False
        self.image.enabled = False
        camera = EditorCamera()
        self.start_game()


    # Fonction pour démarrer le jeu
    def start_game(self):
        # Lancer le thread pour le jeu
        code_thread = threading.Thread(target=self.thread)
        code_thread.start()

    # Fonction pour initialiser le jeu
    def thread(self):

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

        self.button2.enabled = True

        # Début du jeu
        while len(jeu.joueurs) > 1:
            jeu.jouer()
            self.button2.enabled = True


### Définition d'un boutton pour quitter ###
def input(key):
    if key == "escape":
        quit()

# Initialisation de l'interface graphique dans le thread principal
app = Ursina()
scene = Accueil()
app.run()
        