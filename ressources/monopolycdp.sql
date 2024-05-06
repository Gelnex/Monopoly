-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Dim 21 Avril 2024 à 12:56
-- Version du serveur :  5.7.11
-- Version de PHP :  7.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `monopolycdp`
--

-- --------------------------------------------------------

--
-- Structure de la table `carte_or`
--

CREATE TABLE `carte_or` (
  `pouvoir` varchar(20) NOT NULL,
  `valeur` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `cases`
--

CREATE TABLE `cases` (
  `coordonnee` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `type` varchar(50) NOT NULL,
  `prix` int(11) DEFAULT NULL,
  `famille` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `cases`
--

INSERT INTO `cases` (`coordonnee`, `nom`, `type`, `prix`, `famille`) VALUES
(0, 'Case Depart', 'Depart', NULL, NULL),
(1, 'Café', 'Propriete', 60, 'brune'),
(2, 'Professeur', 'Professeur', NULL, NULL),
(3, 'Décharge', 'Propriete', 60, 'brune'),
(4, 'Colonel Prieto', 'Taxe', 200, NULL),
(5, 'Chambre forte trois', 'Tunnel', NULL, NULL),
(6, 'Sous-sol', 'Propriete', 100, 'blanche'),
(7, 'Police', 'Police', NULL, NULL),
(8, 'Toilettes', 'Propriete', 100, 'blanche'),
(9, 'Chambre forte deux', 'Propriete', 120, 'blanche'),
(10, 'Visite Prison', 'Visite_Prison', NULL, NULL),
(11, 'Toit', 'Propriete', 140, 'violet'),
(12, 'Pioche', 'Propriete', 150, 'outil'),
(13, 'Tente de commandement', 'Propriete', 140, 'violet'),
(14, 'Aire de chargement', 'Propriete', 160, 'violet'),
(15, 'Le hangar', 'Tunnel', NULL, NULL),
(16, 'Cidrerie', 'Propriete', 180, 'orange'),
(17, 'Professeur', 'Professeur', NULL, NULL),
(18, 'Hôpital', 'Propriete', 180, 'orange'),
(19, 'Maison de Tolède', 'Propriete', 200, 'orange'),
(20, 'Parc gratuit', 'Case', NULL, NULL),
(21, 'Monastère', 'Propriete', 220, 'rouge'),
(22, 'Police', 'Police', NULL, NULL),
(23, 'Place de Callad', 'Propriete', 220, 'rouge'),
(24, 'Hall', 'Propriete', 240, 'rouge'),
(25, 'Restaurant', 'Tunnel', NULL, NULL),
(26, 'Bureau du gouverneur', 'Propriete', 260, 'jaune'),
(27, 'Antichambre', 'Propriete', 260, 'jaune'),
(28, 'Lance-thermique', 'Propriete', 150, 'outil'),
(29, 'Chambre forte inondée', 'Propriete', 260, 'jaune'),
(30, 'Prison', 'Prison', NULL, NULL),
(31, 'Camping-car de commandement', 'Propriete', 300, 'vert'),
(32, 'Réservoir d eau de pluie', 'Propriete', 300, 'vert'),
(33, 'Professeur', 'Professeur', NULL, NULL),
(34, 'Pièce sécurisée', 'Propriete', 320, 'vert'),
(35, 'Garage', 'Tunnel', NULL, NULL),
(36, 'Police', 'Police', NULL, NULL),
(37, 'Fabrique de la monnaie', 'Propriete', 350, 'bleu'),
(38, 'Colonnel Tamayo', 'Taxe', 100, NULL),
(39, 'La banque', 'Propriete', 400, 'bleu');

-- --------------------------------------------------------

--
-- Structure de la table `personnage`
--

CREATE TABLE `personnage` (
  `nom` varchar(255) NOT NULL,
  `pouvoir` varchar(50) DEFAULT NULL,
  `valeur` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Index pour les tables exportées
--

--
-- Index pour la table `carte_or`
--
ALTER TABLE `carte_or`
  ADD PRIMARY KEY (`pouvoir`);

--
-- Index pour la table `cases`
--
ALTER TABLE `cases`
  ADD KEY `coordonnee` (`coordonnee`),
  ADD KEY `coordonnee_2` (`coordonnee`);

--
-- Index pour la table `personnage`
--
ALTER TABLE `personnage`
  ADD PRIMARY KEY (`nom`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
