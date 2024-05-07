<?php
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

function selected($typetxt,$sql){
	if($typetxt == $sql){
		return "selected";
	}
}

	include('conn.php');
	$id=$_GET['id'];
	$query=mysqli_query($conn,"select * from `cases` where coordonnee='$id'");
	$row=mysqli_fetch_array($query);
?>
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="style.css">
<title>Monopoly DB editor</title>
</head>
<body>
	<h2>Edit</h2>
	<form method="POST" action="update.php?id=<?php echo $id; ?>">
	<label>coordonnee:</label><input type="number" min=0 value="<?php echo $row['coordonnee']; ?>" name="coordonnee">
		<label>nom:</label><input type="text" value="<?php echo $row['nom']; ?>" name="nom">
		<label for="type">Type:</label>
		<select name="type" id="type">
			<option value="Depart" <?php echo selected("Depart", $row['type']); ?>>Depart</option>
			<option value="Propriete" <?php echo selected("Propriete", $row['type']); ?>>Propriete</option>
			<option value="Professeur" <?php echo selected("Professeur", $row['type']); ?>>Professeur</option>
			<option value="Police" <?php echo selected("Police", $row['type']); ?>>Police</option>
			<option value="Taxe" <?php echo selected("Taxe", $row['type']); ?>>Taxe</option>
			<option value="Visite_Prison" <?php echo selected("Visite_Prison", $row['type']); ?>>Visite_Prison</option>
			<option value="Prison" <?php echo selected("Prison", $row['type']); ?>>Prison</option>
			<option value="Tunnel" <?php echo selected("Tunnel", $row['type']); ?>>Tunnel</option>
			<option value="Case" <?php echo selected("Case", $row['type']); ?>>Case</option>
		</select>
		<label>prix:</label><input type="number" min=0 value="<?php echo $row['prix']; ?>" name="prix">
		<label>famille:</label><input type="text" value="<?php echo $row['famille']; ?>" name="famille">
		<input type="submit" name="submit">
		<a href="index.php">Back</a>
	</form>
</body>
</html>