<?php
	$id=$_GET['id'];
	include('conn.php');
	mysqli_query($conn,"delete from `cases` where coordonnee='$id'");
	header('location:index.php');
?>