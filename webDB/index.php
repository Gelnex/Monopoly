<!DOCTYPE html>
<html>
<head>
<title>Basic MySQLi Commands</title>
</head>
<body>
	<div>
		<form method="POST" action="add.php">
			<label>Coordonnee:</label><input type="text" name="coordonnee">
			<label>Nom:</label><input type="text" name="nom">
			<label>Type:</label><input type="text" name="type">
			<label>Prix:</label><input type="text" name="prix">
			<label>Famille:</label><input type="text" name="famille">
			<input type="submit" name="add">
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
								<a href="edit.php?id=<?php echo $row['coordonnee']; ?>">Edit</a>
								<a href="delete.php?id=<?php echo $row['coordonnee']; ?>">Delete</a>
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