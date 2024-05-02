<?php
	include('conn.php');
	$id=$_GET['id'];
	$query=mysqli_query($conn,"select * from `cases` where coordonnee='$id'");
	$row=mysqli_fetch_array($query);
?>
<!DOCTYPE html>
<html>
<head>
<title>Monopoly DB editor</title>
</head>
<body>
	<h2>Edit</h2>
	<form method="POST" action="update.php?id=<?php echo $id; ?>">
		<label>coordonnee:</label><input type="text" value="<?php echo $row['coordonnee']; ?>" name="coordonnee">
		<label>nom:</label><input type="text" value="<?php echo $row['nom']; ?>" name="nom">
		<label>type:</label><input type="text" value="<?php echo $row['type']; ?>" name="type">
		<label>prix:</label><input type="text" value="<?php echo $row['prix']; ?>" name="prix">
		<label>famille:</label><input type="text" value="<?php echo $row['famille']; ?>" name="famille">
		<input type="submit" name="submit">
		<a href="index.php">Back</a>
	</form>
</body>
</html>