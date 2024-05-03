<?php

include('conn.php');

$coordonnee = $_POST['coordonnee'] ?? null;
$nom = $_POST['nom'] ?? null;
$type = $_POST['type'] ?? null;
$prix = $_POST['prix'] ?? null;
$famille = $_POST['famille'] ?? null;

function QuerySelector($type, $coordonnee, $nom, $prix, $famille) {
    switch ($type) {
        case "Propriete":
            $query = "INSERT INTO `cases`(`coordonnee`, `nom`, `type`, `prix`, `famille`) VALUES ('$coordonnee','$nom','$type','$prix','$famille')";
            break;
        case "Taxe":
            $query = "INSERT INTO `cases`(`coordonnee`, `nom`, `type`, `prix`) VALUES ('$coordonnee','$nom','$type','$prix')";
            break;
        default:
            $query = "INSERT INTO `cases`(`coordonnee`, `nom`, `type`) VALUES ('$coordonnee','$nom','$type')";
            break;
    }
    return $query;
}

$query = QuerySelector($type, $coordonnee, $nom, $prix, $famille);

if(mysqli_query($conn, $query)) {
    header('location:index.php');
    exit();
} else {
    echo "Error: " . mysqli_error($conn);
}
?>
