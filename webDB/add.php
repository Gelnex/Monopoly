<?php
	include('conn.php');
	
	$coordonnee=$_POST['coordonnee'];
	$nom=$_POST['nom'];
	$type=$_POST['type'];
	$prix=$_POST['prix'];
	$famille=$_POST['famille'];
		
	mysqli_query($conn,"INSERT INTO `cases`(`coordonnee`, `nom`, `type`, `prix`, `famille`) VALUES ($coordonnee,$nom,$type,$prix,$famille)");
	header('location:index.php');
	
?>