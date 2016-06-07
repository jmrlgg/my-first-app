<!--
*
*          ADD / Create / Edit / Delete News File
*             Made on 1.18.2008 by: lilpimpinbt
*
-->
<html> <body>
	<?php


// The Database settings


// check if POST Var's are set
if(isset($_POST['heading'], $_POST['author'], $_POST['email'], $_POST['bulletin'])) {

	require('config/db_config.php');

		$predheading = $_POST['heading'];
		$predauthor = $_POST['author'];
		$predemail = $_POST['email'];
		$predbulletin = $_POST['bulletin'];
		

		$query = "INSERT INTO predections SET
		heading = '$predheading',
		author = '$predauthor',
		email = '$predemail',
		bulletin = '$predbulletin',
		date = CURDATE()";
		$ok = @mysql_query($query);

// Check for Errors Adding News
	if(!$ok) {

		exit('Database error storing the bulletin: ' . mysql_error());

		}

}
?>

	<form action="<?php $_SERVER['PHP_SELF']; ?>" method="POST">
	<b>Heading:</b> <input type="text" name="heading"><br><br>
	<b>Author: </b><input type="text" name="author"><br><br>
	<b>Email:</b> <input type="text" name="email"><br><br>
	<b>Bulletin:</b> <textarea rows="8" cols="50" name="bulletin">Enter the predection here!</textarea><br> <br> <br>
	<input type="submit" value="Submit">
	</form>



</body></html>