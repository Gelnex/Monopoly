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
from Case_Tunnel import *
from Case_Taxe import *
from ursina import *


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
        self.__plateau = self.mise_en_place()
        self.__joueur_actif = 0
        self.__joueurs = joueurs
        self.__argentPlateau = 10

    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#
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
            Depart("Case Départ", 0),
            Propriete("Café", 1, "brune", 60),
            Professeur("Professeur", 2),
            Propriete("Décharge" , 3, "brune", 60),
            Taxe("Colonel Prieto" , 4, 200),
            Tunnel("Chambre forte trois", 5),
            Propriete("Sous-sol", 6, "blanche", 100),
            Police("Police", 7),
            Propriete("Toilettes", 8, "blanche", 100),
            Propriete("Chambre forte deux", 9, "blanche", 120),
            Visite_Prison("Visite Prison", 10),
            Propriete("Toit", 11, "violet", 140),
            Propriete("Pioche", 12 , "outil", 150),
            Propriete("Tente de commandement", 13, "violet", 140),
            Propriete("Aire de chargement", 14, "violet", 160),
            Tunnel("Le hangar", 15),
            Propriete("Cidrerie", 16, "orange", 180),
            Professeur("Professeur", 17),
            Propriete("Hôpital", 18, "orange", 180),
            Propriete("Maison de Tolède", 19, "orange", 200),
            Case("Parc gratuit", 20),
            Propriete("Monastère", 21, "rouge", 220),
            Police("Police", 22),
            Propriete("Place de Callad", 23, "rouge", 220),
            Propriete("Hall", 24, "rouge", 240),
            Tunnel("Restaurant", 25),
            Propriete("Bureau du gouverneur", 26, "jaune", 260),
            Propriete("Antichambre", 27, "jaune", 260),
            Propriete("Lance-thermique", 28, "outil", 150),
            Propriete("Chambre forte inondée", 29, "jaune", 260),
            Prison("Prison", 30),
            Propriete("Camping-car de commandement", 31 , "vert", 300),
            Propriete("Réservoir d'eau de pluie", 32, "vert", 300),
            Professeur("Professeur", 33),
            Propriete("Pièce sécurisée", 34, "vert", 320),
            Tunnel("Garage", 35),
            Police("Police", 36),
            Propriete("Fabrique de la monnaie", 37, "bleu", 350),
            Taxe("Colonnel Tamayo", 38, 100),
            Propriete("La banque", 39, "bleu", 400)
        ]
        return plateau
    
    # Demande le nombre de joueur
    def nombre_joueur(self):
        nmbrJoueur = 0
        while True:
            try:
                nmbrJoueur = int(input("Entrez le nombre de joueur (entre 2 et 6) -> "))
                if 2 <= nmbrJoueur <= 6:
                    return nmbrJoueur
                else:
                    print("Le nombre de joueurs doit être compris entre 2 et 6.")
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

    # Demande le nom de chaque joueur
    def identifier_joueur(self, nombre_joueur):
        liste_joueurs = []
        i = 1
        n_joueurs = nombre_joueur
        
        while n_joueurs > 0:
            pseudoJoueur = input(f"Entrez le nom du {i}e joueur -> ")
            if isinstance(pseudoJoueur, str):
                if not (pseudoJoueur in liste_joueurs):
                    liste_joueurs.append(pseudoJoueur)
                    n_joueurs = n_joueurs - 1
                    i += 1
                else:
                    print ("Le même nom ne peut pas être utilisé 2 fois")
                
            else:
                print("Erreur : Veuillez entrer un pseudo sous forme de texte.")

        return liste_joueurs

    # Fonction de deplacement Joueur
    def deplacement(self, joueur):
        if joueur.mouvement == False:
            # Appel la classe Des
            des = Des()
            somme_des, double = des.lancer_des()

            # Affiche la somme des dés et de l'état du double
            print(f"{joueur.nom} a fait une somme de dés de {somme_des}.")
            if double:
                print(f"{joueur.nom} a fait un double !")
                joueur.position = (joueur.position + somme_des) % len(self.plateau)
                joueur.pouvoir(self)
            else:
                print(f"{joueur.nom} n'a pas fait de double.")
                joueur.position = (joueur.position + somme_des) % len(self.plateau)

            # Donne 200 d'argent au joueurs quand il dépasse est sur ou dépasse la case départ
            if joueur.position + somme_des > len(self.plateau) + 1:
                print(f"{joueur.nom} a recu 200€ car il est passé par la case départ")
                joueur.donner_argent(200)
                joueur.position = (joueur.position + somme_des) % len(self.plateau)
        else:
            print(f"Le joueur {joueur.nom} est emprisonné")

    # Fonction du tour du joueur
    def tour_joueur(self):

        # Etablie le tour du joueur
        joueur = self.__joueurs[self.__joueur_actif]
        print(f"\n C'est au tour de {joueur.nom}.")

        # Deplacer Joueur
        self.deplacement(joueur)
        case_actuelle = self.__plateau[joueur.position]
        print(
            f"{joueur.nom} est sur la case {self.__plateau[joueur.position].nom}. \n Case N° {case_actuelle.coordonee}"
        )

        # Effectuer l'action de la case actuelle
        match case_actuelle:
            case Propriete():
                case_actuelle.actionOr(joueur, self)
                # Vérifie si le joueur peut acheter
                if joueur.peut_acheter(case_actuelle) == True:
                    joueur.acheter_propriete(case_actuelle, self)
                else:
                    mettre_aux_encheres(case_actuelle)
            case Visite_Prison():
                case_actuelle.visite(joueur, self.__joueurs)
            case Prison():
                case_actuelle.bloquerMouvement(joueur, self)
            case Depart():
                case_actuelle.donner_argent(joueur)
            case Police():
                case_actuelle.malus(joueur, self)
            case Professeur():
                case_actuelle.bonus(joueur, self)
            case Tunnel():
                case_actuelle.transporter(joueur)
            case Taxe():
                case_actuelle.malus(joueur, self)
            case _ if case_actuelle.nom == "Parc gratuit":
                self.donner_argent_plateau(joueur)
            case _:
                pass

        # Passer au prochain joueur
        self.__joueur_actif = (self.__joueur_actif + 1) % len(self.__joueurs)
        print(f"Il lui reste {joueur.argent}€")
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
                pass

    # Donne l'argent du plateau à un joueur
    def donner_argent_plateau(self, joueur):
        joueur.argent += self.__argentPlateau
        print(f"Vous avez reçu {self.__argentPlateau}€ et l'argent plateau est vide")
        self.__argentPlateau = 0
        
    def mettre_aux_encheres(self, propriete:Propriete):
        prix = int(propriete.prix / 1.5)
        encherrisseurIndex = None
        print("\n \n *****les encheres ont commencé !******")
        print(f"le prix de depart est {prix}")
        
        enchere_en_cours = True
        while enchere_en_cours:
            inputEnchere = input("Quel joueur souhaite mettre une enchere ? (laisser vide pour arreter l'enchere) >>> ")
            if inputEnchere != "":
                boucle = True
                while boucle:
                    pasTrouve = True
                    for iJoueur in self.joueurs:
                        if iJoueur.nom == inputEnchere:
                            boucle = False
                            pasTrouve = False
                            encherrisseurIndex = self.joueurs.index(iJoueur)
                    if pasTrouve:
                        inputEnchere = input("Le joueur n'as pas été trouver, veuiller réessayer >>> ")
                        
                negociation_en_cours = True
                while negociation_en_cours:   
                    try:
                        prixPropose = int(input("Quel est le prix auquel vous voudriez monter l'enchere ? >>> "))
                    except:
                        print("L'entrée doit etre un entier.")
                    else:
                        if prixPropose > prix:
                            prix = prixPropose
                            negociation_en_cours = False
            else:
                enchere_en_cours = False
                if inputEnchere == "" and encherrisseurIndex != None:
                    propriete.acheter_enchere(self.joueurs[encherrisseurIndex], prix)
                else:
                    print("Personne n'as voulu de l'enchere")


# ============================================================================#
# = URSINA                                                                   =#
# ============================================================================#
class MaScene(Entity):
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
                position=(0, -.3)
            )