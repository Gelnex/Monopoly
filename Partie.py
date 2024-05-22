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
from SQL import connectionDB


# ============================================================================#
# = DEFINITION DE LA CLASSE                                                  =#
# ============================================================================#
"""
    Qui : Engels Félix
    Quand : 27/02/2024
    Quoi : Création de partie (classe principale du jeu)
"""
class Partie:

    # ============================================================================#
    # = CONSTRUCTEURS / DESTRUCTEUR                                              =#
    # ============================================================================#
    """
        Qui : Engels Félix
        Quand : 27/02/2024
        Quoi : Constructeur, rendre attribut privé et setter
    """
    def __init__(self, joueurs) -> None:

        ### Lister et initialiser les attributs
        self.__plateau = self.mise_en_place()
        self.__longueur_plateau = 0
        self.__joueur_actif = 0
        self.__joueurs = joueurs
        self.__argentPlateau = 0

    # ============================================================================#
    # = ACCESSEURS                                                               =#
    # ============================================================================#
    @property
    def plateau(self):
        return self.__plateau
    
    @property
    def longueur_plateau(self):
        return self.__longueur_plateau

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
    """
        Qui : Haye Noa
        Quand : 05/03/2024
        Quoi : Création de Mise en place, Deplacement, Tour Joueur et Jouer
    """
    def mise_en_place(self):
        """
        Qui : Engles Felix
        Quand : 06/05/2024
        Quoi : Importation de la base de données + option si erreur
        """

        ### Essai de connection à la base de donnée ###
        db = connectionDB("cases")
        if db != None:
            plateau = []
            for i in db:
                match i[2]:
                    case "Propriete":
                       plateau.append(Propriete(i[1], i[0], i[4], i[3]))
                    case "Visite_Prison":
                        plateau.append(Visite_Prison(i[1], i[0]))
                    case "Prison":
                        plateau.append(Prison(i[1], i[0]))
                    case "Depart":
                        plateau.append(Depart(i[1], i[0]))
                    case "Police":
                        plateau.append(Police(i[1], i[0]))
                    case "Professeur":
                        plateau.append(Professeur(i[1], i[0]))
                    case "Tunnel":
                        plateau.append(Tunnel(i[1], i[0]))
                    case "Taxe":
                        plateau.append(Taxe(i[1], i[0],i[3]))
                    case "Case":
                        plateau.append(Case(i[1], i[0]))
                    case _:
                        raise TypeError("case non trouvé")
            return plateau
        else:
            print("connexion a la base de donnée impossible donc utilisation du plateau local")
            plateau = [
                Depart((0, 0, 0), "Case Départ", 0),
                Propriete((1, 0, 0), "Café", 1, "brune", 60),
                Professeur((2, 0, 0), "Professeur", 2),
                Propriete((3, 0, 0), "Décharge" , 3, "brune", 60),
                Taxe((4, 0, 0), "Colonel Prieto" , 4, 200),
                Tunnel((5, 0, 0), "Chambre forte trois", 5),
                Propriete((6, 0, 0), "Sous-sol", 6, "blanche", 100),
                Police((7, 0, 0), "Police", 7),
                Propriete((8, 0, 0), "Toilettes", 8, "blanche", 100),
                Propriete((9, 0, 0), "Chambre forte deux", 9, "blanche", 120),
                Visite_Prison((10, 0, 0), "Visite Prison", 10),
                Propriete((10, 0, 1), "Toit", 11, "violet", 140),
                Propriete((10, 0, 2), "Pioche", 12 , "outil", 150),
                Propriete((10, 0, 3), "Tente de commandement", 13, "violet", 140),
                Propriete((10, 0, 4), "Aire de chargement", 14, "violet", 160),
                Tunnel((10, 0, 5), "Le hangar", 15),
                Propriete((10, 0, 6), "Cidrerie", 16, "orange", 180),
                Professeur((10, 0, 7), "Professeur", 17),
                Propriete((10, 0, 8), "Hôpital", 18, "orange", 180),
                Propriete((10, 0, 9), "Maison de Tolède", 19, "orange", 200),
                Case((10, 0, 10), "Parc gratuit", 20),
                Propriete((9, 0, 10), "Monastère", 21, "rouge", 220),
                Police((8, 0, 10), "Police", 22),
                Propriete((7, 0, 10), "Place de Callad", 23, "rouge", 220),
                Propriete((6, 0, 10), "Hall", 24, "rouge", 240),
                Tunnel((5, 0, 10), "Restaurant", 25),
                Propriete((4, 0, 10), "Bureau du gouverneur", 26, "jaune", 260),
                Propriete((3, 0, 10), "Antichambre", 27, "jaune", 260),
                Propriete((2, 0, 10), "Lance-thermique", 28, "outil", 150),
                Propriete((1, 0, 10), "Chambre forte inondée", 29, "jaune", 260),
                Prison((0, 0, 10), "Prison", 30),
                Propriete((0, 0, 9), "Camping-car de commandement", 31 , "vert", 300),
                Propriete((0, 0, 8), "Réservoir d'eau de pluie", 32, "vert", 300),
                Professeur((0, 0, 7), "Professeur", 33),
                Propriete((0, 0, 6), "Pièce sécurisée", 34, "vert", 320),
                Tunnel((0, 0, 5), "Garage", 35),
                Police((0, 0, 4), "Police", 36),
                Propriete((0, 0, 3), "Fabrique de la monnaie", 37, "bleu", 350),
                Taxe((0, 0, 2), "Colonnel Tamayo", 38, 100),
                Propriete((0, 0, 1), "La banque", 39, "bleu", 400)
            ]
        return plateau
    
    """
        Qui : Haye Noa
        Quand : 15/05/2024
        Quoi : Demande le nombre de joueur
    """
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

    """
        Qui : Haye Noa
        Quand : 15/04/2024
        Quoi : Demande le nom de chaque joueur
    """
    def identifier_joueur(self, nombre_joueur):
        liste_joueurs = []
        i = 1
        n_joueurs = nombre_joueur
        
        while n_joueurs > 0:
            pseudoJoueur = input(f"Entrez le nom du {i}e joueur -> ")
            if isinstance(pseudoJoueur, str) and pseudoJoueur != "":
                if pseudoJoueur.lower() not in [joueur.lower() for joueur in liste_joueurs]:
                    liste_joueurs.append(pseudoJoueur)
                    n_joueurs = n_joueurs - 1
                    i += 1
                else:
                    print ("Le même nom ne peut pas être utilisé 2 fois")
                
            else:
                print("Erreur : Veuillez entrer un pseudo sous forme de texte.")

        return liste_joueurs

    """
        Qui : Haye Noa
        Quand : 05/03/2024
        Quoi : Fonction qui sert au déplacement du joueur
    """
    def deplacement(self, joueur):
        if joueur.mouvement == False:
            # Appel la classe Des
            des = Des()
            somme_des, double = des.lancer_des()
            

            if joueur.position + somme_des >= 10:
                joueur.pion.position = (0, 0.5, 10)
                joueur.pion.position += (somme_des, 0, 0)
            elif joueur.position + somme_des >= 20:
                joueur.pion.position = (10, 0.5, 10)
                joueur.pion.position -= (0, 0, somme_des)
            else:
                joueur.pion.position += (0, 0, somme_des)



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

    """
        Qui : Haye Noa
        Quand : 05/03/2024
        Quoi : Définition du tour joueur
    """
    def tour_joueur(self):

        # Etablir le tour du joueur
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
                    self.mettre_aux_encheres(case_actuelle)
                self.CheckFamille(joueur, case_actuelle.famille)
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

    """
        Qui : Haye Noa
        Quand : 05/03/2024
        Quoi : Vérifie si il y a un gagnant
    """
    def verification_gagnant(self):
        for joueur in self.__joueurs:
            if joueur.argent <= 0:
                return joueur
        return None

    
    """
        Qui : Haye Noa
        Quand : 05/03/2024
        Quoi : Vérifie la condition de victoire
    """
    def jouer(self):
    
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
            else:
                # Afficher le message du joueur en faillite et continuer le jeu
                print(f"{nom_perdant} est en faillite.")
        else:
            pass

    """
        Qui : Engels Felix
        Quand : 21/04/2024
        Quoi : Ajoute l'argent au plateau
    """
    def donner_argent_plateau(self, joueur):
        joueur.argent += self.__argentPlateau
        print(f"{joueur.nom} a reçu {self.__argentPlateau}€ et l'argent plateau est vide")
        self.__argentPlateau = 0

    """
        Qui : Engles Felix
        Quand : 17/04/2024
        Quoi : Sert a enchérire quand une propriete n'est pas acheté
    """
    def mettre_aux_encheres(self, propriete: Propriete):
        prix = int(propriete.prix / 1.5)
        print("\n \n *****les encheres ont commencé !******")
        print(f"le prix de départ est {prix}")
        
        enchere_en_cours = True
        encherrisseurIndex = None 

        while enchere_en_cours:
            inputEnchere = input("Quel joueur souhaite mettre une enchere ? (laisser vide pour arreter l'enchere) >>> ")
            if inputEnchere != "":
                iJoueur = None
                for joueur in self.joueurs:
                    if joueur.nom == inputEnchere and (encherrisseurIndex is None or joueur.nom != self.joueurs[encherrisseurIndex].nom):
                        iJoueur = joueur
                        break
                
                if iJoueur is not None:
                    encherrisseurIndex = self.joueurs.index(iJoueur)
                    
                    negociation_en_cours = True
                    while negociation_en_cours:   
                        try:
                            prixPropose = int(input("Quel est le prix auquel vous voudriez monter l'enchere ? >>> "))
                        except ValueError:
                            print("L'entrée doit être un entier.")
                        else:
                            if self.joueurs[encherrisseurIndex].argent > prixPropose and prixPropose > prix:
                                prix = prixPropose
                                negociation_en_cours = False
                else:
                    print("Le joueur n'a pas été trouvé ou est deja le top encherisseur, veuillez réessayer.")
            else:
                enchere_en_cours = False
                
        if encherrisseurIndex is not None:
            propriete.acheter_enchere(self.joueurs[encherrisseurIndex], prix)
        else:
            print("Personne n'a voulu de l'enchere")

    """
        Qui : Engles Felix
        Quand : 07/04/2024
        Quoi : Verifie si un joueur possède toute la familles
    """
    def CheckFamille(self,joueur,famille):
        totalFamille = True
        for case in self.plateau:
            if isinstance(case,Propriete):
                if case.famille == famille:
                    if not(case.proprietaire == joueur):
                        totalFamille = False
        if totalFamille:
            joueur.famille.append(famille)
            print(f"{joueur.nom} possede toutes les propriete de la famille {famille}, les loyers sont doublés.")
