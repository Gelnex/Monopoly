<?php
	include('conn.php');
	$id=$_GET['id'];
	// lier les données localement
	$coordonnee=$_POST['coordonnee'];
	$nom=$_POST['nom'];
	$type=$_POST['type'];
	$prix=$_POST['prix'];
	$famille=$_POST['famille'];
	
	function QuerySelector($type, $nom, $prix, $famille, $id) {
		// verifier pour chaque type possible la requete qui devrait etre envoyer
		switch ($type) {
			case "Propriete":
				$query = "UPDATE `cases` SET `nom`='$nom',`type`='$type',`prix`='$prix',`famille`='$famille' WHERE coordonnee = '$id'";
				break;
			case "Taxe":
				$query = "UPDATE `cases` SET `nom`='$nom',`type`='$type',`prix`='$prix' WHERE coordonnee = '$id'";
				break;
			default:
				$query = "UPDATE `cases` SET `nom`='$nom',`type`='$type' WHERE coordonnee = '$id'";
				break;
		}
		return $query;
	}
	
	$query = QuerySelector($type, $nom, $prix, $famille, $id);
	
	// envoyer la requete et si impossible retourne une erreur
	if(mysqli_query($conn, $query)) {
		header('location:index.php');
		exit();
	} else {
		echo "Error: " . mysqli_error($conn);
	}
?>