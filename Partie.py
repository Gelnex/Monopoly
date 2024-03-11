# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
from Case import *
from Joueur import *
from Des import *
from Case_Depart import *
from Case_Prison import *
from Case_Propriete import *
from Case_Visite_Prison import *
from Case_Police import *
from Case_Professeur import *


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
class Partie:
    """
    Qui : Engels Félix
    Quand : 27/02/2024
    Quoi : recommencer tant que nombre joueur n'est pas correct et ajout de testeur basique.
    à faire : rendre l'attribut privé parceque sa marche pas et je sais pas pourquoi
    """

    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    def __init__(self, joueurs) -> None:

        ### Lister et initialiser les attributs
        self.__idPartie = 0
        self.__plateau = self.mise_en_place()
        self.__joueur_actif = 0
        self.__joueurs = joueurs
        self.__argentPlateau = 10

    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#
    @property
    def idPartie(self) -> int:
        return self.__idPartie

    @property
    def tour(self) -> int:
        return self.__tour

    @property
    def plateau(self):
        return self.__plateau

    @property
    def joueur_actif(self):
        return self.__joueur_actif

    @property
    def joueurs(self):
        return self.__joueurs
    
    @property
    def argentPlateau(self):
        return self.__argentPlateau

    # ============================================================================#
    # = MUTATEUR                                                                 =#
    # ============================================================================#

    @idPartie.setter
    def idPartie(self, nvId):
        self.__idPartie = nvId

    @tour.setter
    def tour(self, nvTour):
        self.__tour = nvTour

    @plateau.setter
    def plateau(self, nvPlateau):
        self.__plateau = nvPlateau

    @joueur_actif.setter
    def joueur_actif(self, nvActif):
        self.__joueur_actif = nvActif

    @joueurs.setter
    def joueurs(self, nvJoueurs):
        self.__joueurs = nvJoueurs
        
    @argentPlateau.setter
    def argentPlateau(self, argent):       
        self.__argentPlateau = argent
        print(f"le plateau contient maintenant {self.__argentPlateau}€ ")

    # ============================================================================#
    # = METHODE                                                                  =#
    # ============================================================================#
    def mise_en_place(self):
        # Créer un plateau de jeu avec des propriétés
        plateau = [
            Depart("Départ", 1),
            Propriete("Café", 2, "brune", 50, 15),
            Propriete("Décharge", 3, "brune", 75, 30),
            Propriete("Sous Sol", 4, "bleu Clair", 100, 45),
            Propriete("Toilette", 5, "bleu Clair", 125, 60),
            Propriete("Chambre forte", 6, "bleu Clair", 150, 75),
            Prison("prison d'Azkaban", 7),
            Visite_Prison("Visite Prison", 8),
            Propriete("Toit", 9, "rose", 175, 87),
            Case_Professeur("Professeur", 10),
            Propriete("Tante", 11, "rose", 200, 100),
            Propriete("Aire de chargement", 12, "rose", 250, 150),
            Case_Police("Police", 13),
            Propriete("Jardin public", 14, "vert", 275, 175),
            Propriete("Place du marché", 15, "vert", 300, 200),
            Propriete("Parking", 16, "vert", 325, 225),
            Case("Parc gratuit", 17),
            Prison("Électricité", 18),
            Propriete("Allée sombre", 19, "violet", 350, 250),
            Propriete("Bibliothèque", 20, "violet", 375, 275),
            Propriete("Ruelle étroite", 21, "violet", 400, 300),
            Visite_Prison("Communauté", 22),
            Propriete("Galerie d'art", 23, "orange", 425, 325),
            Propriete("Cinéma", 24, "orange", 450, 350),
            Propriete("Gare", 25, "orange", 475, 375),
            Propriete("Théâtre", 26, "rouge", 500, 400),
        ]
        return plateau
    
    def nombre_joueur(self):
        nmbrJoueur = 0
        while True:
            try:
                nmbrJoueur = int(input("Entrez le nombre de joueur (entre 2 et 6): "))
                if 2 <= nmbrJoueur <= 6:
                    return nmbrJoueur
                else:
                    print("Le nombre de joueurs doit être compris entre 2 et 6.")
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

    def identifier_joueur(self, i):
            while True:
                pseudoJoueur = input(f"Entrez le nom du {i+1}e joueur: ")
                if pseudoJoueur != "0.0":
                    return pseudoJoueur
                else:
                    print("Erreur : Veuillez entrer un pseudo différent de '0.0'.")

    # Fonction de deplacement Joueur
    def deplacement(self, joueur):
        if joueur.bloquerMouvement == False:
            # Appel la classe Des
            des = Des()
            somme_des, double = des.lancer_des()

            # Affiche la somme des dés et de l'état du doublé
            print(f"{joueur.nom} a fait une somme de dés de {somme_des}.")
            if double:
                print(f"{joueur.nom} a fait un double !")
                joueur.pouvoir(self)
            else:
                print(f"{joueur.nom} n'a pas fait de double.")

            # Donne 200 d'argent au joueurs quand il dépasse est sur ou dépasse la case départ
            if joueur.position + somme_des > len(self.plateau) + 1:
                print(f"{joueur.nom} a recu 200 car il est passé par la case départ")
                joueur.donner_argent(200)
            joueur.position = (joueur.position + somme_des) % len(self.plateau)
        else:
            print(f"le joueur {joueur.nom} est emprisonné")

    # Fonction du tour du joueur
    def tour_joueur(self):

        # Etablie le tour du joueur
        joueur = self.__joueurs[self.__joueur_actif]
        print(f"\n C'est au tour de {joueur.nom}.")

        # Deplacer Joueur
        self.deplacement(joueur)
        case_actuelle = self.__plateau[joueur.position]
        print(
            f"{joueur.nom} est sur la case {self.__plateau[joueur.position].nom}. \n Case N°",
            case_actuelle.coordonee,
        )

        # Effectuer l'action de la case actuelle
        if isinstance(case_actuelle, Propriete):
            case_actuelle.actionOr(joueur,self.__joueurs)
            if joueur.peut_acheter(case_actuelle):
                joueur.acheter_propriete(case_actuelle)
            else:
                pass
        elif isinstance(case_actuelle, Visite_Prison):
            case_actuelle.visite(joueur,self.__joueurs)
        elif isinstance(case_actuelle, Prison):
            case_actuelle.bloquerMouvement(joueur, self)
        elif isinstance(case_actuelle, Depart):
            case_actuelle.donner_argent(joueur)
        elif isinstance(case_actuelle, Case_Police):
            case_actuelle.malus(joueur,self)
        elif isinstance(case_actuelle, Case_Professeur):
            case_actuelle.bonus(joueur,self)
        elif case_actuelle.nom == "Parc gratuit":
            self.donner_argent_plateau(joueur)
        else:
            pass

        # Passer au prochain joueur
        self.__joueur_actif = (self.__joueur_actif + 1) % len(self.__joueurs)
        print(f"Il lui reste {joueur.argent}")
        input("Appuyez pour passer au tour suivant")

    # Verifie si il y a un gagnant
    def verification_gagnant(self):
        for joueur in self.__joueurs:
            if joueur.argent <= 0:
                return joueur
        return None

    # Boucle principale du jeu et vérifie la condition de victoire
    def jouer(self):
        while len(self.__joueurs) > 1:
            self.tour_joueur()
            perdant = self.verification_gagnant()

            if perdant:
                # Stocker le nom du joueur perdant
                nom_perdant = perdant.nom

                # Retirer le joueur perdant de la liste
                self.__joueurs.remove(perdant)

                # Vérifier s'il reste des joueurs actifs
                if len(self.__joueurs) == 1:
                    # Afficher le message de victoire avec le nom du joueur restant
                    print(
                        f"{nom_perdant} est en faillite. {self.__joueurs[0].nom} a gagné !"
                    )
                    break
                else:
                    # Afficher le message du joueur en faillite et continuer le jeu
                    print(f"{nom_perdant} est en faillite.")
            else:
                for joueur in self.__joueurs:
                    if joueur.argent < 0:
                        # Stocker le nom du joueur en faillite
                        nom_perdant = joueur.nom

                        # Retirer le joueur en faillite de la liste
                        self.__joueurs.remove(joueur)

                        # Afficher le message du joueur en faillite et continuer le jeu
                        print(f"{nom_perdant} est en faillite.")
                        break
    
    def donner_argent_plateau(self, joueur):
        joueur.argent += self.__argentPlateau
        print(f"vous avez reçu {self.__argentPlateau}€ et l'argent plateau est vide")
        self.__argentPlateau = 0

# ============================================================================#
# = AFFICHAGE                                                                =#
# ============================================================================#

if __name__ == "__main__":
    # Création d'une instance de la classe Partie avec une liste de joueurs vide
    partie = Partie([])
    
    # Demande du nombre de joueurs à l'utilisateur et récupération de la valeur
    nJoueur = partie.nombre_joueur()

    # Initialisation de l'indice i
    i = 1

    # Demande des noms des joueurs à l'utilisateur et stockage dans une liste
    joueur_noms = [partie.identifier_joueur(i) for i in range(nJoueur)]

    # Création d'instances de la classe Joueur à partir des noms fournis par l'utilisateur
    joueurs = [Joueur(nom) for nom in joueur_noms]

    # Création d'une nouvelle instance de la classe Partie avec les joueurs créés
    jeu = Partie(joueurs)

    # Début du jeu
    jeu.jouer()
