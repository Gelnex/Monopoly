<?php
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
		<label for="famille">Famille:</label>
			<select name="famille" id="famille">
					<option value="" <?php echo selected("", $row['famille']); ?>>--Vide--</option>
					<option value="brune" <?php echo selected("brune", $row['famille']); ?>>brune</option>
					<option value="blanche" <?php echo selected("blanche", $row['famille']); ?>>blanche</option>
					<option value="violet" <?php echo selected("violet", $row['famille']); ?>>violet</option>
					<option value="outil" <?php echo selected("outil", $row['famille']); ?>>outil</option>
					<option value="orange" <?php echo selected("orange", $row['famille']); ?>>orange</option>
					<option value="rouge" <?php echo selected("rouge", $row['famille']); ?>>rouge</option>
					<option value="jaune" <?php echo selected("jaune", $row['famille']); ?>>jaune</option>
					<option value="vert" <?php echo selected("vert", $row['famille']); ?>>vert</option>
					<option value="bleu" <?php echo selected("bleu", $row['famille']); ?>>bleu</option>
				</select>
		<input type="submit" name="submit">
		<a href="index.php">Back</a>
	</form>
</body>
</html>