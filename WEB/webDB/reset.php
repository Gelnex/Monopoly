<?php
include('conn.php');

$query = "TRUNCATE TABLE cases;
INSERT INTO cases (coordonnee, nom, type, prix, famille) VALUES
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
(32, 'Réservoir d\\'eau de pluie', 'Propriete', 300, 'vert'),
(33, 'Professeur', 'Professeur', NULL, NULL),
(34, 'Pièce sécurisée', 'Propriete', 320, 'vert'),
(35, 'Garage', 'Tunnel', NULL, NULL),
(36, 'Police', 'Police', NULL, NULL),
(37, 'Fabrique de la monnaie', 'Propriete', 350, 'bleu'),
(38, 'Colonnel Tamayo', 'Taxe', 100, NULL),
(39, 'La banque', 'Propriete', 400, 'bleu');
";

if(mysqli_multi_query($conn, $query)) {
    header('location:index.php');
    exit();
} else {
    echo "Error: " . mysqli_error($conn);
}
?>
