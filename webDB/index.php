<!DOCTYPE html>
<html>
<head>
<title>Monopoly DB editor</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<a href="https://github.com/Gelnex/Monopoly/issues/new">
   <span title="Certaines cases modifiées pourraient ne pas agir comme prévu dans le jeu normal. Veuillez signaler tout comportement imprévu.">⚠ attention ⚠</span>
</a>

	<div>
		<form method="POST" action="add.php">
			<label>Coordonnee:</label><input type="number" name="coordonnee" min=0>
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
			<label>Famille:</label><input type="text" name="famille">
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
				?>
			</tbody>
		</table>
	</div>
</body>
</html>