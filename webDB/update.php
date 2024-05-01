<?php
	include('conn.php');
	$id=$_GET['id'];
	
	$coordonnee=$_POST['coordonnee'];
	$nom=$_POST['nom'];
	$type=$_POST['type'];
	$prix=$_POST['prix'];
	$famille=$_POST['famille'];
	
	mysqli_query($conn,"UPDATE `cases` SET `coordonnee`='$coordonnee',`nom`='$nom',`type`='$type',`prix`='$prix',`famille`='$famille' WHERE coordonnee = '$id'");
	header('location:index.php');
?>