import threading
from Partie import *
from ursina import *

class InputForm(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=camera.ui, scale=0.1, **kwargs)
        self.input_field = InputField(parent=self, scale=Vec2(1, 0.5))

    def input(self, key):
        if key == 'enter':
            print("Entered text:", self.input_field.text)

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
            text='Jouer',
            text_origin=(0, 0),
            text_color=color.white,
            text_font='font/test.otf',
            text_size=100,
            on_click=self.switch_nbrJoueur
        )

    def switch_nbrJoueur(self):
        self.enabled = False
        self.button.enabled = False
        scene = NbrJoueur()

class NbrJoueur(Entity):
    def __init__(self):
        super().__init__()

        screen_width, screen_height = window.size

        self.image = Entity(
            parent=camera.ui,
            model='quad',
            texture='ressource/image/nbrJoueur.png', 
            scale=(1.6, 0.9),
            position=(0, screen_height / 4),
            render_queue=1  # Set a lower render order to render first (background)
        )

        self.input_form = InputForm(position=(0, 0), render_queue=2)  # Set a higher render order to render last (foreground)

        self.button = Button(
            parent=camera.ui,
            model='quad',
            texture='white_cube',
            color=color.red,
            scale=(.4, .1),
            position=(0, -screen_height / 4),
            text='Test',
            text_origin=(0, 0),
            text_color=color.white,
            text_font='font/test.otf',
            text_size=100,
            on_click=self.start_game,
            render_queue=2  # Set the same render order as the input form
        )

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

        # Début du jeu
        jeu.jouer()

# Initialisation de l'interface graphique dans le thread principal
app = Ursina()
scene = Accueil()
app.run()
