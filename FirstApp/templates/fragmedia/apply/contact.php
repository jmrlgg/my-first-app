<html>
<head>
</head>
<body>
<?php
$firstname = $_POST['firstname'];
$lastname = $_POST['lastname']
$email = $_POST['email'];
$position = $_POST['position'];
$referred = $_POST['referred'];
$comments = $_POST['comments'];
?>

<form method="post" action="sendmail.php">
  *First Name: <input name="firstname" type="text"><br>
  *Last Name: <input name="lastname" type="text"><br>
  *Email: <input name="email" type="text"/<br>
  General Question: <input type="radio" name="sex" value="male"> <br>
  Price Quote: <input type="radio" name="sex" value="female"> <br>
  *Query Selection
	<select name="type">
	<option value="design">Complete Design</option>
	<option value="cms" selected="selected">Custom CMS</option>
	<option value="site_redo" selected="selected">Site Redo/Remake</option>
	<option value="repair">Computer Repair/Installation</option>
		<option value="repair">General Question</option>
	</select><br>
  Referred By: <input name="referred" type="text"><br>
  Description/Question:<br> <textarea name="comments" rows="15" cols="40">
  </textarea><br>
  <input type="submit">
  * Required Fields
</form>



</body>
</html>