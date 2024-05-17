<!DOCTYPE html>
<html>
<head>
<title>Monopoly DB editor</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<a href="..\site statique\index.html">
   <button title="retourner a l'acceuil">🏠</button>
</a>

	<div>
		<form method="POST" action="add.php">
		<label>Coordonnee:</label><input type="number" name="coordonnee" min="0">
			<label>Nom:</label><input type="text" name="nom">
				<label for="type">Type:</label>
				<select name="type" id="type">
					<option value="Depart">Depart</option>
					<option value="Propriete">Propriete</option>
					<option value="Professeur">Professeur</option>
					<option value="Police">Police</option>
					<option value="Taxe">Taxe</option>
					<option value="Visite_Prison">Visite_Prison</option>
					<option value="Prison">Prison</option>
					<option value="Tunnel">Tunnel</option>
					<option value="Case">Case</option>
				</select>
			<label>Prix:</label><input type="number" name="prix" min=0>
			<label for="famille">Famille:</label>
			<select name="famille" id="famille">
					<option value="" select>--Vide--</option>
					<option value="brune">brune</option>
					<option value="blanche">blanche</option>
					<option value="violet">violet</option>
					<option value="outil">outil</option>
					<option value="orange">orange</option>
					<option value="rouge">rouge</option>
					<option value="jaune">jaune</option>
					<option value="vert">vert</option>
					<option value="bleu">bleu</option>
				</select>
			<input type="submit" name="add">
			<a href="reset.php" title="Retourner la base de donné à son etat original">Hard reset</a>
		</form>
	</div>
	<br>
	<div>
		<table border="1">
			<thead>
				<th>Coordonnee</th>
				<th>Nom</th>
				<th>Type</th>
				<th>Prix</th>
				<th>Famille</th>
				<th></th>
			</thead>
			<tbody>
				<?php
					include('conn.php');
					$query=mysqli_query($conn,"select * from `cases`");
					while($row=mysqli_fetch_array($query)){
						?>
						<tr>
							<td><?php echo $row['coordonnee']; ?></td>
							<td><?php echo $row['nom']; ?></td>
							<td><?php echo $row['type']; ?></td>
							<td><?php echo $row['prix']; ?></td>
							<td><?php echo $row['famille']; ?></td>
							<td>
								<a href="edit.php?id=<?php echo $row['coordonnee']; ?>">Modifier</a>
								<a href="delete.php?id=<?php echo $row['coordonnee']; ?>">Supprimer</a>
							</td>
						</tr>
						<?php
					}
				$result = mysqli_query($conn, 'SELECT COUNT(*) AS count FROM cases'); 
				$length = mysqli_fetch_assoc($result)['count']; // Fetch the count directly
				if ($length % 4 != 0) {
					echo "La longueur totale de la table n'est pas un multiple de 4, cela risque de causer des problèmes avec la partie graphique du jeu.";
				}
			?>
			</tbody>
		</table>
	</div>
</body>
</html>